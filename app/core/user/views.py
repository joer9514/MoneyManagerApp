# from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from core.user.models import User
from django.views.generic import *
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
from django.forms import *


class UserForm(ModelForm):
    class Meta:
        model = User
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


class RegisterCreateUser(CreateView):
    model = User
    form_class = UserForm
    template_name = 'user/signup.html'
    success_url = reverse_lazy('login')


def login_user(request):
    return render(request, "user/login.html")


class UserListView(ListView):
    model = User
    template_name = 'user/user.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'user/create.html'
    success_url = reverse_lazy('list_user')


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'user/update.html'
    success_url = reverse_lazy('list_user')


class UserDeleteView(DeleteView):
    model = User
    form_class = UserForm
    template_name = 'user/delete.html'
    success_url = reverse_lazy('list_user')
