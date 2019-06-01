import requests
import json

class RequesterServer:
    #BASIC_URL= "https://hypechat-t2.herokuapp.com"
    BASIC_URL= "https://app-server-t2.herokuapp.com"
    USERS_URL= "/api/users"
    MESSAGE_URL = "/api/messages"
    TOKEN = ""
    TYPE_TEXT = "2"

    def user_info(self,username):
        url = BASIC_URL + USERS_URL + "/" + username
        response = requests.get( url, headers={'x-auth-token': TOKEN})
        json_response = response.json()

    def send_message(self, message, username, workspace, channel):
        url = BASIC_URL + MESSAGE_URL + "/workspace/" + workspace + "/channel/" + channel
        response = requests.post(url,data={'creator':'value', 'text':message, 'type': TYPE_TEXT}, headers={'x-auth-token': TOKEN})

        response.raise_for_status()

