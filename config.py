# from flask_mysqldb import MySQL

# mysql = MySQL()


# class Config:

#     SECRET_KEY = "brightfuture_local_secret_key_2026"

#     MYSQL_HOST = "localhost"
#     MYSQL_USER = "root"
#     MYSQL_PASSWORD = ""
#     MYSQL_DB = "brightfuture"

#     UPLOAD_FOLDER = "static/uploads/gallery"


from flask_mysqldb import MySQL
from flask_mail import Mail

mysql = MySQL()
mail = Mail()


class Config:

    # Flask Session
    SECRET_KEY = "brightfuture_local_secret_key_2026"

    # MySQL
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DB = "brightfuture"

    # Gallery Upload
    UPLOAD_FOLDER = "static/uploads/gallery"

    # Gmail SMTP
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    # IMPORTANT:
    # Apna real Gmail yahan likhein
    MAIL_USERNAME = "loveindiabyvishal9616@gmail.com"

    # Gmail ka 16-digit APP PASSWORD yahan likhein
    MAIL_PASSWORD = "kliekvxqfynksxvv"

    MAIL_DEFAULT_SENDER = "loveindiabyvishal9616@gmail.com"