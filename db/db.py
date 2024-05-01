from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from .models import Base
import os

class Database:
    def __init__(self, database_url):
        self.engine = create_engine(database_url)
        self.Session = sessionmaker(bind=self.engine)
        self.connect = self.check_connection()

    def get_session(self):
        return self.Session()

    def initialize_database(self):
        if not database_exists(self.engine.url):
            create_database(self.engine.url)
        Base.metadata.create_all(bind=self.engine)
        
    def check_connection(self):
        try:
            with self.engine.connect():
                return True
        except:
            return False
