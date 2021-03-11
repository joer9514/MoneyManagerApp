# from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from core.user.models import User
from django.views.generic import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


def register_user(request):
    return render(request, "user/signup.html")


def login_user(request):
    return render(request, "user/login.html")


class UserListView(ListView):
    model = User
    template_name = 'user/user.html'

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class UserCreateView(CreateView):
    pass


class UserUpdateView(UpdateView):
    pass


class UserDeleteView(DeleteView):
    pass
