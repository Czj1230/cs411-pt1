# This is config file for connecting mysql server
import os
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'Aduiduidui'
HOST = '35.192.159.68'
PORT = '3306'
DATABASE = 'steamgame'
SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
# mysql does not recoginize utf8, so write in utf8 format directly
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True