from flask import Flask
from src import app
from src.controllers import loadbox
from src.controllers import users
from src.controllers import report

app.config["SECRET_KEY"] = "wedefergewvgetrgw492890348t2vnwc"
app.config["SECRET_SALT"] = "mkonjibhu65544321"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int("4000"))
