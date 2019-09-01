from flask import Flask, url_for
from flask import  render_template
app = Flask(__name__)

@app.route('/funny')
def hello():
    return  '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">' 

@app.route('/usr/<name>')
def user_page(name):
    return 'User: %s' % name

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name='greyli'))
    print(url_for('user_page', name='peter'))
    print(url_for('test_url_for'))
    #print(url_for('test_url_for_te')) 会报错
    print(url_for('test_url_for', num=2))
    return 'Test page'

# 处理 404 异常
# @app.errorhandler(404)
# def error_404(e):
#     return '404 Error', 404

# 对错误进行分类处理
from werkzeug.exceptions import HTTPException

@app.errorhandler(Exception)
def all_exception_handler(e):
    if isinstance(e, HTTPException):
        return e.description, e.code
    return 'Error', 500


name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

@app.route('/')
def index():
    print("我的替他那")
    return render_template('index.html', name=name, movies=movies)

