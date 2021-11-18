# Django Rest Framework를 이용해 만든 PinkSeat 서버
👩‍💻 Server with Django Rest API / MySQL - 2021 Capstone Design


---

#### [선다영](https://github.com/dayowoo)
#### Department of Information and Communication Engineering at SMU
<br>
#### ✨ 맡은 파트

	- Django Rest Framework / MySQL 개발
	- retrofit 을 사용한 Android - Django 통신 구현
	- Raspberry Pi - 서버 통신 구현 (server-final.py 파일 참조)

#### <br>

### Introduction

---

### 💌 Summary

* 🎬 **DEMO VIDEO** : https://www.youtube.com/watch?v=5QyCfUJtvto&t=1s

  <br>

* **Project 소개**

  <img align="left" src="https://github.com/dayowoo/PinkSeat-Server/issues/1#issue-1056981041" width="600" height="auto">
  <br>
  지하철 내 임산부 좌석이 도입된 지 8년째이지만, 서울 지하철 임산부 배려석 관련 민원은 하루 평균 75.9건이 접수될 정도로 갈등이 지속되고 있다. 현 지하철 임산부 좌석 시스템은 비워두는 것이 원칙이지만 아직까지 비워두기 규칙이 잘 지켜지지 않고 있어 양보를 요청하기 눈치 보인다는 불편함이 제기되었다. 더불어 초기 임산부의 경우, 겉모습으로 임산부 여부를 판단하기 매우 주관적이기 때문에 양보 받기 어려움 등의 문제점이 있다. PinkSeat는 기존 임산부 좌석의 문제점들을 개선하여 임산부 좌석을 효율적으로 이용할 수 있도록 하는 **임산부 좌석 관리 IoT**이다.

  <br>

* **주요 기능**

  * 회원가입 / 로그인 / 로그아웃 을 수행합니다.

  * 지하철 좌석 현황을 확인합니다

    * 빈 좌석 : 하얀색
    * 임산부 착석 좌석 : 초록색
    * 일반인 착석 좌석 : 빨간색 

  * QR코드 인증을 통해 임산부를 인증합니다.

  * 일반인 착석 좌석에 양보요청을 울립니다.

  * 마스크 착용 여부를 구분하여 미착용시, 알람을 울립니다.

    <br>

* **BACKEND** : [Django Rest Framework](https://github.com/dayowoo/PinkSeat-Server)

* **DATABASE** : [MySQL](https://github.com/dayowoo/PinkSeat-Server)

* **FRONTEND** : Android Studio

* **HARDWARE** : Raspberry Pi

<br>



### 📚 What I Earned

---

-   `Django Rest Framework` 에 대한 이해
-   `DRF` - `Android` retrofit 통신
-   `DRF` - `Raspberry Pi`  통신

<br>



### 📢 Report implemented assignment

---

* 구현한 기능 및 제약사항들을 케이스별로 시뮬레이션하며 설명합니다.
* 모든 케이스들은 순차적으로 진행되며, 해당 DB는 MySQL에 저장되어 있습니다.
* 시뮬레이션 및 기능 설명 순서는 다음과 같습니다
  1. Django 서버 - MySQL 연동
  2. Django - Android 간 회원 관리 기능
  3. Android - Server - 라즈베리파이 간 양보요청 기능 구현
  4. Android - Server 임산부 QR코드 인증 구현
  5. 라즈베리파이 마스크 인식

