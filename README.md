# <p align="center">Telegram bot Geek Brains Homework

Домашнее задание.

Запуск бота.
* Создать виртуальное окружение (пример для Win)
```
path\to\python\dir\python -m venv d:\test\.venv
```
* выполнить git clone (либо сохранить файлы GB_Home_Work.py и requirements.txt вручную в каталг проекта)
* активировать venv (через cmd)
```
cd d:\test\.venv\scripts
activate
```
* Установить зависимости 
```
pip install -r requirements.txt
```
* Запустить GB_Home_Work.py любым удобным способом
вариант:
```
python ../../GB_Home_Work.py
```

Бот обрабатывает:
* текстовые сообщения согласно заданию
* сообщения типа "sticker", получив стикер файл конвертируется в png и отправляется обратно в чат

