from flask import Flask

name = Flask(__name__)

@name.route('/')
def name_is():
    return "My name is Linnea"