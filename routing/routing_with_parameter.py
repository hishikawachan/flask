from flask import Flask
app = Flask(__name__)  

@app.route('/')
def index():
    return '<h1>これは掲示板のトップページです</h1>'

@app.route('/write')
def write():
    return '<h1>掲示板の書き込むページです</h1>'

@app.route('/edit/<message_id>') 
def edit(message_id):
    #return f'<h1>掲示板のメッセージ {message_id} を編集するページです</h1>'
    return f'<h1>message_idは{type(message_id).__name__}型です</h1>'

if __name__ == '__main__':
    app.run(debug=True) 