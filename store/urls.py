from django.urls import path, include
from store.views import base_view

urlpatterns = [
    path('', base_view, name='base' ),
]