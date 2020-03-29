import os

from dotenv import load_dotenv


load_dotenv()
try:
    BOT_TOKEN = os.environ["MOCKINGBIRD_BOT_TOKEN"]
except KeyError:
    raise AssertionError(
        "MOCKINGBIRD_BOT_TOKEN env variable has not been set. Is your local .env file configured correctly?"
    )
