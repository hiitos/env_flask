from sqlalchemy import Column, Integer, String, DateTime, Sequence
from datetime import datetime
from test_db_setting import engine,Base

class User(Base):
    """
    UserModel
    """
    __tablename__ = 'users'
    __table_args__ = {
        'comment': 'ユーザー情報のマスターテーブル'
    }
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(200))
    age = Column('age', Integer)
    email = Column('email', String(100))
    created_at = Column('created', DateTime, default=datetime.now, nullable=False)
    updated_at = Column('modified', DateTime, default=datetime.now, nullable=False)

class AppLog(Base):
    """
    AppLogModel
    """
    __tablename__ = 'logs'
    __table_args__ = {
        'comment': 'アプリのログテーブル'
    }
    log_id = Column('id', Integer, primary_key=True, autoincrement=True)
    user_id = Column('user_id', Integer)
    event_id = Column('event_id', Integer)
    created_at = Column('created', DateTime, default=datetime.now, nullable=False)
