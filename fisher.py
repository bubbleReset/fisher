
from flask import Flask, make_response

app = Flask(__name__) 
app.config.from_object('config')


@app.route('/hello')
def hello():

    headers = {
        'content-type': 'text/palin',
        'location': 'http://www.bing.com'
    }
    response = make_response('<html></html>', 404)
    response.headers = headers
    return response
    # return '<html></html>', 301, headers


if __name__ == '__main__':

    app.run(host='0.0.0.0', port='8080', debug=app.config['DEBUG'])

    # SyntaxError: positional argument follows keyword argument
