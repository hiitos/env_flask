import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import desc
from dotenv import load_dotenv
load_dotenv()

# ローカル用のDB設定
DB_CONNECT_URL = 'sqlite:///db.sqlite3'

# engineの設定 接続用のインスタンスを作成（create_engine関数がEngineインスタンスを返す）
engine = create_engine(DB_CONNECT_URL,echo=True)

# DBに対してORM操作するときに利用
# Sessionを通じて操作を行う
session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

# 各modelで利用
# classとDBをMapping
Base = declarative_base()
