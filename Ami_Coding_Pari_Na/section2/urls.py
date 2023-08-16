
from django.urls import path
from .views import khojView

app_name='section2'

urlpatterns = [
    path('',  khojView, name='khoj'),
]
