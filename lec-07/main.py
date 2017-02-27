from flask import Flask, render_template

app = Flask(__name__)

#index page
@app.route('/')
@app.route('/<name>')
def index(name = None):
	return render_template('user.html', name = name)
	
app.run()