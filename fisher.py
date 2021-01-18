
from flask import Flask, make_response

app = Flask(__name__) 
app.config.from_object('config')


@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
        q: 普通关键字 或者 isbn
        page
    """
    # isbn isbn13 13个0到9的数字组成
    # isbn10 10个0到9的数字组成，含有一些 ' - '
    isbn_or_key = 'key'
    if len(q) == 13 and q.isdigit():
        isbn_or_key = 'isbn' 
    short_q = q.replace('-', '')
    if '-' in q and len(short_q) == 0 and short_q.isdigit():
        isbn_or_key = 'isbn' 

    pass


if __name__ == '__main__':

    app.run(host='0.0.0.0', port='8080', debug=app.config['DEBUG'])

    # SyntaxError: positional argument follows keyword argument
