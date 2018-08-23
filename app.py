from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
	
	
	
	
	
@app.route('/user2/<name>')
def user2(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run()
