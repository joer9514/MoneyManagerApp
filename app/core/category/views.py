# from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from core.category.models import Category
from django.views.generic import *
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
from django.forms import *


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


class CategoryListView(ListView):
    model = Category
    template_name = 'category/category.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('list_category')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/update.html'
    success_url = reverse_lazy('list_category')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class CategoryDeleteView(DeleteView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/delete.html'
    success_url = reverse_lazy('list_category')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
