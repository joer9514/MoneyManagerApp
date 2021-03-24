# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render
from django.urls import reverse_lazy
from core.budget.models import Budget
#This imports the method CreateView, ListView, UpdateView, and DeleteView
from django.views.generic import *
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
from django.forms import *

#Class to create the registration form used in Signup.html
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
"""
The class lists all objects in the Budget model 
(This is possible with the use and import of the ListView method.)
"""
class BudgetListView(ListView):
    #Model indication
    model = Budget
    #This indicates in which templete the objects will be sent.
    template_name = 'budget/budget.html'

    #Inherits objects from the model
    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

#Class to create the form with CreateView method (must import the method)
class BudgetCreateView(CreateView):
    model = Budget
    #indicates in which form (class) are the objects that are needed for creation
    form_class = BudgetForm
    #The templete where it will be used for the registers that the user is going to enter.
    template_name = 'budget/create.html'
    #With reverze_lazy once the data is validated I redirect you to the page that has been specified. 
    success_url = reverse_lazy('list_budget')

"""
Class that updates and saves the records entered by the user or changes 
that were made and redirects it to the budget listing view.
(This is possible with the use and import of the UpdataView method.)
"""
class BudgetUpdateView(UpdateView):
    model = Budget
    form_class = BudgetForm
    template_name = 'budget/update.html'
    success_url = reverse_lazy('list_budget')

"""
Class that deletes a record and redirects it to the budget list view.
(This is possible with the use and import of the DeleteView method).
"""
class BudgetDeleteView(DeleteView):
    model = Budget
    form_class = BudgetForm
    template_name = 'budget/delete.html'
    success_url = reverse_lazy('list_budget')
