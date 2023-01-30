
import datetime
import json
from django.http import JsonResponse
import jwt

def getUsername(token):
    return jwt.decode(token, key='backendtemplate', algorithms="HS256")['username']

def verifyAndGenNewToken(oldToken):
    try:
        decoded_data = jwt.decode(oldToken, key='backendtemplate', algorithms="HS256")
        if datetime.datetime.now() - datetime.timedelta(minutes=10) > \
            datetime.datetime.strptime(decoded_data['timestamp'], '%Y-%m-%d %H:%M:%S.%f'):
            return ''
        decoded_data['timestamp'] = str(datetime.datetime.now())
        return jwt.encode(payload=decoded_data, key='backendtemplate', algorithm="HS256")
    except:
        print('JWT token error')
        return ''
    
def genNewToken(username, role):
    return jwt.encode(payload={"username": username, "role": role, 'timestamp':str(datetime.datetime.now())},
                               key='backendtemplate',
                               algorithm="HS256")

def urlResponse(data, status, authorization=None):
    response = JsonResponse(data,status=status)
    if authorization:
        response['Authorization'] = authorization
        response['Access-Control-Expose-Headers'] = "Authorization, X-Custom"
    return response    

def isUserAuthorize(request):
    return verifyAndGenNewToken(request.headers['Authorization'])

def sessionExpiredResponse():
    return urlResponse({'error': 'Session Expired! Please Login Again!'}, 401)

def wrongParameterResponse():
    return urlResponse({'error': 'Invalid Argument!'}, 422)

def handleInput(request, params, method):
    fields = []
    if method == 'POST':
        body = json.loads(request.body)
        for param in params:
            fields.append(body[param])
    if method == 'GET':
        for param in params:
            fields.append(request.GET[param])
    if len(fields) > 1:
        return tuple(fields)
    return fields[0]