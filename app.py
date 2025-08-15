from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
import os

from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        comment = request.form.get("comment")

        # Отправка письма
        smtp_server = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
        smtp_port = int(os.environ.get("SMTP_PORT", 587))
        smtp_username = os.environ.get("SMTP_USERNAME")
        smtp_password = os.environ.get("SMTP_PASSWORD")
        to_email = os.environ.get("TO_EMAIL", "1790144@gmail.com")

        subject = f"Новая заявка с сайта ХЛЕБ54 от {name}"
        body = f"Имя: {name}\nТелефон: {phone}\nКомментарий: {comment}"

        msg = MIMEText(body, "plain", "utf-8")
        msg["Subject"] = subject
        msg["From"] = smtp_username
        msg["To"] = to_email

        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.send_message(msg)
            flash("Заявка успешно отправлена!", "success")
        except Exception as e:
            flash(f"Ошибка при отправке: {e}", "error")

        return redirect(url_for("index"))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
