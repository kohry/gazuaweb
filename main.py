from flask import Flask
from flask import render_template
app = Flask(__name__)

import exchange

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exchange/')
def getExchangeRate():
    exchange.getExchangeRate()

    return render_template('index.html')



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5882)