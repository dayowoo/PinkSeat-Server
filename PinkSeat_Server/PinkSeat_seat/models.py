from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model


# 지하철 공공데이터 API 명세 작성에 따라 설계
class Subway(models.Model):
    # api 서비스 키
    service_key = models.TextField(max_length=300, blank=False, null=False)
    # 페이지번호
    pageNo = models.IntegerField(blank=False, null=False)
    # 한 페이지 결과 수
    numOfRows = models.IntegerField(blank=False, null=False)
    # 도시코드
    cityCd = models.CharField(max_length=300, blank=False, null=False)
    # 노선번호
    lineNo = models.IntegerField(blank=False, null=False, default=0)
    # 노선순서
    #routOrd = models.IntegerField(blank=False, null=False)
    # 역코드
    stationCd = models.IntegerField(blank=False, null=False, default=0)
    # 역명
    stationNm = models.CharField(max_length=300, blank=False, null=False, default="판암")


# 좌석 정보
class Seat_info(models.Model):
    space = models.IntegerField(default=1) # 좌석 칸
    # pk / 임산부 좌석 이름 (A1, A2, ...)
    seat_name = models.CharField(max_length=20)
    # 좌석 상태 : 0=비어있음, 1=일반인 앉음, 2= 임산부 착석
    seat_stat = models.IntegerField(default=0)
    # 동작모드 : 0= 아무동작X, 1= 양보요청 울리기
    alarm = models.BooleanField(default=False)

    def __self__(self):
        return self.seat_name


# 예약 정보
class Reservation(models.Model):
    reservation_id = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    seat = models.ForeignKey(Seat_info, on_delete=models.CASCADE)

    def __str__(self):
        return self.reservation_id


# 지하철 시간표 DB
class SubSchedule(models.Model):
    station = models.CharField(max_length=200)
    a1002 = models.CharField(max_length=100, null=True)
    a1004 = models.CharField(max_length=100, null=True)
    a1006 = models.CharField(max_length=100, null=True)
    a1008 = models.CharField(max_length=100, null=True)
    a1010 = models.CharField(max_length=100, null=True)
    a1012 = models.CharField(max_length=100, null=True)
    a1014 = models.CharField(max_length=100, null=True)
    a1016 = models.CharField(max_length=100, null=True)
    a1018 = models.CharField(max_length=100, null=True)
    a1020 = models.CharField(max_length=100, null=True)
    a1022 = models.CharField(max_length=100, null=True)
    a1024 = models.CharField(max_length=100, null=True)
    a1026 = models.CharField(max_length=100, null=True)
    a1028 = models.CharField(max_length=100, null=True)
    a1030 = models.CharField(max_length=100, null=True)
    a1032 = models.CharField(max_length=100, null=True)
    a1034 = models.CharField(max_length=100, null=True)
    a1036 = models.CharField(max_length=100, null=True)
    a1038 = models.CharField(max_length=100, null=True)
    a1040 = models.CharField(max_length=100, null=True)
    a1042 = models.CharField(max_length=100, null=True)
    a1044 = models.CharField(max_length=100, null=True)
    a1046 = models.CharField(max_length=100, null=True)
    a1048 = models.CharField(max_length=100, null=True)
    a1050 = models.CharField(max_length=100, null=True)
    a1052 = models.CharField(max_length=100, null=True)
    a1054 = models.CharField(max_length=100, null=True)
    a1056 = models.CharField(max_length=100, null=True)
    a1058 = models.CharField(max_length=100, null=True)
    a1060 = models.CharField(max_length=100, null=True)
    a1062 = models.CharField(max_length=100, null=True)
    a1064 = models.CharField(max_length=100, null=True)
    a1066 = models.CharField(max_length=100, null=True)
    a1068 = models.CharField(max_length=100, null=True)
    a1070 = models.CharField(max_length=100, null=True)
    a1072 = models.CharField(max_length=100, null=True)
    a1074 = models.CharField(max_length=100, null=True)
    a1076 = models.CharField(max_length=100, null=True)
    a1078 = models.CharField(max_length=100, null=True)
    a1080 = models.CharField(max_length=100, null=True)
    a1082 = models.CharField(max_length=100, null=True)
    a1084 = models.CharField(max_length=100, null=True)
    a1088 = models.CharField(max_length=100, null=True)
    a1090 = models.CharField(max_length=100, null=True)
    a1092 = models.CharField(max_length=100, null=True)
    a1094 = models.CharField(max_length=100, null=True)
    a1096 = models.CharField(max_length=100, null=True)
    a1098 = models.CharField(max_length=100, null=True)
    a1100 = models.CharField(max_length=100, null=True)
    a1102 = models.CharField(max_length=100, null=True)
    a1104 = models.CharField(max_length=100, null=True)
    a1106 = models.CharField(max_length=100, null=True)
    a1108 = models.CharField(max_length=100, null=True)
    a1110 = models.CharField(max_length=100, null=True)
    a1112 = models.CharField(max_length=100, null=True)
    a1114 = models.CharField(max_length=100, null=True)
    a1116 = models.CharField(max_length=100, null=True)
    a1118 = models.CharField(max_length=100, null=True)
    a1120 = models.CharField(max_length=100, null=True)
    a1122 = models.CharField(max_length=100, null=True)
    a1124 = models.CharField(max_length=100, null=True)
    a1126 = models.CharField(max_length=100, null=True)
    a1128 = models.CharField(max_length=100, null=True)
    a1130 = models.CharField(max_length=100, null=True)
    a1132 = models.CharField(max_length=100, null=True)
    a1134 = models.CharField(max_length=100, null=True)
    a1136 = models.CharField(max_length=100, null=True)
    a1138 = models.CharField(max_length=100, null=True)
    a1140 = models.CharField(max_length=100, null=True)
    a1142 = models.CharField(max_length=100, null=True)
    a1144 = models.CharField(max_length=100, null=True)
    a1146 = models.CharField(max_length=100, null=True)
    a1148 = models.CharField(max_length=100, null=True)
    a1150 = models.CharField(max_length=100, null=True)
    a1152 = models.CharField(max_length=100, null=True)
    a1154 = models.CharField(max_length=100, null=True)
    a1156 = models.CharField(max_length=100, null=True)
    a1158 = models.CharField(max_length=100, null=True)
    a1160 = models.CharField(max_length=100, null=True)
    a1162 = models.CharField(max_length=100, null=True)
    a1164 = models.CharField(max_length=100, null=True)
    a1166 = models.CharField(max_length=100, null=True)
    a1168 = models.CharField(max_length=100, null=True)
    a1170 = models.CharField(max_length=100, null=True)
    a1172 = models.CharField(max_length=100, null=True)
    a1174 = models.CharField(max_length=100, null=True)
    a1176 = models.CharField(max_length=100, null=True)
    a1178 = models.CharField(max_length=100, null=True)
    a1180 = models.CharField(max_length=100, null=True)
    a1182 = models.CharField(max_length=100, null=True)
    a1184 = models.CharField(max_length=100, null=True)
    a1186 = models.CharField(max_length=100, null=True)
    a1188 = models.CharField(max_length=100, null=True)
    a1190 = models.CharField(max_length=100, null=True)
    a1192 = models.CharField(max_length=100, null=True)
    a1194 = models.CharField(max_length=100, null=True)
    a1196 = models.CharField(max_length=100, null=True)
    a1198 = models.CharField(max_length=100, null=True)
    a1200 = models.CharField(max_length=100, null=True)
    a1202 = models.CharField(max_length=100, null=True)
    a1204 = models.CharField(max_length=100, null=True)
    a1206 = models.CharField(max_length=100, null=True)
    a1208 = models.CharField(max_length=100, null=True)
    a1210 = models.CharField(max_length=100, null=True)
    a1212 = models.CharField(max_length=100, null=True)
    a1214 = models.CharField(max_length=100, null=True)
    a1216 = models.CharField(max_length=100, null=True)
    a1218 = models.CharField(max_length=100, null=True)
    a1220 = models.CharField(max_length=100, null=True)
    a1222 = models.CharField(max_length=100, null=True)
    a1224 = models.CharField(max_length=100, null=True)
    a1226 = models.CharField(max_length=100, null=True)
    a1228 = models.CharField(max_length=100, null=True)
    a1230 = models.CharField(max_length=100, null=True)
    a1232 = models.CharField(max_length=100, null=True)
    a1234 = models.CharField(max_length=100, null=True)
    a1236 = models.CharField(max_length=100, null=True)
    a1238 = models.CharField(max_length=100, null=True)
    a1240 = models.CharField(max_length=100, null=True)
    a1242 = models.CharField(max_length=100, null=True)

    def __str__(self): 
        return self.station




'''
class Subway(models.Model):
    subway_id = models.PositiveIntegerField(primary_key=True)
    subway_name = models.CharField(max_length=50)

    def __str__(self):
        return self.subwayname

# 좌석 정보
class Seat(models.Model):
    seat_id = models.IntegerField(primary_key=True)
    subway_id = models.ForeignKey(Subway, on_delete=models.CASCADE)
    seat_row = models.IntegerField()
    seat_col = models.CharField(max_length=11)
    status = models.BooleanField(default=False)

    def __str__(self):
        return "{0}{1}".format(self.seatcol, self.seatrow)

# 예약 정보
class Reservation(models.Model):
    reservationid = models.CharField(max_length=20, primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    seatid = models.ForeignKey(Seat, on_delete=models.CASCADE)

    def __str__(self):
        return self.reservationid

'''





