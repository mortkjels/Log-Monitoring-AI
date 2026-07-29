import os
from dotenv import load_dotenv
from google.genai import Client
from pathlib import Path
from bs4 import BeautifulSoup


BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

API_KEY = os.getenv("API_KEY")

def get_client():

    



    answer = "!"
    return answer