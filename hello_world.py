from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World People, Welcome to My Page"

@app.route('/about')
def about():
    return "The is the About Me"

if __name__ == '__main__':
    app.run(debug=True)