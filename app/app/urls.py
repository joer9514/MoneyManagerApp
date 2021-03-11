"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.user.views import *
from core.saving.views import *
from core.index_page.views import *
from core.home_page.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', register_user, name='signup'),
    path('login/', login_user, name='login'),
    path('', index_page, name='index'),
    path('home', home_page, name='home'),
    path('home/user/add', UserListView.as_view(), name='list_user'),
    path('home/user/create', UserCreateView.as_view(), name='add_user'),
    path('home/user/Update', UserUpdateView.as_view(), name='update_user'),
    path('home/user/delete', UserDeleteView.as_view(), name='delete_user'),
    path('home/saving/add', SavingListView.as_view(), name='list_saving'),
    path('home/saving/create', SavingCreateView.as_view(), name='create_saving'),
    path('home/saving/update', SavingUpdateView.as_view(), name='update_saving'),
    path('home/saving/delete', SavingDeleteView.as_view(), name='delete_saving'),
]
