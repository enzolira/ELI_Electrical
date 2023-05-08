from flask import Flask
from src import app

from src.controllers import loadbox
from src.controllers import users


if __name__=="__main__":
    app.run(debug=True)