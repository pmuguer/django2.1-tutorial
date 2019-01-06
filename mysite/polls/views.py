from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World of Django! You are on the polls index")
