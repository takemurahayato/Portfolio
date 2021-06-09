from django.http import HttpResponse

def index(requet):
    return HttpResponse("Hello instagram")
