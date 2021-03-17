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


class SavingListView(ListView):
    model = Saving
    template_name = 'saving/saving.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class SavingCreateView(CreateView):
    model = Saving
    form_class = SavingForm
    template_name = 'saving/create.html'
    success_url = reverse_lazy('list_saving')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class SavingUpdateView(UpdateView):
    model = Saving
    form_class = SavingForm
    template_name = 'saving/update.html'
    success_url = reverse_lazy('list_saving')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class SavingDeleteView(DeleteView):
    model = Saving
    form_class = SavingForm
    template_name = 'saving/delete.html'
    success_url = reverse_lazy('list_saving')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
