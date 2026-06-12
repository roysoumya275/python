from django.urls import path
from . import views

urlpatterns = [
    path('', views.card_list, name='card_list'),
    path('add/', views.add_card, name='add_card'),
     path('edit/<int:id>/', views.edit_card, name='edit_card'),
    path('delete/<int:id>/', views.delete_card, name='delete_card'),
    path('search/', views.search_view, name='search'),
]