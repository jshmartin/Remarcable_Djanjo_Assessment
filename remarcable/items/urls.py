from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.items, name='items'),
    path('items/details/<int:id>', views.details, name='details'),
]
