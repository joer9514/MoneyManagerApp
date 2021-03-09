# from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.


def my_user(request):
    return render(request, "user/index.html")
