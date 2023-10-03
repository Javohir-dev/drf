import json
from django.shortcuts import render
from django.http import JsonResponse
from pprint import pprint


def api_home(request, *args, **kwargs):
    pprint(request.GET)
    pprint(request.POST)
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        ...
    print(body)
    # body["headers"] = request.headers
    data["params"] = dict(request.GET)
    data["headers"] = dict(request.headers)
    data["content_type"] = request.content_type

    # return JsonResponse({"message": "Hi there, this is your Django API response :)"})
    return JsonResponse(data)
