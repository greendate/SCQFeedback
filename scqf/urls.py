from django.urls import path
from . import views


urlpatterns = [
    path('', views.clubs_list, name='clubs_list'),
    path('club/<int:identify>/', views.club, name='club'),
]
