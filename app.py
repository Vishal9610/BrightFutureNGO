from flask import Flask

from config import Config, mysql, mail

from routes.home import home_bp
from routes.admin import admin_bp
from routes.gallery import gallery_bp
from routes.analytics import analytics_bp


app = Flask(__name__)

# Load configuration
app.config.from_object(Config)

# Initialize MySQL
mysql.init_app(app)

# Initialize Flask-Mail
mail.init_app(app)

# Register Blueprints
app.register_blueprint(home_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(gallery_bp)
app.register_blueprint(analytics_bp)


if __name__ == "__main__":
    app.run(debug=True)