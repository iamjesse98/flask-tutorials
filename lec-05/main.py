from flask import Flask, render_template

app = Flask(__name__)

#index page
@app.route('/')
def index():
	return 'Hello from homepage'
	
@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name = name)
	
app.run()