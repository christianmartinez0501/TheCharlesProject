from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='The Charles Project', heading='Welcome')


@app.route('/landing')
def landing():
    return render_template('landing.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
