from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
SECRET_AUTH = os.environ.get("SECRET_AUTH")