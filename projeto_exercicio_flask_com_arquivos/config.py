import os
import secrets

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = secrets.token_hex(16)
    JSON_STORAGE_FILE = os.path.join(basedir, 'app', 'data', 'storage.json')