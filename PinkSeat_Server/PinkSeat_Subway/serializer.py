from rest_framework import serializers, viewsets
from .models import SubSchedule
#from .crawling import subwayParsing

# 시간표정보
class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubSchedule
        fields = "__all__"

class SubwayViewSet(viewsets.ModelViewSet):
    queryset = SubSchedule.objects.all()
    serializer_class = ScheduleSerializer