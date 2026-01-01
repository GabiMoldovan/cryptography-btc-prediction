import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from threading import Lock
from contextlib import contextmanager

Base = declarative_base()

class Database:
    '''
    Class for managing database connections
    '''
    _instance = None
    _lock = Lock()
    _tables_created = False

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(Database, cls).__new__(cls)
                    cls._instance._init_engine()
        return cls._instance

    def _init_engine(self):
        load_dotenv()

        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        host = os.getenv("DB_HOST")
        port = os.getenv("DB_PORT")
        dbname = os.getenv("DB_NAME")

        self.engine = create_engine(
            f"postgresql+psycopg://{user}:{password}@{host}:{port}/{dbname}",
            echo=False,
            pool_size=5,
            max_overflow=10
        )

        self.SessionLocal = sessionmaker(bind=self.engine, expire_on_commit=False)

    def get_session(self):
        # Get a database session, ensuring tables are created first
        if not Database._tables_created:
            Base.metadata.create_all(self.engine)
            Database._tables_created = True
            print("Tables created/verified successfully!")
        return self.SessionLocal()

    @contextmanager
    def session(self):
        """
        Context manager that automatically closes the session.
        Also automatically rolls back on exception, and commits if successful.
        """
        session = self.get_session()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()