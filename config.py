from flask_mysqldb import MySQL
mysql = MySQL()
class Config:
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DB = "brightfuture"
    SECRET_KEY = "brightfuture123"
    UPLOAD_FOLDER = "static/uploads/gallery"