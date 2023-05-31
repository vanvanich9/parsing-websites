from dotenv import load_dotenv
import os

load_dotenv()

JWT_SECRET = os.getenv('JWT_SECRET')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')
TESTING_TOKEN = os.getenv('TESTING_TOKEN')
