import os
from dotenv import load_dotenv

load_dotenv()

def env_run():
    if "URL_ENV" in os.environ:
        url = os.environ["URL_ENV"]
    else:
        url = str(os.getenv("URL_ENV"))
    return url

def env_username():
    if "USER_MAIL" in os.environ:
        username = os.environ["USER_MAIL"]
    else:
        username = str(os.getenv("USER_MAIL"))
    return username

def env_password():
    if "PASSWORD" in os.environ:
        password = os.environ["PASSWORD"]
    else:
        password = str(os.getenv("PASSWORD"))
    return password
