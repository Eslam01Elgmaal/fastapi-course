import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



SQLALCHEMY_DATABASE_URL = "postgresql://neondb_owner:npg_J4aiUvQrkIE9@ep-fancy-surf-b1pba6h6-pooler.c-5.eu-central-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)




# SQLALCHEMY_DATABASE_URL = os.getenv(
#     "DATABASE_URL",
#     "sqlite:///./todoapp.db"
# )
#
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL,
#     connect_args={"check_same_thread": False})


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()