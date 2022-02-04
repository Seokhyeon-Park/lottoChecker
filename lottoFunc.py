import telegram as tel
import key
from pytesseract import *
from PIL import Image

# bot 생성
bot = tel.Bot(token=key.token)

# 이미지 다운로드
def echo(update, cb):
    chat_id = update.message.chat_id
    file_id = update.message.photo[-1].file_id
    
    newFile = bot.getFile(file_id)
    newFile.download('img/lotto'+str(chat_id)+'.jpg')
    bot.sendMessage(chat_id=chat_id, text="download succesfull!")
    getNumber(chat_id)

# 이미지 처리
def getNumber(chat_id):
    img = Image.open('img/lotto'+str(chat_id)+'.jpg')
    text = pytesseract.image_to_string(img, config = '--psm 6')
    print(text)