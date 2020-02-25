# import flask
from flask import Flask
import models
# import our resources
from resources.users import users
from resources.items import items
from resources.comments import comments
# this is the main tool for coordinating the login/session
from flask_login import LoginManager



DEBUG = True # print the error
PORT = 8000 






app = Flask(__name__)

# set up a secret key
app.secret_key = "This is a secret key. It says that we needed a secret key"

# instantiate LoginManager to a login_manager
login_manager = LoginManager()

# connect the app with login_manager
login_manager.init_app(app)

# user loader will use this callback to load the user object
@login_manager.user_loader
def load_user(user_id):
	try:
		# look up user
		return models.User.get(models.User.id == user_id)
	except models.DoesNotExist:
		return None

# use the blueprint that will handle the users stuff
app.register_blueprint(users, url_prefix='/api/v1/users/')
app.register_blueprint(items, url_prefix='/api/v1/items/')
app.register_blueprint(comments, url_prefix='/api/v1/comments/')




if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT) 