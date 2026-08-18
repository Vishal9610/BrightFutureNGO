# from flask_mysqldb import MySQL

# mysql = MySQL()


# class Config:

#     SECRET_KEY = "brightfuture_local_secret_key_2026"

#     MYSQL_HOST = "localhost"
#     MYSQL_USER = "root"
#     MYSQL_PASSWORD = ""
#     MYSQL_DB = "brightfuture"

#     UPLOAD_FOLDER = "static/uploads/gallery"




# from flask_mysqldb import MySQL
# from flask_mail import Mail

# mysql = MySQL()
# mail = Mail()


# class Config:

#     # Flask Session
#     SECRET_KEY = "brightfuture_local_secret_key_2026"

#     # MySQL
#     MYSQL_HOST = "localhost"
#     MYSQL_USER = "root"
#     MYSQL_PASSWORD = ""
#     MYSQL_DB = "brightfuture"

#     # Gallery Upload
#     UPLOAD_FOLDER = "static/uploads/gallery"

#     # Gmail SMTP
#     MAIL_SERVER = "smtp.gmail.com"
#     MAIL_PORT = 587
#     MAIL_USE_TLS = True
#     MAIL_USE_SSL = False

#     # IMPORTANT:
#     # Apna real Gmail yahan likhein
#     MAIL_USERNAME = "loveindiabyvishal9616@gmail.com"

#     # Gmail ka 16-digit APP PASSWORD yahan likhein
#     MAIL_PASSWORD = "xmrfcmwdavhkuddq"

#     MAIL_DEFAULT_SENDER = "loveindiabyvishal9616@gmail.com"












# import os

# from flask_mysqldb import MySQL
# from flask_mail import Mail

# mysql = MySQL()
# mail = Mail()


# class Config:

#     # =========================
#     # Flask Session
#     # =========================
#     SECRET_KEY = os.environ.get(
#         "SECRET_KEY",
#         "brightfuture_local_secret_key_2026"
#     )

#     # =========================
#     # MySQL
#     # =========================
#     MYSQL_HOST = os.environ.get("sql12.freesqldatabase.com", "localhost")
#     MYSQL_USER = os.environ.get("sql12835518", "root")
#     MYSQL_PASSWORD = os.environ.get("qiLhjnnbqK", "")
#     MYSQL_DB = os.environ.get("sql12835518", "brightfuture")
#     MYSQL_PORT = int(os.environ.get("3306", "3306"))
#     # Aiven MySQL SSL
#     MYSQL_SSL_MODE = os.environ.get("REQUIRED", "REQUIRED")

   

#     # =========================
#     # Gallery Upload
#     # =========================
#     UPLOAD_FOLDER = "static/uploads/gallery"

#     # =========================
#     # Gmail SMTP
#     # =========================
#     MAIL_SERVER = "smtp.gmail.com"
#     MAIL_PORT = 587
#     MAIL_USE_TLS = True
#     MAIL_USE_SSL = False

#     MAIL_USERNAME = os.environ.get("loveindiabyvishal9616@gmail.com")
#     MAIL_PASSWORD = os.environ.get("xmrfcmwdavhkuddq")

#     MAIL_DEFAULT_SENDER = os.environ.get("loveindiabyvishal9616@gmail.com")







import os

from flask_mysqldb import MySQL
from flask_mail import Mail

mysql = MySQL()
mail = Mail()


class Config:

    # =========================
    # Flask Session
    # =========================
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "brightfuture_local_secret_key_2026"
    )

    # =========================
    # MySQL - Render / FreeSQLDatabase
    # =========================
    MYSQL_HOST = os.environ.get(
        "MYSQL_HOST",
        "sql12.freesqldatabase.com"
    )

    MYSQL_USER = os.environ.get(
        "MYSQL_USER",
        "sql12835518"
    )

    MYSQL_PASSWORD = os.environ.get(
        "MYSQL_PASSWORD",
        "qiLhjnnbqK"
    )

    MYSQL_DB = os.environ.get(
        "MYSQL_DB",
        "sql12835518"
    )

    MYSQL_PORT = int(
        os.environ.get("MYSQL_PORT", "3306")
    )

    
# =========================
# Cloudinary
# =========================
CLOUDINARY_CLOUD_NAME = os.environ.get("cypipohx")
CLOUDINARY_API_KEY = os.environ.get("884271135157468")
CLOUDINARY_API_SECRET = os.environ.get("fAmH5p6FiM1F9wATItKtZ5WZxew")

    # =========================
    # Gallery Upload
    # =========================
    UPLOAD_FOLDER = "static/uploads/gallery"

    # =========================
    # Gmail SMTP
    # =========================
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    MAIL_USERNAME = os.environ.get(
        "MAIL_USERNAME",
        "loveindiabyvishal9616@gmail.com"
    )

    MAIL_PASSWORD = os.environ.get(
        "MAIL_PASSWORD",
        "xmrfcmwdavhkuddq"
    )

    MAIL_DEFAULT_SENDER = os.environ.get(
        "MAIL_DEFAULT_SENDER",
        "loveindiabyvishal9616@gmail.com"
    )

