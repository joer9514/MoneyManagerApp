# from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def home_page(request):
    """
    Render index page of our application
    """
    data = {
        'usuarios': 'test'
    }
    return render(request, "home_page/home.html", data)
