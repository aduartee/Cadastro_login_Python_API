from sqlalchemy import create_engine, Column, String,Integer, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

USUARIO = 'root'
SENHA = ''
HOST = 'localhost'
BANCO = 'projetoapi'
PORTA = '3306'


CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORTA}/{BANCO}"

engine = create_engine(CONN, echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Pessoa(Base):
    __tablename__ = 'Pessoa'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    usuario = Column(String(40))
    senha = Column(String(10))

class Tokens(Base):
    __tablename__ = 'Tokens'
    id = Column(Integer, primary_key=True)
    id_pessoa = Column(ForeignKey('Pessoa.id'))
    token = Column(String(100))
    data = Column(datetime, default=datetime.utc.now())

