from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Hardcoded username and password
    hardcoded_username = 'getser'
    hardcoded_password = '123456'

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == hardcoded_username and password == hardcoded_password:
            return 'Login successful!'
        else:
            return 'Invalid credentials, please try again.'

    return '''
        <form method="post">
            Username: <input type="text" name="username" value="getser"><br>
            Password: <input type="password" name="password" value="123456"><br>
            <input type="submit" value="Login">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
