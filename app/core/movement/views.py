# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from core.movement.models import Movement
from django.views.generic import *
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
from django.forms import *

#Class to create the form for Movement
class MovementForm(ModelForm):
    class Meta:
        model = Movement
        fields = '__all__'
        widgets = {
            'name_user': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Name',
                    'autocomplete': 'off',
                }
            ),
            'surname_user': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Surname',
                    'autocomplete': 'off',
                }
            ),
            'email_user': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email: test@gmail.com, test@hotmail.com',
                    'autocomplete': 'off',
                }
            ),
            'password_user': TextInput(
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
class MovementListView(ListView):
    #Model indication
    model = Movement
    #This indicates in which templete the objects will be sent.
    template_name = 'movement/movement.html'
    """
    Decorator method that validates prevents access to the o
    ther application windows until you log in.
    """
    @method_decorator(login_required)
    #Inherits objects from the model
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

#Class to create the form with CreateView method (must import the method)
class MovementCreateView(CreateView):
    model = Movement
    #indicates in which form (class) are the objects that are needed for creation
    form_class = MovementForm
    #The templete where it will be used for the registers that the user is going to enter.
    template_name = 'movement/create.html'
    success_url = reverse_lazy('list_movement')
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
class MovementUpdateView(UpdateView):
    model = Movement
    form_class = MovementForm
    template_name = 'movement/update.html'
    success_url = reverse_lazy('list_movement')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

"""
Class that deletes a record and redirects it to the budget list view.
(This is possible with the use and import of the DeleteView method).
"""
class MovementDeleteView(DeleteView):
    model = Movement
    form_class = MovementForm
    template_name = 'movement/delete.html'
    success_url = reverse_lazy('list_movement')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
