from django.shortcuts import render
from django.http import HttpResponse

import json

def index(request):
    response = json.dumps([{'Message': 'Hello i am Tito'}])
    return HttpResponse(response, content_type='text/json')