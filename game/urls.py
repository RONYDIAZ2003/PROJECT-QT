from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('characters/', views.character_list, name='character_list'),
    path('characters/<int:character_id>/', views.character_detail, name='character_detail'),
    path('add/', views.add_character, name='add_character'),
    path('search/', views.search_characters, name='search_characters'),
    path('send-email/', views.send_test_email, name='send_test_email'),  
]




