import os
from pymongo import MongoClient

DB_chat = os.getenv('DB_paste_bin')
Data_base_name = "posts"


def mk_connection(collection_name):
    client = MongoClient(DB_chat)
    db = client[Data_base_name]
    return db[collection_name]


def get_full(tiny_url):
    collection = mk_connection('user_data')
    data = collection.find_one({'tiny_url': tiny_url})
    if data:
        return True, data['full_text']
    else:
        return False, None


def add_link_db(tiny_url, full_text):
    collection = mk_connection('user_data')
    collection.insert({'tiny_url': tiny_url, 'full_text': full_text})
    return None
