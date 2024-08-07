from django.shortcuts import render
from django import http
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.


def testtodoapp(web_http_request):
    return render(web_http_request, "vtodoapp/testtodoapp.html")