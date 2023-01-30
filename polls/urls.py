from rest_framework import routers
from . import views
from django.urls import path

# router = routers.DefaultRouter()

# router.register('api/polls', views.PollsViewSet, 'polls')

# urlpatterns = router.urls

urlpatterns =  [
    path('', views.PollsViewSet.as_view(), name='polls_list'),
]