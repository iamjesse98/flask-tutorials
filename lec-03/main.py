from flask import Flask

app = Flask(__name__)

#index page
@app.route('/')
def index():
	return 'Hello from homepage'
	
#localhost:5000/user/name	
@app.route('/user/<username>')
def user(username):
	return '<h2>Hello, {}</h2>'.format(username)
	
app.run()