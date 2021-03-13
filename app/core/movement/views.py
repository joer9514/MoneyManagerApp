# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render
from django.urls import reverse_lazy
from core.movement.models import Movement
from django.views.generic import *
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
from django.forms import *


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


class MovementListView(ListView):
    model = Movement
    template_name = 'movement/movement.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class MovementCreateView(CreateView):
    model = Movement
    form_class = MovementForm
    template_name = 'movement/create.html'
    success_url = reverse_lazy('list_movement')


class MovementUpdateView(UpdateView):
    model = Movement
    form_class = MovementForm
    template_name = 'movement/update.html'
    success_url = reverse_lazy('list_movement')


class MovementDeleteView(DeleteView):
    model = Movement
    form_class = MovementForm
    template_name = 'movement/delete.html'
    success_url = reverse_lazy('list_movement')
