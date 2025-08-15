# ХЛЕБ54 Flask сайт

## Запуск локально
1. Установить зависимости:
```
pip install -r requirements.txt
```
2. Переименовать `.env.example` в `.env` и заполнить своими данными SMTP.
3. Запустить сервер:
```
python app.py
```

## Развёртывание на Render.com
- Загрузить проект в GitHub
- Создать новый Web Service на Render
- Указать команду запуска: `gunicorn app:app`
- В Variables внести переменные из `.env`
