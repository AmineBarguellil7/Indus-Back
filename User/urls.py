from django.urls import path
from .views import *

urlpatterns = [
    path('getdata/', getData, name='getdata'),
    path('signup/', SignUp, name='signup'),
    path('login/', login, name='login'),
    path('logout/',Logout,name='logout'),
    path('is-admin-connected/', is_admin_connected, name='is_admin_connected'),
]