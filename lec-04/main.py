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
	
#localhost:5000/post/number
@app.route('/post/<int:post_id>')
def post(post_id):
	return '<h3>the post id is: {}</h3>'.format(post_id)

app.run()