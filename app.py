from flask import Flask, render_template, request
from github_utils import fetch_user_data


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    username = request.form['username']
    token = request.form.get('token', None)
    data = fetch_user_data(username, token)
    if not data:
        return render_template('index.html', error="GitHub user not found or API rate limited.")
    return render_template('result.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
