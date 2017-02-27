from flask import Flask, render_template

app = Flask(__name__)

#index page
@app.route('/')
@app.route('/<name>')
def index(name = None):
	return render_template('user.html', name = name)
	
names = ['Jesse', 'Samira', 'jon', 'Emily', 'Don']
@app.route('/users')
def users():
	return render_template('users.html', names = names)
	
app.run()