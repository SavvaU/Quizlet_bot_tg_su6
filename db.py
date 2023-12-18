import logging

from random_word import RandomWords
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
import requests
from config import settings
from models import Word
from utils import translate_text


class Database:
    def __init__(self, db_url: str):
        self.__db_url = db_url
        self.__engine = None

    def connect(self):
        self.__engine = create_engine(url=self.__db_url)
        try:
            self.sql_query(query=select(1))
            print("Connected to database")
        except Exception as e:
            logging.error(e)

    def create_object(self, obj):
        with Session(self.__engine, expire_on_commit=False) as session:
            session.add(obj)
            session.commit()
            return obj

    def sql_query(self, query, params=None, single=True, is_commit=False):
        with Session(self.__engine, expire_on_commit=True, autocommit=False,
                     autoflush=True) as session:
            result = session.execute(query, params)
            if is_commit:
                session.commit()
            obj = result.scalar() if single else result.scalars().all()
            return obj


db = Database(db_url=settings.db_url)
db.connect()
#
#
#
# word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
#
# response = requests.get(word_site)
# WORDS = response.content.splitlines()
#
# for word in WORDS:
#     word_str = word.decode(encoding="utf-8")
#     db.create_object(Word(eng_name=word_str, ru_name=translate_text(word_str)))