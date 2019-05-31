from django.shortcuts import render
from django.http import HttpResponse
from .message import Message
from datetime import datetime
from datetime import timedelta
from .models import Client
import traceback


import json
import time

HELP = '@tito help: muestra los comandos disponibles \\n @tito info: muestra información del canal \\n @tito mute <n>: desactiva respuestas por n segundos \\n @tito me: muestra información del usuario que envia el mensaje.'
ERROR = 'Comando invalido'
NO_ACTION = 'Tito no puede hacer eso'
OK_SLEEP = 'Tito ya no esta dormido'

def index(request):
    response = json.dumps([{'Message': 'Hello i am Tito'}])
    return HttpResponse(response, content_type='text/json')



def work(request):
    if request.method == 'POST':
        try:
            message = Message(request)
            if not is_mute(message):
                response = action(message.action,message)
            else:
                response = json.dumps([{'Respuesta': "Tito esta muteado"}])
        except:
            traceback.print_exc()
            response = json.dumps([{'Error': ERROR }])
    return HttpResponse(response, content_type='text/json')


def action(json_action, message):
    if(json_action == 'help'):
        return help_action()
    elif(json_action == 'mute'):
        return mute(message)
    elif(json_action == 'me'):
        3
    elif(json_action == 'info'):
        4
    else:
        return no_action_error()

def no_action_error():
    return json.dumps([{'Error': NO_ACTION }])

def help_action():
    return json.dumps([{'Message': HELP }])

def mute(message):
    secs = int(message.argument())
    time = datetime.now() + timedelta(seconds=secs)
    client = Client(name=message.client(), mute_time=time)
    client.save()
    return json.dumps([{'Message': client.name}])

def is_mute(message):
    try:
        client = Client.objects.get(name=message.client())
        if(client.mute_time > datetime.now()):
            return True
        else:
            return False
    except Client.DoesNotExist:
        return False


