
from django.urls import path
from .views import valueApiView

app_name='section3'

urlpatterns = [
    path('<start_datetime>/<end_datetime>/<user_id>',  valueApiView, name='api'),
    
]
