import datetime
import pytz
from django.db.models import Q
from django.utils import timezone
from rest_framework import serializers, viewsets
from .models import Subway, Seat_info
#from .crawling import subwayParsing



# 좌석정보
class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat_info
        fields = "__all__"


class SubwaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subway
        fields = "__all__"

class SubwayViewSet(viewsets.ModelViewSet):
    queryset = Subway.objects.all()
    serializer_class = SubwaySerializer





'''
# Seat 데이터가 주어지면 JSON 데이터로 변환
class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat_info
        fields = "__all__"
        
        # 좌석 존재, 이용시간대 중복 체크
        if Seat_info.objects.filter(id=self.context['view'].kwargs.get('seat_pk')).exists():
            seat = Seat_info.objects.get(id=self.context['view'].kwargs.get('seat_pk'))
            if seat.time_tables.filter(Q(date_time_start__lte=date_time_start) & Q(date_time_end__gte=date_time_end) |
                                      Q(date_time_end__range=(date_time_start, date_time_end)) |
                                      Q(date_time_start__range=(date_time_start, date_time_end))).exists():
                raise serializers.ValidationError('이 좌석은 현재 사용 불가능합니다.')
        else:
            raise serializers.ValidationError('해당 좌석이 존재하지 않습니다.')

    
class ReservationHistorySerializer(ModelSerializer):
    date_time_start = serializers.DateTimeField(read_only=True, default_timezone=KST)
    date_time_end = serializers.DateTimeField(read_only=True, default_timezone=KST)

    class Meta:
        model = Seat_info
        fields = "__all__"

    created_at = models.DateTimeField(auto_now_add=True, help_text='TimeStamp')
    updated_at = models.DateTimeField(auto_now=True)
    '''