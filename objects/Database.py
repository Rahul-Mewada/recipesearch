from config import Config
import mysql.connector

class Database:
    def __init__(self):
        self.db = mysql.connect(
            host = Config.DATABASE_CONFIG['server'],
            user = Config.DATABASE_CONFIG['user'],
            passwd = Config.DATABASE_CONFIG['password'],
            database = Config.DATABASE_CONFIG['name']
        )
        self.cursor = self.db.cursor()
        


