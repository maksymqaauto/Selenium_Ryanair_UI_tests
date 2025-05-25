import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
APP_STORE_URL = os.getenv("APP_STORE_URL")
USER_1 = os.getenv("USER_1")
PASS_1 = os.getenv("PASS_1")
USER_2 = os.getenv("USER_2")
PASS_2 = os.getenv("PASS_2")

invalid_creds = [
        (os.getenv("USER_2"), os.getenv("PASS_2")),
        (os.getenv("USER_3"), os.getenv("PASS_3")),
]
