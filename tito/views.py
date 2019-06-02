from django.shortcuts import render
from django.http import HttpResponse
from .message import Message
from datetime import datetime
from datetime import timedelta
from .models import Client
from .requester_server import RequesterServer
import traceback


import json
import time

HELP = '@tito help: muestra los comandos disponibles \n @tito info: muestra información del canal \n @tito mute <n>: desactiva respuestas por n segundos \n @tito me: muestra información del usuario que envia el mensaje.'
ERROR = 'Comando invalido'
ERROR_DEFAULT = 'Hubo un error, Tito esta triste :('
NO_ACTION = 'Tito no puede hacer eso'
OK_SLEEP = 'Tito ya no esta dormido'
OK = 'Tito Ok'


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
            response = json.dumps([{'Error': ERROR_DEFAULT }])
    return HttpResponse(response, content_type='text/json')


def action(json_action, message):
    if(json_action == 'help'):
        return help_action(message)
    elif(json_action == 'mute'):
        return mute(message)
    elif(json_action == 'me'):
        return me_action(message)
    elif(json_action == 'info'):
        return info_action(message)
    elif(json_action == 'welcome'):
        return welcome_action(message)
    else:
        return no_action_error()

def no_action_error():
    return json.dumps([{'Error': NO_ACTION }])

def help_action(message):
    requester = RequesterServer()
    requester.send_message(HELP,message.username,message.workspace, message.channel)

    return json.dumps([{'Message': OK}])

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

def me_action(message):
    requester = RequesterServer()
    user_data = requester.user_info(message.username)
    msg_nickname = "Usuario: " + user_data['nickname'] + "\n"
    msg_name = "Nombre: " + user_data['name'] + "\n"
    msg_email = "Email: " + user_data['email'] + "\n"
    msg = msg_nickname + msg_name + msg_email
    requester.send_message(msg,message.username,message.workspace,message.channel)
    return json.dumps([{'Message': OK}])

def info_action(message):
    requester = RequesterServer()
    channel_data = requester.channel_info(message.workspace, message.channel)
    msg_name = "Canal: " + channel_data['name'] + "\n"
    msg_des = "Descripcion: " + channel_data['description'] + "\n"
    msg_welcome = "Welcome:" + channel_data['welcomeMessage'] + "\n"
    msg_creator = "Creador: " + channel_data['creator']['email'] + "\n"
    msg = msg_name + msg_des + msg_welcome + msg_creator
    requester.send_message(msg,message.username,message.workspace,message.channel)
    return json.dumps([{'Message': OK}])

def welcome_action(message):
    requester = RequesterServer()
    channel_data = requester.channel_info(message.workspace, message.channel)
    msg_welcome = channel_data['welcomeMessage']
    requester.send_message(msg_welcome,message.username,message.workspace,message.channel)
    return json.dumps([{'Message': OK}])





