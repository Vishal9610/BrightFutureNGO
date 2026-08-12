import os
from flask_mysqldb import MySQL

mysql = MySQL()


class Config:

    MYSQL_HOST = os.environ.get(
        "MYSQL_HOST",
        "sql12.freesqldatabase.com"
    )

    MYSQL_USER = os.environ.get(
        "MYSQL_USER",
        "sql12834978"
    )

    MYSQL_PASSWORD = os.environ.get(
        "MYSQL_PASSWORD"
    )

    MYSQL_DB = os.environ.get(
        "MYSQL_DB",
        "sql12834978"
    )

    MYSQL_PORT = int(
        os.environ.get("MYSQL_PORT", "3306")
    )

    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "brightfuture-secret"
    )

    UPLOAD_FOLDER = "static/uploads/gallery"