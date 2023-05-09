from django.http import HttpResponse

# Create your views here.

# Nova view, leva para algum rota
def index(request):
    return HttpResponse("Olá mundo")

def sobre(request):
    return HttpResponse("Esse é um app de enquete")