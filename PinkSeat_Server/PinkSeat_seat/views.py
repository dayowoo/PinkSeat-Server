from django.shortcuts import render, redirect
#from django.response import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from PinkSeat_seat.serializer import SubwaySerializer, SeatSerializer
from PinkSeat_seat.models import Subway, Seat_info
import socket
from rest_framework.views import APIView
#from .crawling import subwayParsing
from . import models
from rest_framework import serializers


@api_view(['GET', 'POST'])
def subway_info(request):
    if request.method == 'GET':
        subway = Subway.objects.all()
        serializer = SubwaySerializer(subway, many=True)
        return Response(serializer.data)


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat_info.objects.all()
    serializer_class = SeatSerializer



#양보요청 울리기 - 부저 작동 함수 ( App Btn Down )
# class AlarmViewSet(viewsets.ModelViewSet):     
#     queryset = Seat_info.objects.all()
#     serializer_class = SeatSerializer









'''
#아두이노
import serial
import time
import json


@api_view(["GET"])
def HelloAPI(request):
    return Response("hello world!")

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat_info.objects.all()
    serializer_class = SeatSerializer

def seatP(request, number):
        ser = serial.Serial(
                        port='COM4',
                        baudrate=115200,
                )
        
        print('아두이노와 통신 시작')
        print('아두이노의 접속 포트는 COM4 입니다.\n')

        number = number
        while True:
                if ser.readable():
                        res = ser.readline()
                        json_data = json.loads(res.decode()[:-1])  ##json_data -> json으로 파싱된 데이터를 dict형태로 바뀌서 저장
                        print(json_data)
                        return render(request, 'NawamMa/seatP.html', {'json_data': json_data, 'number':number})
        # # if(val <= 0 )
                else:
                        print("연결을 실패했습니다.")
                        return HttpResponse("실패")

# 임산부가 요청보낼 시 아두이노 불과 소리 나오게하는 url
def preRequset(request):
        ser = serial.Serial(
                port='COM4',
                baudrate=115200,
        )

        print('아두이노와 통신 시작')
        print('아두이노의 접속 포트는 COM4 입니다.\n')

        while True:
                c = 'p'
                c = c.encode()
                ser.write(c)
                print(c)

                if ser.readable():
                        stop = ser.readline()
                        stopA = stop.decode()
                        stopB = stopA.strip()
                        print(stopB)
                        if stopB == 'T':
                                return redirect('/')

'''

'''
PrettyPrint : 복잡한 자료구조 더 알기 쉽게
from pprint import pprint

arduino = serial.Serial('com4',115200)
time.sleep(1)

print("'1'을 입력하면 LED ON & '0'을 입력하면 LED OFF")

while 1:s
    var = input()

    if(var == '1'):
        var = var.encode('utf-8')
        arduino.write(var)
        print("LED turned ON")
        time.sleep(1)

    if(var == '0'):
        var = var.encode('utf-8')
        arduino.write(var)
        print("LED turned OFF")
        time.sleep(1)


       

# 임산부 양보요청 아두이노 통신
def preRequset(request):
        ser = serial.Serial(
                port='COM4',
                baudrate=115200,
        )

        print('아두이노와 통신 시작')
        print('아두이노의 접속 포트는 COM4 입니다.\n')

        while True:
                c = 'p'
                c = c.encode()
                ser.write(c)
                print(c)

                if ser.readable():
                        stop = ser.readline()
                        stopA = stop.decode()
                        stopB = stopA.strip()
                        print(stopB)
                        if stopB == 'T':
                                return redirect('/')

'''













'''
from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
# from rest_framework.decorators import api_view, login_required

from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import GenericViewSet

# from .models import .
# from .serializers import SeatSerializer
'''

'''
# 좌석 선택
@login_required
def seatSelect(request, user_id, subway_id):
    seats = Seat.objects.filter(subway_id = subway_id)
    return render(request, 'seatSelect.html', {'user_id': user_id, 'seats': seats, 'bus_id': bus_id, 'start_id': start_id})

# 좌석 선택시 예약 번호 생성
@login_required
def confirm(request, user_id, bus_id, start_id, seat_id):
    seat_instance = Seat.objects.get(seatid=seat_id)
    seat_instance.status = True
    seat_instance.save()

    reservation_id = "{}-{}-{}".format(user_id, bus_id, seat_id)

    try:
        reservation_instance = Reservation.objects.create(
            reservationid = reservation_id,
            username = User.objects.get(username=user_id),
            subway_id = Bus.objects.get(subway_id=subway_id),
            seatid = Seat.objects.get(seatid=seat_id),
        )
        reservation_instance.save()
    except:
        return seatSelect(request, user_id, bus_id, start_id)
        
    return render(request, 'confirm.html', {'user_id': user_id})


# 예약 성공
@login_required
def initial(request):
    seats = Seat.objects.all()
    for seat in seats:
        seat.status = False
        seat.save()
    return HttpResponse("성공")





# 예약 생성 API / 예약 완료 버튼 API
@login_required
class ReservationViewSet(mixins.CreateModelMixin,
                         mixins.UpdateModelMixin,
                         GenericViewSet):
    
    queryset = Seat_info.objects.all()
    serializer_class = SeatSerializer
    # permission_classes = [IsOwner, ]

    def perform_create(self, serializer):
        get_object_or_404(Seat_info, id=self.kwargs.get('seat_info_pk'))
        serializer.save(member=self.request.user,
                        seat_id=self.kwargs.get('seat_info_pk'))


# 생성된 예약을 반환하는 API
@login_required
class ReservationHistoryViewSet(mixins.RetrieveModelMixin,
                                mixins.ListModelMixin,
                                GenericViewSet):
 queryset = Seat_info.objects.all()
    serializer_class = SeatSerializer
    # permission_classes = [IsOwner, ]

    def get_serializer_class(self):
        if self.action == 'history':
            return UseHistoryListSerializer
        return super().get_serializer_class()

    def filter_queryset(self, queryset):
        queryset = queryset.filter(member=self.request.user)
        return super().filter_queryset(queryset)

    @action(detail=False)
    def history(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
'''
