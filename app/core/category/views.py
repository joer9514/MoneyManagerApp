# from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from core.category.models import Category
#This imports the method CreateView, ListView, UpdateView, and DeleteView
from django.views.generic import *
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
from django.forms import *

#Class to create the form for application login
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name_category': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Bus, Traveler, Car, etc',
                    'autocomplete': 'off',
                }
            ),
            'description_category': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Description ',
                    'autocomplete': 'off',
                }
            )
            # Close_dictionary
        }

"""
The class lists all objects in the Budget model 
(This is possible with the use and import of the ListView method.)
"""
class CategoryListView(ListView):
    #Model indication
    model = Category
    #This indicates in which templete the objects will be sent.
    template_name = 'category/category.html'
    """
    Decorator method that validates prevents access to the o
    ther application windows until you log in.
    """
    @method_decorator(login_required)
    #Inherits objects from the model
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

#Class to create the form with CreateView method (must import the method)
class CategoryCreateView(CreateView):
    model = Category
    #indicates in which form (class) are the objects that are needed for creation
    form_class = CategoryForm
    #The templete where it will be used for the registers that the user is going to enter.
    template_name = 'category/create.html'
    success_url = reverse_lazy('list_category')
    """
    Decorator method that validates prevents access to the o
    ther application windows until you log in.
    """
    @method_decorator(login_required)
    #Inherits objects from the model
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


"""
Class that updates and saves the records entered by the user or changes 
that were made and redirects it to the budget listing view.
(This is possible with the use and import of the UpdataView method.)
"""
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/update.html'
    success_url = reverse_lazy('list_category')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


"""
Class that deletes a record and redirects it to the budget list view.
(This is possible with the use and import of the DeleteView method).
"""
class CategoryDeleteView(DeleteView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/delete.html'
    success_url = reverse_lazy('list_category')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
