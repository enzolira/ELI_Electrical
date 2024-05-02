from flask import Flask
from src import app
from src.controllers import loadbox
from src.controllers import users
from src.controllers import planning

if __name__ == "__main__":
    app.run(debug=True)
