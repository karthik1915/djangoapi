from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {"title": "Home"}
    return render(request, "main_index.html", context)
