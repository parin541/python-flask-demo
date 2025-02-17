from flask import Flask

app = Flask(__name__)

from Sourcecode.app import routes
