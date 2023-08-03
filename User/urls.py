from django.urls import path
from .views import getData, SignUp

urlpatterns = [
    path('getdata/', getData, name='getdata'),
    path('signup/', SignUp, name='signup'),
    # path('login/', login, name='login'),
]