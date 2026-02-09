from sqlalchemy import Integer,String,Boolean,DateTime,Date,Enum
from flask_login import UserMixin
from app import db
import enum

class Cargo(enum.Enum):
    USUARIO = 'usuario'
    ONG = 'ong' 
    ADMIN = 'admin'


class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios' 
    id = db.Column(Integer(), primary_key=True) 
    nome = db.Column(String(255), nullable=False) 
    genero = db.Column(String(20), nullable=False)
    nascimento = db.Column(Date(), nullable=False)
    telefone  = db.Column(String(20), nullable=False)
    cpf = db.Column(String(14), nullable=False, unique=True)
    estado = db.Column(String(50), nullable=False)
    cidade = db.Column(String(100), nullable=False)
    senha_hash=  db.Column(String(512), nullable=False)
    email=  db.Column(String(255), nullable=False, unique=True)
    criado_em = db.Column(DateTime(), nullable=False, default=db.func.now())
    ativo = db.Column(Boolean, nullable=False,default=True)
    tipo = db.Column(Enum(Cargo), nullable= False)