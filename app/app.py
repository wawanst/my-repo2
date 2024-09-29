# app.py
from flask import Flask
import os
import logging

app = Flask(__name__)

# Cek apakah file ada di lokasi yang benar
try:
    logging.info(f"Checking if /run/secrets/db_password exists: {os.path.exists('/run/secrets/db_password')}")
    logging.info(f"Checking if /run/secrets directory is readable: {os.access('/run/secrets', os.R_OK)}")
    with open('/run/secrets/db_password', 'r') as f:
        db_password = f.read().strip()
except FileNotFoundError:
    logging.error("/run/secrets/db_password not found!")
    db_password = 'File not found'
    
@app.route('/')
def hello():
    return f'Password: {db_password}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
