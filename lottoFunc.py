import telegram as tel
import key
import cv2
from pytesseract import *
from PIL import Image

# bot 생성
bot = tel.Bot(token=key.token)

# 이미지 다운로드
def echo(update, cb):
    # 업데이트된 파일과 해당 파일 채팅 유저
    chat_id = update.message.chat_id
    file_id = update.message.photo[-1].file_id
    
    # 업데이트된 파일 다운로드
    newFile = bot.getFile(file_id)
    newFile.download('img/lotto'+str(chat_id)+'.jpg')
    imgProcessing(chat_id)

# 이미지 처리
def imgProcessing(chat_id):
    # 다운로드된 이미지 불러오기
    # 이미지 색상을 뚜렷하게 변경
    imgArr = cv2.imread('img/lotto'+str(chat_id)+'.jpg', 0)

    for dOne in range(0, len(imgArr)):
        for dTwo in range(0, len(imgArr[dOne])):
            if imgArr[dOne][dTwo] < 210:
                imgArr[dOne][dTwo] = 0
    
    # 변경된 이미지 저장
    cv2.imwrite('img/lotto'+str(chat_id)+'.jpg', imgArr)

    # 숫자 영역 및 MNIST
    # https://kagus2.tistory.com/28

    # 변경된 이미지 불러오기
    img = Image.open('img/lotto'+str(chat_id)+'.jpg')
    text = pytesseract.image_to_string(img, config = '--psm 6')
    bot.sendMessage(chat_id=chat_id, text=text)