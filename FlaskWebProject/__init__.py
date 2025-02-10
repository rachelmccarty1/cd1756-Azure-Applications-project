"""
The flask application package.
"""
import logging
from flask import Flask, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, user_logged_in, user_login_failed
from flask_session import Session
 
app = Flask(__name__)
app.config.from_object(Config)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'
 
import FlaskWebProject.views
@user_logged_in.connect_via(app)
def log_successful_login(sender, user):
    logger.info(f"User {user.id} logged in successfully from {request.remote_addr}")
@user_login_failed.connect_via(app)
def log_failed_login(sender, credentials):
    logger.warning(f"Failed login attempt for user {credentials['username']} from {request.remote_addr}")
