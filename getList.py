import requests
import json
import os
import telegramModule
import sys
from datetime import datetime
import pytz

reviewListUrl = os.environ.get("APPLE_REVIEW_URL")
telegramChatId = os.environ.get("TELEGRAM_CHAT_ID")




ratingString = ["", "⭐", "⭐⭐", "⭐⭐⭐",  "⭐⭐⭐⭐", "🌟🌟🌟🌟🌟"]
class userReviewData:
  def __init__(self, jsonData):
    self.name = jsonData["author"]["name"]["label"]
    self.rating = jsonData["im:rating"]["label"]
    self.version = jsonData["im:version"]["label"]
    self.reviewId = jsonData["id"]["label"]
    self.title = jsonData["title"]["label"]
    self.content = jsonData["content"]["label"]
    self.updated = jsonData["updated"]["label"]
    

# 링크에서 리뷰들 가져오는 함수 
def getListFromUrl():
  r = requests.get(
      url=reviewListUrl
    )

  reviewList = []

  data = json.loads(r.text)
  for e in data.get("feed").get("entry"):
    reviewList.append(
      userReviewData(e)
    )

  return reviewList



# 환경설정 파일 읽기.
exefilePath = os.path.dirname(sys.argv[0])
idFilePath = exefilePath+'/tempLast.id'


# 아이디 파일이 없으면 0으로 세팅한다. 나오는 모든 글을 검사해서 전달하게 된다.
if os.path.isfile(idFilePath) is False:
  fp = open(idFilePath, 'w')
  fp.write("0")
  fp.close()



# 마지막으로 읽은 파일 게시글의 숫자를 가지고 온다.
fp = open(idFilePath, 'r')
line = fp.readline()
fp.close()
print("=================검사시작=================")
print(f"파일에 저장되어 있던 마지막 점검 글의 아이디{line}")
storedlastid = int(line)
newLastId = storedlastid


reviewLists = getListFromUrl()

for r in reviewLists:
  reviewId = int(r.reviewId)
  if reviewId > newLastId:
    newLastId = reviewId
  

  if reviewId > storedlastid:
    # 새로 추가된 리뷰
    print(f"{r.name} // {r.rating}  // {r.title} // {r.reviewId}")
    starRating = int(r.rating)
    if starRating > 5:
      starRating = 5
    if starRating < 1: 
      starRating = 1

    KST = pytz.timezone('Asia/Seoul')
    # 2021-09-14T02:55:55-07:00
    updateTime = datetime.strptime(r.updated, '%Y-%m-%dT%H:%M:%S%z').astimezone(KST).strftime('%Y년 %m월 %d일 %H:%M:%S')

    msg = f"{updateTime}\n{r.name}\n{ratingString[starRating]}\n제목: {r.title}\n\n{r.content}"
    telegramModule.sendMessage(telegramChatId, msg)

print(f"검사 완료 후 마지막 아이디  {newLastId}")
if newLastId > storedlastid: 
  fp = open(idFilePath,'w')
  fp.write(str(newLastId))
  fp.close()
  print(f"검사후 기존 저장 번호 {storedlastid}, 신규 저장번호 {newLastId}")

print("!!!!!!!!!!!!!!!       검사끝        !!!!!!!!!!!!!!!")
print("::set-output name=list_count::"+ str(newLastId - storedlastid) + "")



