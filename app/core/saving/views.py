# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from core.saving.models import Saving
from django.views.generic import *
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
from django.forms import *

#Class to create the form for Saving
class SavingForm(ModelForm):
    class Meta:
        model = Saving
        fields = '__all__'
        widgets = {
            'month_saving': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Name',
                    'autocomplete': 'off',
                }
            ),
            'account_saving': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Surname',
                    'autocomplete': 'off',
                }
            ),
            'account_status': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email: test@gmail.com, test@hotmail.com',
                    'autocomplete': 'off',
                }
            ),
            'account_balance': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Password > 4 characters',
                    'autocomplete': 'off',
                }
            ),
            'id_movement_id': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Password > 4 characters',
                    'autocomplete': 'off',
                }
            ),
            'id_user_id': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Password > 4 characters',
                    'autocomplete': 'off',
                }
            )
            # Close_dictionary
        }

"""
The class lists all objects in the Budget model 
(This is possible with the use and import of the ListView method.)
"""
class SavingListView(ListView):
    #Model indication
    model = Saving
    #This indicates in which templete the objects will be sent.
    template_name = 'saving/saving.html'
    """
    Decorator method that validates prevents access to the o
    ther application windows until you log in.
    """
    @method_decorator(login_required)
    #Inherits objects from the model
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

#Class to create the form with CreateView method (must import the method)
class SavingCreateView(CreateView):
    model = Saving
    #indicates in which form (class) are the objects that are needed for creation
    form_class = SavingForm
    #The templete where it will be used for the registers that the user is going to enter.
    template_name = 'saving/create.html'
    success_url = reverse_lazy('list_saving')
     """
    Decorator method that validates prevents access to the o
    ther application windows until you log in.
    """
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

"""
Class that updates and saves the records entered by the user or changes 
that were made and redirects it to the budget listing view.
(This is possible with the use and import of the UpdataView method.)
"""
class SavingUpdateView(UpdateView):
    model = Saving
    form_class = SavingForm
    template_name = 'saving/update.html'
    success_url = reverse_lazy('list_saving')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

"""
Class that deletes a record and redirects it to the budget list view.
(This is possible with the use and import of the DeleteView method).
"""
class SavingDeleteView(DeleteView):
    model = Saving
    form_class = SavingForm
    template_name = 'saving/delete.html'
    success_url = reverse_lazy('list_saving')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
