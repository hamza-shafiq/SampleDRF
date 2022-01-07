from django.urls import path
from .views import InfoView, PythonView, DjangoView

app_name = 'finance'

urlpatterns = [
    path('', InfoView.as_view(), name='info'),
    path('python-questions', PythonView.as_view(), name='python-questions'),
    path('django-questions', DjangoView.as_view(), name='django-questions'),
]
