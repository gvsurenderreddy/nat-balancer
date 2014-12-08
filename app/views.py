import json

from django.http import HttpResponse

def index(request):
    response = {}
    return HttpResponse(json.dumps(response), content_type="application/json")
