# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from core.saving.views import *
from core.budget.views import *
from django.views.generic import *


class HomeListView(TemplateView):
    template_name = 'home_page/home.html'

    def get_context_data(self, *args, **kwargs):
        budget = Budget.objects.all()
        saving = Saving.objects.all()
        return {'budgets': budget, 'savings': saving}

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
