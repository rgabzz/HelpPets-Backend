from dotenv import load_dotenv
import os

load_dotenv()

# Pega a chave secreta de criptografia, guardada na env
SECRET_KEY = os.getenv('SECRET_KEY')

# Pega a chave secreta de criptografia, guardada na env
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

# Identifica o banco de dados que o SQLAlchemy vai usar
SQLALCHEMY_DATABASE_URI = \
 '{SGBD}://{usuario}:{senha}@{servidor}/{database}?charset=utf8mb4'.format(
    SGBD = 'mysql+mysqlconnector',
    usuario = 'root',
    senha = 'gabzz',
    servidor = '127.0.0.1',
    database = 'help_pets'
)