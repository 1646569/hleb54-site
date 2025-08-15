from flask import Flask, render_template, request
import smtplib
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev')

TO_EMAIL = os.environ.get('TO_EMAIL')
SMTP_SERVER = os.environ.get('SMTP_SERVER')
SMTP_PORT = int(os.environ.get('SMTP_PORT', 587))
SMTP_USERNAME = os.environ.get('SMTP_USERNAME')
SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacts', methods=['GET', 'POST'])
def feedback():
    message = ''
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(SMTP_USERNAME, SMTP_PASSWORD)
                subject = f'Обратная связь с сайта: {name}'
                body = f'Имя: {name}\nТелефон: {phone}'
                msg = f'Subject: {subject}\n\n{body}'
                server.sendmail(SMTP_USERNAME, TO_EMAIL, msg)
            message = 'Спасибо! Мы свяжемся с вами.'
        except Exception as e:
            message = f'Ошибка отправки: {e}'
    return render_template('contacts.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
