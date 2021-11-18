from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url
from PinkSeat_Subway.views import ScheduleViewSet
from . import views
#from PinkSeat_seat.views import HelloAPI

router = routers.DefaultRouter()
router.register('schedule', ScheduleViewSet)

urlpatterns = [
    #path("hello/", HelloAPI),
    path('', include(router.urls)),
    #path('', views.SeatDeatil.as_view()),
]