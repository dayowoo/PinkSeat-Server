import urllib.request as ul
import xmltodict
import json
import sys
import io
import requests

#아톰에디터 한글사용을 위한 구문
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#데이터를 받을 url (대전 지하철 1호선)
url = "http://openapi.tago.go.kr/openapi/service/MetroRtInfoService/getMetroLineInfoList?serviceKey=RHv0D4SxDrFwkzbgY%2FddXyxdIZsdCc%2Bt5tTVkxoIFz3wVoYJZHTaz2%2FyJgEeJeXBiECabr4bFqkDZ8TBnG70ww%3D%3D&pageNo=1&numOfRows=10&cityCd=DJ&lineNo=1"

#url의 데이터를 요청함
request = ul.Request(url)

#요청받은 데이터를 열어줌
response = ul.urlopen(request)

#제대로 데이터가 수신됐는지 확인하는 코드 성공시 200
rescode = response.getcode()

# 데이터출력하기
if(rescode == 200):
    responseData = response.read()
    #요청받은 데이터를 읽음
    rD = xmltodict.parse(responseData)
    #XML형식의 데이터를 dict형식으로 변환시켜줌

    rDJ = json.dumps(rD)
    #dict 형식의 데이터를 json형식으로 변환

    rDD = json.loads(rDJ)
    #json형식의 데이터를 dict 형식으로 변환
    
    print(rDD)
    #정상적으로 데이터가 출력되는지 확인


    
'''
def subwayParsing():
    #데이터를 받을 url (대전 지하철 1호선)
    url = "http://openapi.tago.go.kr/openapi/service/MetroRtInfoService/getMetroLineInfoList?serviceKey=RHv0D4SxDrFwkzbgY%2FddXyxdIZsdCc%2Bt5tTVkxoIFz3wVoYJZHTaz2%2FyJgEeJeXBiECabr4bFqkDZ8TBnG70ww%3D%3D&pageNo=1&numOfRows=10&cityCd=DJ&lineNo=1"

    #url의 데이터를 요청함
    request = ul.Request(url)

    #요청받은 데이터를 열어줌
    response = ul.urlopen(request)

    #제대로 데이터가 수신됐는지 확인하는 코드 성공시 200
    rescode = response.getcode()

    # 데이터출력하기
    if(rescode == 200):
        responseData = response.read()
        #요청받은 데이터를 읽음
        rD = xmltodict.parse(responseData)
        #XML형식의 데이터를 dict형식으로 변환시켜줌

        rDJ = json.dumps(rD)
        #dict 형식의 데이터를 json형식으로 변환

        rDD = json.loads(rDJ)
        #json형식의 데이터를 dict 형식으로 변환
        
        #print(rDD)
        #정상적으로 데이터가 출력되는지 확인

    return rdd
'''
  

'''
    #데이터를 받을 url (대전 지하철 1호선)
    url = "http://openapi.tago.go.kr/openapi/service/MetroRtInfoService/getMetroLineInfoList?serviceKey=RHv0D4SxDrFwkzbgY%2FddXyxdIZsdCc%2Bt5tTVkxoIFz3wVoYJZHTaz2%2FyJgEeJeXBiECabr4bFqkDZ8TBnG70ww%3D%3D&pageNo=1&numOfRows=10&cityCd=DJ&lineNo=1"
    key = "RHv0D4SxDrFwkzbgY%2FddXyxdIZsdCc%2Bt5tTVkxoIFz3wVoYJZHTaz2%2FyJgEeJeXBiECabr4bFqkDZ8TBnG70ww%3D%3D"
    # url에 요청보내기
    req = requests.get(url).content
    xmlObject = xmltodict.parse(req)
    allData = xmlObject['response']['body']['items']['item']
    return allData
'''