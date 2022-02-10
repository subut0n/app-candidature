import os
import psycopg2
#Database initialization
# if os.environ.get('DATABASE_URL') is None:
#     basedir = os.path.abspath(os.path.dirname(__file__))
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# else:
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

SQLALCHEMY_DATABASE_URI = "postgres://zknfzgayureaep:3ea358f223f36b642b214319c7e095e787ae9a618cce330fe23065f5f12a3944@ec2-54-77-182-219.eu-west-1.compute.amazonaws.com:5432/d9blfsn01rfeds"

SECRET_KEY = 'VerySecret'
SQLALCHEMY_TRACK_MODIFICATIONS = False


