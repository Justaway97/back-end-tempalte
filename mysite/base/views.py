# TODO:
# currently set all user update and create as songming first, will implement from header next time

import json
from django.http import HttpResponse, JsonResponse
from base.models import TestModel, TestCode, TestTable
from django.views.decorators.csrf import csrf_exempt

def index(request):
    testModel = TestModel.objects.all().first()
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    authorization = verifyAndGenNewToken(genNewToken('songming', 'admin'))
    if authorization == '':
        return JsonResponse({'error': 'Token expired!. Please login again!'}, status=410)
    testModel = TestModel.objects.all().first()
    return urlResponse({'data': TestModel.deserialize(testModel)}, 200, authorization)

def option(request):
    codeType = request.GET.get('code_type')
    testCode = TestCode.objects.filter(code_type=request.GET.get('code_type'), is_deleted = 0)
    if len(testCode) > 0:
        return JsonResponse({'data': [TestCode.deserialize(tc) for tc in testCode]}, status=200)
    return JsonResponse({ 'error':'No Code with Code Type = ' + codeType}, status=500)

@csrf_exempt
def homeUpdate(request):
    updatedTestModel = json.loads(request.body)
    testModel = TestModel.objects.filter(pk=updatedTestModel['uuid'], is_deleted=0).first()
    testModel.update(updatedTestModel)
    return JsonResponse({'message': 'successfully updated record!'}, status=200)

def table(request):
    testTable = TestTable.objects.filter(is_deleted=0).order_by('created_at')
    return JsonResponse({'data': [TestTable.deserialize(tm) for tm in testTable]}, status=200)

@csrf_exempt
def tableUpdate(request):
    updatedTableModel = json.loads(request.body)
    data = updatedTableModel['data']
    for d in data:
        if 'uuid' in d: #update
            testTable = TestTable.objects.filter(pk=d['uuid'], is_deleted=0).first()
            testTable.update(d)
        else:
            d['created_by']='songming'
            d['updated_by']='songming'
            newRecord = TestTable()
            newRecord.saveNew(d)
    return JsonResponse({'message': 'successfully updated record!'}, status=200)

@csrf_exempt
def tableAdd(request):
    newTableModel = json.loads(request.body)
    newTableModel['created_by']='songming'
    newTableModel['updated_by']='songming'
    newRecord = TestTable()
    newRecord.saveNew(newTableModel)
    return JsonResponse({'message': 'successfully inserted record!'}, status=200)

@csrf_exempt
def tableDelete(request):
    ids = request.GET['id'].split(',')
    for i in ids:
        tableModel = TestTable.objects.get(uuid=i)
        tableModel.delete()
    return JsonResponse({'message': 'successfully deleted record!'}, status=200)


## real one start here

from django.shortcuts import render
from django.contrib.auth import authenticate
from base.models import BaseRole, BaseUser, BaseCode

from mysite.share.views import genNewToken, handleInput, urlResponse, verifyAndGenNewToken, sessionExpiredResponse, wrongParameterResponse

# Create your views here.
@csrf_exempt
def login(request):
    username, password = handleInput(request, ['username', 'password'], 'POST')
    if username is None or password is None:
        wrongParameterResponse()
    user = authenticate(username = username, password = password)
    if user is not None:
        leaveUser = BaseUser.objects.filter(username=username, is_deleted=0).first()
        if leaveUser:
            role = BaseRole.objects.filter(role_type = leaveUser.role_type, is_deleted=0).first()
            if role is not None:
                return urlResponse({}, 200, verifyAndGenNewToken(genNewToken(username, role.role)))
    sessionExpiredResponse()

def getCode(request):
    authorization = verifyAndGenNewToken(request.headers['Authorization'])
    if authorization == '':
        return sessionExpiredResponse()
    app = handleInput(request, ['app'], 'GET')
    if app is None:
        wrongParameterResponse()
    code = BaseCode.objects.filter(app=app)
    return urlResponse({'data': [BaseCode.deserialize(c) for c in code]}, status=200)
