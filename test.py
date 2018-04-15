from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

import migrate
from migrate import Message

DBSession = sessionmaker(bind=migrate.engine)
session = DBSession()

for msg in session.query(Message).filter(Message.chat_id == 88376478):
    print(msg.id, msg.message)

#


