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

@app.post('login')
def login(usuario : str, senha : str):
    session = conectaBanco()
    user = session.query(Pessoa).filter_by(usuario = usuario, senha = senha)
    if len(user) == 0:
        return {'status' : 'Usuario não existe'}

    while True:
        token = token_hex(50)
        token_existe = session.query(Tokens).filter_by(token=token).all()
        if len(token_existe) == 0:
            pessoa_existe = session.query(Tokens).filter_by(id_pessoa=user[0].id).all()

            if len(pessoa_existe) == 0:
                novo_token = Tokens(id_pessoa=user[0].id, token=token)
                session.add(novo_token)
            elif len(pessoa_existe) > 0:
                pessoa_existe[0].token = token

            session.commit()
            break
        return token







