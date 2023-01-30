
import datetime
from datetime import date
from leave.models import Leave, LeaveSummary
from mysite.share.views import getUsername, handleInput, urlResponse, verifyAndGenNewToken, sessionExpiredResponse, wrongParameterResponse

def leaveSummary(request):
    authorization = verifyAndGenNewToken(request.headers['Authorization'])
    if authorization == '':
        return sessionExpiredResponse()
    username = getUsername(authorization)
    if username is None:
        return wrongParameterResponse()
    leaveSummary = LeaveSummary.objects.filter(username=username, is_deleted=0)
    return urlResponse({'data': [LeaveSummary.deserialize(ls) for ls in leaveSummary]}, 200, authorization)

def leaveComing(request):
    authorization = verifyAndGenNewToken(request.headers['Authorization'])
    if authorization == '':
        return sessionExpiredResponse()
    username = getUsername(authorization)
    if username is None:
        return wrongParameterResponse()
    leave = Leave.objects.filter(username=username, leave_date__gte=date.today(), rejected_remark='', is_deleted=0).exclude(approved_by='').order_by('leave_date')
    return urlResponse({'data': [Leave.deserialize(l) for l in leave]}, 200, authorization)

def leavePending(request):
    authorization = verifyAndGenNewToken(request.headers['Authorization'])
    if authorization == '':
        return sessionExpiredResponse()
    username = getUsername(authorization)
    if username is None:
        return wrongParameterResponse()
    leave = Leave.objects.filter(username=username, approved_by='', rejected_remark='', is_deleted=0).order_by('leave_date')
    return urlResponse({'data': [Leave.deserialize(l) for l in leave]}, 200, authorization)

def leaveHistory(request):
    authorization = verifyAndGenNewToken(request.headers['Authorization'])
    if authorization == '':
        return sessionExpiredResponse()
    username = getUsername(authorization)
    if username is None:
        return wrongParameterResponse()
    leave = Leave.objects.filter(username=username, leave_date__lt=date.today(), is_deleted=0).exclude(approved_by='').order_by('-leave_date')
    return urlResponse({'data': [Leave.deserialize(l) for l in leave]}, 200, authorization)

def leaveApproval(request):
    authorization = verifyAndGenNewToken(request.headers['Authorization'])
    if authorization == '':
        return sessionExpiredResponse()
    username = handleInput(request, ['username'], 'GET')
    if username is None:
        return wrongParameterResponse()
    leave = Leave.objects.filter(approver=username, approved_by='', is_deleted=0).order_by('-leave_date')
    return urlResponse({'data': [Leave.deserialize(l) for l in leave]}, 200, authorization)

def applyLeave(request):
    authorization = verifyAndGenNewToken(request.headers['Authorization'])
    if authorization == '':
        return sessionExpiredResponse()
    username = getUsername(authorization)
    leave_type, leave_from, fromTime, leave_to, toTime, approver, attachment, remark = handleInput(request, 
        ['leave_type', 'from', 'fromTime', 'to', 'toTime', 'approver', 'attachment', 'remark'], 'POST')
    leaveFrom = leave_from.split('T')
    startDate = datetime.datetime(leaveFrom[0], leaveFrom[1], leaveFrom[2], 0, 0)
    leaveTo = leave_to.split('T')
    endDate = datetime.datetime(leaveTo[0], leaveTo[1], leaveTo[2], 0, 0)
    delta = datetime.timedelta(days=1)
    numberOfLeaveTaken = 0
    while (startDate <= endDate):
        newLeave = dict()
        newLeave['created_by'] = username
        newLeave['updated_by'] = username
        newLeave['username'] = username
        newLeave['leave_type'] = leave_type
        newLeave['leave_date'] = startDate
        newLeave['approver'] = approver
        newLeave['attachment'] = attachment
        newLeave['remark'] = remark
        if numberOfLeaveTaken == 0:
            if len(fromTime) > 0:
                newLeave['leave_date_time'] = fromTime
                numberOfLeaveTaken -= 0.5
        if startDate == endDate: 
            if len(toTime) > 0:
                newLeave['leave_date_time'] = toTime
                numberOfLeaveTaken -= 0.5
        startDate += delta
        numberOfLeaveTaken += 1
        newLeaveRecord = Leave()
        newLeaveRecord.saveNew(newLeave)
    leaveSummary = LeaveSummary.objects.filter(username=username, is_deleted=0, leave_type=leave_type).first()
    leaveSummary.leave_balance -= numberOfLeaveTaken
    leaveSummary.save()
    return urlResponse({'message': 'Data successfully addded!'}, 200, authorization)