from django.urls import path
from django.urls.conf import include
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('add/',add_post,name='add_post'),
    path('fields/',field,name='field'),
    path('login/',login_user,name='login'),
    path('logout/', logoutUser, name="logout"),
    path('list/',all_list,name='all_list'),
    path('search/',search, name='search'),
    path('search_list/',search_list, name='slist'),
    path('delete/<id>/', delete_post, name="delete")
]