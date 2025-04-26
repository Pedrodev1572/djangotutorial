from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá, este é o app de enquetes!")