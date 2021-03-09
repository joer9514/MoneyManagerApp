# from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.


def my_user(request):
    data = {
        'message': 'Estoy desde la vista usuario'
    }
    return render(request, 'index.html', data)
