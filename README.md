# 구글 플레이 마켓, 애플 앱 스토어에서 리뷰를 가져와서 텔레그램 노티로 알려주는 작업

![python3.9.2](https://img.shields.io/badge/python-3.9.2-green.svg)

깃허브의 액션을 기반으로 하루에 한번 특정앱의 리뷰를 검사하여 텔레그램으로 알려주는 것을 작성 예정.  


### 설정해야 하는것
- 환경변수 
	- TELEGRAM_BOT_TOKEN : 텔레그램 봇 토큰
	- TELEGRAM_CHAT_ID : 텔레그램 챗 아이디 
	- APPLE_REVIEW_URL : 애플의 리뷰 url


### python에서 필요한 라이브러리
Pillow
pyTelegramBotAPI
requests


### 앞으로 진행할 일정.

- [x] 애플의 리뷰 가져오기
- [x] 애플의 리뷰 가공해서 텔레그램으로 전달
- [ ] 구글의 리뷰 가져오기 
- [ ] 구글의 리뷰 가져와서 텔레그램으로 전달
- [ ] 기존에 가져온 리뷰와 새로운 리뷰 구분하는 방법 확인

--- 
- [ ] 텔레그램 답장으로 리뷰 답장 작성하기.