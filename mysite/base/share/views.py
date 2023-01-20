
import datetime
from django.http import JsonResponse
import jwt


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

def urlResponse(data, status, authorization):
    response = JsonResponse(data,status=status)
    response['Authorization'] = authorization
    response['Access-Control-Expose-Headers'] = "Authorization, X-Custom"
    return response    
