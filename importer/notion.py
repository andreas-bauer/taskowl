import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

NOTION_KEY = os.getenv('NOTION_KEY', '')
NOTION_DATABASE_ID = os.getenv('NOTION_DATABASE_ID', '')

headers = {
    "Authorization": "Bearer " + NOTION_KEY,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}


def get_users(headers):
    url = 'https://api.notion.com/v1/users'
    res = requests.request("GET", url, headers=headers)
    print(res.status_code)
    print(res.json())


def get_db(database, headers):
    url = 'https://api.notion.com/v1/databases/' + database
    res = requests.request("GET", url, headers=headers)
    print(json.dumps(res.json(), indent=2))


get_db(NOTION_DATABASE_ID, headers)
