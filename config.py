import os

SECRET_KEY = 'why are you gae?'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root0',
        senha = 'admin0',
        servidor = 'localhost',
        database = 'jogoteca'
    )    

UPLOAD_PATH  = os.path.dirname(os.path.abspath(__file__)) + '/uploads'