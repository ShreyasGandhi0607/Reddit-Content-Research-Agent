import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def snapshot_webhook_handler(request):
    # webhook -> POST request
    # Django does not allow post request without csrf token
    if request.method != "POST":
        return HttpResponse("OK") # prevent it from hacker use okay instead of POST required
    
    auth = request.headers.get("Authorization")
    if auth.startswith("Basic "):
        token = auth.split(" ")[1]
        if token == "abc123":
            data = {}
            try:
                data = json.loads(request.body.decode("utf-8"))
            except:
                pass
            print(data)
    return HttpResponse("Okay")