from django.urls import path
from .views import *

urlpatterns = [
    path('getdata/', getData, name='getdata'),
    path('get-user/<int:user_id>/', get_user_by_id, name='get_user_by_id'),
    path('signup/', SignUp, name='signup'),
    path('login/', login, name='login'),
    path('logout/',Logout,name='logout'),
    path('is-admin-connected/', is_admin_connected, name='is_admin_connected'),
     path('is-user-connected/', is_user_connected, name='is_user_connected'),
]