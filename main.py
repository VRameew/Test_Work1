import requests
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy.ext.declarative import declarative_base
from fastapi import FastAPI

#Data class for SQL base
Base = declarative_base()
class Data(Base):
    __tablename__ = "data"

    id_question = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    question = sa.Column(sa.Text, nullable=False)
    answer = sa.Column(sa.Text, nullable=False)
    date_create = sa.Column(sa.Text, nullable=False)

#Creating SQL Base
engine = sa.create_engine("postgresql+psycopg2://postgres:postgres@DB", echo=True, pool_pre_ping=True)
#Creating tables
Base.metadata.create_all(engine)

DBSession = sessionmaker(
    binds={Base: engine},
    expire_on_commit=False,
)
session = DBSession()

#Start FastAPI APP
app = FastAPI()

def response_new_question():
    """Request for New Data if founds duplicates"""
    url = f'https://jservice.io/api/random?count={1}'
    response = requests.get(url)
    questions = (response.json())
    data = Data(id_question=questions[0]['id'], question=questions[0]['question'],
                    answer=questions[0]['answer'], date_create=questions[0]['created_at'])
    return data

def save_data(data):
    """Function for saved non duplicates data"""
    id_in_base = session.query(Data.id_question).all()
    data_base = session.query(Data).all()
    print(data_base)
    for quest in data:
        if quest.id_question not in id_in_base:
            session.add(quest)
        else:
            while True:
                new_quest = response_new_question()
                if new_quest.id_question not in id_in_base:
                    session.add(new_quest)
                    break
                else:
                    pass
    session.commit()

@app.post('/api/{questions_num}')
async def response_question(questions_num: int):
    """API App takes one value INT for request questions on public API
    And saved data in PostgresSQL"""
    url = f'https://jservice.io/api/random?count={questions_num}'
    response = requests.get(url)
    questions = (response.json())
    data = []
    for quest in questions:
        data.append(Data(id_question=quest['id'], question=quest['question'],
                    answer=quest['answer'], date_create=quest['created_at']))
    save_data(data)
    return data
