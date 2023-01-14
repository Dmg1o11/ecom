from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from .views import Signup
from .views import Login,logout
from .models import Category,Customer,Products

urlpatterns = [
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('Get_user', Login.as_view(), name='Get User'),
    path('Get_user_product', Products, name='Get User products'),
    path('Get_user_Business', Customer, name='Get User Business'),
    path('Get_countries', Customer, name='Get countries'),
    path('Get_States', Customer, name='Get States'),
    path('Get_cities', Customer, name='Get Cities'),
    path('Get_categories', Category, name='Get categories'),
    path('Get_Brands', Customer, name='Get Brannds'),
    path('Add_product', Products, name='Add product'),
    path('Update_product', Products, name='Update product'),
    path('Delete product', Products, name='Delete product'),
    path('Get_Business_products',Products , name='Get Business Products'),
    
]