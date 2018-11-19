import db
from db import DatabaseConnection
conn = DatabaseConnection()
user = conn.user("TIMO")
print(user)
