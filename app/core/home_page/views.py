# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render
from core.saving.views import *
from core.budget.views import *
from django.views.generic import *


class HomeListView(ListView):
    model = Budget
    template_name = 'home_page/home.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
