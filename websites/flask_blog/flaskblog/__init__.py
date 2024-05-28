from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e7baf83401a1b5e1ea0007cb20a7b0b7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
from flaskblog import routes
from flaskblog.models import User

with app.app_context():
    # Create the database tables
    db.create_all()
    user = User.query.first()
    print(user)

# Print a message to indicate successful initialization
print("Database initialized successfully.")