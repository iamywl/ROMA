# ROMA

## [버그 기록](https://docs.google.com/presentation/d/1H_awmql93YOD6v-1pSeu13CaCOZjtBIWA9208dpQGys/edit?usp=sharing)


### 시스템 설계 다이어그램

1. **ERD**
![ERD](./img/ERD.png)

2. **로그인/프로필 시퀀스**
![Login Profile Diagram](./img/loginprofil_diagram.png)

3. **매칭 로직**
![Matching Diagram](./img/matching_diagram.png)

4. **서비스 인프라 아키텍처**
![Service Infra Architecture](./img/service_infra_arch.png)

5. **웹소켓 구조**
![WebSocket Diagram](./img/websocket_diagram.png)




## API 

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