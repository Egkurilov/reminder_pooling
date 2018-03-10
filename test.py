from main import session
from migrate import Message

for row in session.query(Message.id).all():
    print(row.id)
