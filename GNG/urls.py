from django.urls import path
from GNG_app.views import hello  # Import your view function

urlpatterns = [
    path('hello/', hello, name='hello'),  # Map URL to view
]