
from django.urls import path
from .views import UserLoginView , UserSignUpView 

app_name='section1'

urlpatterns = [
    path('signin', UserLoginView.as_view(), name='signin'),
    path('signup', UserSignUpView.as_view(), name='signup'),
]
