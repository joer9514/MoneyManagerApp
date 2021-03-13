# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render
from django.urls import reverse_lazy
from core.budget.models import Budget
from django.views.generic import *
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
from django.forms import *


class BudgetForm(ModelForm):
    class Meta:
        model = Budget
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


class BudgetListView(ListView):
    model = Budget
    template_name = 'budget/budget.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class BudgetCreateView(CreateView):
    model = Budget
    form_class = BudgetForm
    template_name = 'budget/create.html'
    success_url = reverse_lazy('list_budget')


class BudgetUpdateView(UpdateView):
    model = Budget
    form_class = BudgetForm
    template_name = 'budget/update.html'
    success_url = reverse_lazy('list_budget')


class BudgetDeleteView(DeleteView):
    model = Budget
    form_class = BudgetForm
    template_name = 'budget/delete.html'
    success_url = reverse_lazy('list_budget')
