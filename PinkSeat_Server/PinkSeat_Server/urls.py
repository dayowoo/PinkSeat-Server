from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url
from rest_framework import routers

import PinkSeat_seat.serializer

from PinkSeat_account import views
import PinkSeat_seat.serializer

app_name = 'PinkSeat_seat'

router = routers.DefaultRouter()
router.register('PinkSeat_seat', PinkSeat_seat.serializer.SubwayViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('PinkSeat_seat/', include('PinkSeat_seat.urls')),
    path('PinkSeat_Subway/', include('PinkSeat_Subway.urls')),
    url('api/v1/', include((router.urls, 'PinkSeat_seat'), namespace='api')),
    path("PinkSeat_account/", include("PinkSeat_account.urls")),
    path("PinkSeat_account/auth", include("knox.urls")),
]
