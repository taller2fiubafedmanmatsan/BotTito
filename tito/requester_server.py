import requests
import json
import logging
import http.client


class RequesterServer:
    #BASIC_URL= "https://hypechat-t2.herokuapp.com"
    BASIC_URL= "https://app-server-t2.herokuapp.com"
    USERS_URL= "/api/users"
    CHANNEL_URL = "/api/channels/"
    MESSAGE_URL = "/api/messages"
    TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1Y2Y3MDFkMzU3NGYyZDAwMDQxZGZiYWEiLCJpYXQiOjE1NTk2OTE3MzEsImV4cCI6MTU1OTc3ODEzMX0.WfVFAoqhn-aqhCWtbzxic6Vq1RM-9hF-BaExKcId9dY"
    TYPE_TEXT = "2"

    def __init__(self):
        # Debug logging
        http.client.HTTPConnection.debuglevel = 1
        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)
        req_log = logging.getLogger('requests.packages.urllib3')
        req_log.setLevel(logging.DEBUG)
        req_log.propagate = True


    def user_info(self,username):
        url = self.BASIC_URL + self.USERS_URL + "/" + username
        response = requests.get( url, headers={'x-auth-token': self.TOKEN})
        json_response = response.json()

        response.raise_for_status()

        return json_response

    def send_message(self,message,username, workspace, channel):
        url = self.BASIC_URL + self.MESSAGE_URL + "/workspace/" + workspace + "/channel/" + channel
        payload={'creator': username,'text':message, 'type': self.TYPE_TEXT}
        response = requests.post(url,json=payload, headers={'x-auth-token': self.TOKEN})

        response.raise_for_status()

    def channel_info(self,workspace, channel):
        url = self.BASIC_URL + self.CHANNEL_URL + channel + "/workspace/" + workspace
        response = requests.get( url, headers={'x-auth-token': self.TOKEN})
        json_response = response.json()
        response.raise_for_status()

        return json_response


