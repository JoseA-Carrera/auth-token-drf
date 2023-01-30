from rest_framework import routers
from . import views
from django.urls import path


urlpatterns =  [
    path('poll/', views.PollsViewSet.as_view(), name='poll-list'),
    path('poll/<int:pk>/delete/', views.PollDeleteView.as_view(), name='poll-delete'),
    path('poll/<int:pk>/update/', views.PollUpdateView.as_view(), name='poll-update'),
    path('poll/<int:pk>/', views.PollDetailView.as_view(), name='poll-detail')

]