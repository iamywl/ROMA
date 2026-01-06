# ROMA

## [버그 기록](https://docs.google.com/presentation/d/1H_awmql93YOD6v-1pSeu13CaCOZjtBIWA9208dpQGys/edit?usp=sharing)

## 시스템 설계 다이어그램

1. **서비스 인프라 아키텍처**
![Infra](src/img/service_infra_arch.png)

**인프라 생성 시 고려 및 목표한 점**
* 개발지원 비용이 없다는 점을 고려하여 최대한 적은 비용으함 서비스를 배포해야함
* 도메인을 구매하는 것이 현실적으로 불가능하여 Route 53을 사용하지 않았음.
* ALB(Application Load Balancer)를 사용하면 추가적인 비용이 발생하여 클러스터의 IP를 이용하여 배포하고 서비스하지 않는 포트는 모두 방화벽으로 보호하는 방식으로 서비스를 배포.
* 개가장 빠르게 버그를 찾을 수 있고, 가장 빠르게 개발한 코드의 동작을 확인학 위해 자동적으로 서비스에 배포 될 수 있도록 CICD파이프라인 구성
* 개발된 코드가 자동적으로 서비스에 배포 될 수 있도록 CICD파이프라인 구성

2. **ERD**
![ERD](src/img/ERD.png)

**핵심 엔티티 구성**
총 4개로 구성
* User: 시스템의 기본 사용자 정보(ID, 비밀번호)를 담고 있음
* Profile: 사용자의 성향(취침 시간, MBTI, 흡연 여부 등)을 담은 확장 테이블
* ChatRoom: 사용자 간의 대화가 이뤄지는 공간
* ChatMessage: 채팅방 안에서 주고받은 실제 메시지 내용

**관계**
* User - Profile (1:1 관계):
    * 사용자당 1개의 프로필만 가짐
    * Django의 OneToOneField(FOREIGN KEY와 UNIQUE를 이용하여 1:1관계 강제함)를 사용하여 구현
    * 


3. **로그인/프로필 시퀀스**
![Login Profile](src/img/loginprofil_diagram.png)

4. **매칭 로직**
![Matching](src/img/matching_diagram.png)

5. **웹소켓 구조**
![WebSocket](src/img/websocket_diagram.png)



## API & Route map
| 기능         | HTTP Method | URL 경로                 | 설명                                                                     |   |
|------------|-------------|------------------------|------------------------------------------------------------------------|---|
| 홈 페이지      | GET         | /                      | 로그인 후 메인 페이지를 보여줍니다.                                                   |   |
| 회원가입       | GET, POST   | /accounts/signup/      | GET: 회원가입 폼을 보여줍니다. <br> POST: 사용자 정보를 받아 계정을 생성합니다.                   |   |
| 로그인        | GET, POST   | /accounts/login/       | GET: 로그인 폼을 보여줍니다. <br> POST: 사용자 인증을 수행합니다.                           |   |
| 로그아웃       | GET         | /accounts/logout/      | 로그아웃을 수행하고 홈으로 리다이렉트합니다.                                               |   |
| 마이페이지(프로필) | GET, POST   | /accounts/my_page/     | GET: 현재 사용자의 프로필(체크리스트)을 보여줍니다. <br> POST: 수정된 프로필 정보를 DB에 저장합니다.      |   |
| 룸메이트 매칭    | GET         | /matching/             | 현재 사용자의 프로필을 기반으로 매칭 점수가 높은 다른 사용자 목록을 보여줍니다.                          |   |
| 채팅 목록      | GET         | /chat/                 | 현재 사용자가 참여 중인 모든 채팅방 목록과 사용자 검색창을 보여줍니다.                               |   |
| 사용자 검색     | POST        | /chat/search/          | Request Body: username={검색할_아이디} <br> ID로 사용자를 검색하여 해당 채팅방으로 리다이렉트합니다. |   |
| 채팅방 입장     | GET         | /chat/{other_user_pk}/ | 특정 사용자(other_user_pk)와의 1:1 채팅방에 입장합니다.                                |   |
|            |             |                        |                                                                        |   |