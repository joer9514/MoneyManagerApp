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

##inputs needed to implement the urls paths for each templet
from django.contrib import admin
from django.urls import path
from core.user.views import *
from core.saving.views import *
from core.category.views import *
from core.budget.views import *
from core.movement.views import *
from core.index_page.views import *
from core.home_page.views import *


#Here we add the views of the templets,
urlpatterns = [
#The syntax of the views is as follows:
#path(name of  rute/, name of funtcion of class, name for use within templates)
#We use function-based classes to transform them into a view with the as_view() method. 
    path('admin/', admin.site.urls),
    path('signup/', RegisterCreateUser.as_view(), name='signup'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', index_page, name='index'),
    path('home/', HomeListView.as_view(), name='home'),
    path('home/user/add/', UserListView.as_view(), name='list_user'),
    path('home/user/create/', UserCreateView.as_view(), name='add_user'),
    path('home/user/update<int:pk>/', UserUpdateView.as_view(), name='update_user'),
    path('home/user/delete<int:pk>/', UserDeleteView.as_view(), name='delete_user'),

    path('home/saving/add/', SavingListView.as_view(), name='list_saving'),
    path('home/saving/create/', SavingCreateView.as_view(), name='create_saving'),
    path('home/saving/update<int:pk>/', SavingUpdateView.as_view(), name='update_saving'),
    path('home/saving/delete<int:pk>/', SavingDeleteView.as_view(), name='delete_saving'),

    path('home/category/add/', CategoryListView.as_view(), name='list_category'),
    path('home/category/create/', CategoryCreateView.as_view(), name='create_category'),
    path('home/category/update<int:pk>/', CategoryUpdateView.as_view(), name='update_category'),
    path('home/category/delete<int:pk>/', CategoryDeleteView.as_view(), name='delete_category'),

    path('home/budget/add/', BudgetListView.as_view(), name='list_budget'),
    path('home/budget/create/', BudgetCreateView.as_view(), name='create_budget'),
    path('home/budget/update<int:pk>/', BudgetUpdateView.as_view(), name='update_budget'),
    path('home/budget/delete<int:pk>/', BudgetDeleteView.as_view(), name='delete_budget'),

    path('home/movement/add/', MovementListView.as_view(), name='list_movement'),
    path('home/movement/create/', MovementCreateView.as_view(), name='create_movement'),
    path('home/movement/update<int:pk>/', MovementUpdateView.as_view(), name='update_movement'),
    path('home/movement/delete<int:pk>/', MovementDeleteView.as_view(), name='delete_movement'),
]
