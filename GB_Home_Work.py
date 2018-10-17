from telebot import apihelper
import telebot
import regex
from random import randint
import requests
from PIL import Image
import os

# ЗЫ
# то что удалось написать за несколько часов
# из недочетов - не хватает обработки ошибок особенно в getsticker связанных с http запросами и работой с файлами


# Не жалко, все равно тестовый
token = '671767776:AAG_Nn4UD91-j5axEvImp3zpcPU-ethr8zg'
apihelper.proxy = {'https': 'socks5h://proxyuser:proxypass@80.211.231.94:17836'}
bot = telebot.TeleBot(token)

# используемый временный каталог
tempdir = 'temp'

# Создание временного каталога
if not os.path.exists(tempdir):
    os.makedirs(tempdir)


accept_on_message = {'Msg_Counter': 0, 'accept_on': randint(2, 10)}


@bot.message_handler(content_types=['text'])
def answer(message):
    if regex.search(r'(?i).*?(Подтверди){e<=2}.?$', message.text) is not None:
        bot.reply_to(message, 'Подтверждаю!')
    else:
        accept_on_message['Msg_Counter'] += 1
        if accept_on_message['accept_on'] == accept_on_message['Msg_Counter']:
            accept_on_message['Msg_Counter'] = 0
            accept_on_message['accept_on'] = randint(2, 10)
            bot.send_message(message.chat.id, 'УГУ УГУ')


# для сообщения типа "стикер" сохрание в файл и отправка в png формате обратно отправителю
@bot.message_handler(content_types=['sticker'])
def getsticker(message):
    file_info = bot.get_file(message.sticker.file_id)
    sfile = f'{tempdir}/{file_info.file_id}'

    r = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, file_info.file_path), proxies=dict(https='socks5h://proxyuser:proxypass@80.211.231.94:17836'))
    if r.status_code == 200:
        open(f'{sfile}.webp', 'wb').write(r.content)
        # convert image
        img = Image.open(f'{sfile}.webp')
        img.save(f'{sfile}.png', 'png')
        # send image
        imageforsend = open(f'{sfile}.png', 'rb')
        bot.send_document(message.chat.id, imageforsend, caption=f'Emoji:{message.sticker.emoji}', reply_to_message_id=message.message_id)
        imageforsend.close()
        # remove files
        os.remove(f'{sfile}.webp')
        os.remove(f'{sfile}.png')
    else:
        bot.reply_to(message, 'Ошибка при конвертации стикера')


if __name__ == '__main__':
     bot.polling(none_stop=True, timeout=240)