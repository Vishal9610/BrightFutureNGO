from flask import Flask
from config import Config, mysql

from routes.home import home_bp
from routes.admin import admin_bp
from routes.gallery import gallery_bp
from routes.analytics import analytics_bp

app = Flask(__name__)

app.config.from_object(Config)

mysql.init_app(app)

app.register_blueprint(home_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(gallery_bp)
app.register_blueprint(analytics_bp)

if __name__ == "__main__":
    app.run(debug=True)