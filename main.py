from flask import Flask, render_template, request
import smtplib
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def receive_data():
    E_mail = "merugusai112233@gmail.com"
    password = "vmcw wuem katw dzkj"  # Store this securely!

    name = request.form['name']
    user_email = request.form['email']
    user_password = request.form['password']

    message = f"Subject: Hello\n\nName: {name}\nPassword: {user_password}"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=E_mail, password=password)
        connection.sendmail(
            from_addr=E_mail,
            to_addrs=user_email,
            msg=message
        )
    return "Email sent successfully!"

if __name__ == "__main__":
    app.run(debug=True)
