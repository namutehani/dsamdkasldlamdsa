
#url  = "mongodb+srv://odin12:silik10vadisi@cluster0.uvxro.mongodb.net/cluster0?retryWrites=true&w=majority"
url = "mongodb+srv://odij:silik10vadisi@cluster0.ohccr.mongodb.net/cluster0?retryWrites=true&w=majority
import datetime
import motor.motor_asyncio

class Database:
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users

    def new_user(self, id):
        return dict(
            id=id,
            join_date=datetime.date.today().isoformat(),
        )

    async def add_user(self, id):
        user = self.new_user(id)
        await self.col.insert_one(user)

    async def is_user_exist(self, id):
        user = await self.col.find_one({'id': int(id)})
        return bool(user)

    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self):
        return self.col.find({})

    async def delete_user(self, user_id):
        await self.col.delete_many({'id': int(user_id)})

    async def get_user_data(self, id) -> dict:
        user = await self.col.find_one({'id': int(id)})
        return user or None

#------------------------------#
q="""
import os
import threading
from sqlalchemy import create_engine
from sqlalchemy import Column, TEXT, Numeric
from sqlalchemy.ext.declarative import declarative_base
from config import DB_URI
from sqlalchemy.orm import sessionmaker, scoped_session

def start() -> scoped_session:
    engine = create_engine(DB_URI, client_encoding="utf8")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start()

INSERTION_LOCK = threading.RLock()

class Broadcast(BASE):
    __tablename__ = "broadcast"
    id = Column(Numeric, primary_key=True)
    user_name = Column(TEXT)

    def __init__(self, id, user_name):
        self.id = id
        self.user_name = user_name

Broadcast.__table__.create(checkfirst=True)


#  Add user details -
async def add_user(id, user_name):
    with INSERTION_LOCK:
        msg = SESSION.query(Broadcast).get(id)
        if not msg:
            usr = Broadcast(id, user_name)
            SESSION.add(usr)
            SESSION.commit()
        else:
            pass
          
async def full_userbase():
    users = SESSION.query(Broadcast).all()
    SESSION.close()
    return users

async def query_msg():
    try:
        query = SESSION.query(Broadcast.id).order_by(Broadcast.id)
        return query
    finally:
        SESSION.close()
"""
