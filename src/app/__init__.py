from flask import Flask

app = Flask(__name__)

from src.app import routes
