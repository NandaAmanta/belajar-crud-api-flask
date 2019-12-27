from flask import Flask,render_template,jsonify
from models.user import initialize
import models

#blueprint
from resources_api.user import users_api
from routes.route import route

app     = Flask(__name__)

app.register_blueprint(users_api)
app.register_blueprint(route)





if __name__ == "__main__":
    initialize()
    app.run(debug=True)