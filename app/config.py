from decouple import config
import os

class Config:
    SECRET_KEY = config('SECRET_KEY')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'klicheflask@gmail.com'
    MAIL_PASSWORD = 'sjqf zpbl pmtn xkjj'
    # os.path.join
    UPLOAD_FOLDER = os.path.join('app', 'static', 'images')

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig
}
