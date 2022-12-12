from sqlalchemy import create_engine, Column, String, Integer, Text, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
from datetime import date
from fastapi import FastAPI
from models import CONN, Pessoa, Tokens
from secrets import token_hex

app = FastAPI()

def conectaBanco():
    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

@app.post('/cadastro')
def cadastro(nome: str, user: str, senha: str):
    session = conectaBanco()
    usuario = session.query(Pessoa).filter_by(usuario=user, senha=senha).all()

    if len(usuario) == 0:
        x = Pessoa(nome=nome, usuario=user, senha=senha)
        session.add(x)
        session.commit()
        return {'status' : 'Usuario cadastrado com sucesso!'}


    elif len(usuario) > 0:
        return {'status': 'Esse usuario já está cadastrado'}





