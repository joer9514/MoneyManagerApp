# from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def register_user(request):
    """

    """
    return render(request, "user/signup.html")


def login_user(request):
    """

    """
    return render(request, "user/login.html")
