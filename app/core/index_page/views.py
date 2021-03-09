# from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def index_page(request):
    """
    Render index page of our application
    """
    return render(request, "index_page/base_principal.html")
