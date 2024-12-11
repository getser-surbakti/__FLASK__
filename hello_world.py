<<<<<<< HEAD
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World People 321, Welcome to My Page"

@app.route('/about')
def about():
    return "The is the About Me"

if __name__ == '__main__':
=======
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World, Welcome to My Page"

@app.route('/about')
def about():
    return "The is the About Me"

if __name__ == '__main__':
>>>>>>> df114bc1f07e8af31ff33606e8d1bfedec812ab2
    app.run(debug=True)