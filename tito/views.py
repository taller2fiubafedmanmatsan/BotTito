from django.shortcuts import render
from django.http import HttpResponse

import json
import time

HELP = '@tito help: muestra los comandos disponibles \\n @tito info: muestra información del canal \\n @tito mute <n>: desactiva respuestas por n segundos \\n @tito me: muestra información del usuario que envia el mensaje.'
ERROR = 'Comando invalido'
OK_SLEEP = 'Tito ya no esta dormido'

def index(request):
    response = json.dumps([{'Message': 'Hello i am Tito'}])
    return HttpResponse(response, content_type='text/json')

def help(request):
    if request.method == 'GET':
        try:
            response = json.dumps([{'Message': HELP }])
        except:
            response = json.dumps([{'Error': ERROR }])
    return HttpResponse(response, content_type='text/json')

def mute(request,time_mute):
    if request.method == 'GET':
        try:
            time.sleep(time_mute)
            response = json.dumps([{'Message': OK_SLEEP }])
        except:
            response = json.dumps([{'Error': ERROR }])
    return HttpResponse(response, content_type='text/json')




