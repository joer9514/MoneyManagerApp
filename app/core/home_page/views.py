# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

#imports of model classes and functions
from core.saving.views import *
from core.budget.views import *
from core.movement.views import *
from django.views.generic import *

#Class that takes the template
class HomeListView(TemplateView):
    template_name = 'home_page/home.html'
    """
    function that obtains the objects from the 
    models and stores them in a dictionary
    """
    def get_context_data(self, *args, **kwargs):
        budget = Budget.objects.all()
        saving = Saving.objects.all()
        movement = Movement.objects.all()
        return {'budgets': budget, 'savings': saving, 'movements': movement}

    """
    Decorator method that validates prevents access to the o
    ther application windows until you log in.
    """
    @method_decorator(login_required)
    #Inherits objects from the model
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
