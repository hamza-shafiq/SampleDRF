from django.urls import path
from .views import InfoView

app_name = 'finance'

urlpatterns = [
    path('', InfoView.as_view(), name='info'),
]
