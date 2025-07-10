from dotenv import load_dotenv
load_dotenv()

import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://python-flask-blog:python-flask-blog@localhost:5432/python-flask-blog-db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
