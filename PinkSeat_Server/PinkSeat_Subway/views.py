from django.shortcuts import render, redirect
#from django.response import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from PinkSeat_Subway.serializer import ScheduleSerializer
from PinkSeat_Subway.models import SubSchedule
import socket
from rest_framework.views import APIView
#from .crawling import subwayParsing
from . import models
from rest_framework import serializers

# Create your views here.
class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = SubSchedule.objects.all()
    serializer_class = ScheduleSerializer