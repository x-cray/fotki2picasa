from google.appengine.ext import webapp
from google.appengine.api import users
from appengine_utilities.sessions import Session
from data import *

application_key_yandex = "afe8ed20da74460bb4c410074791c100"
application_key_google = "ExGxaCOrlEDbc0Dj5kKA"
application_secret_google = "Tc5bhNLVkTF8LTiUbAdgLOXkus62QxJiYioqMKxmGI"

# In the real world, you'd want to edit this callback URL to point to your
# production server. This is where the user is sent to after they have
# authenticated with Twitter. 
callback_url = "https://fotki2picasa.appspot.com/verify"

# Test data.
#session["logged_user"] = UserInfo.get_or_insert(
#	"x_cray",
#	name="Denis Parchenko",
#	picture="http://a0.twimg.com/profile_images/1279535592/0_4c987_235e6f74_orig_normal.jpeg",
#	follow_account="",
#	needed_count=1000
#)

class BasicHandler(webapp.RequestHandler):
	def load_user(self):
		self.session = Session(writer="cookie")
		self.logged_user = None
		if "username" in self.session:
			self.logged_user = UserInfo.get_by_key_name(self.session["username"])
