from django.shortcuts import render

# Create your views here.
import requests, json
from django.views import View
from rest_framework.response import Response


class ResponseView(View):

    def post(self, request, *args, **kwargs):
        data = request.POST
        sender = data['sender']
        message = data['message']
        url = "http://localhost:5005/webhooks/rest/webhook"

        obj = {
            "sender": sender,
            "message": message, }
        x = requests.post(url, data=json.dumps(obj))
        _res = x.json()
        _res = _res[0]
        return Response(_res)
