from django.shortcuts import render
from django import http
# Create your views here.

def index(web_http_request):
    # return http.HttpResponse("Welcome to the Main Page of VinXD")
    return render(web_http_request, "Main_Page/Main.html")