from flask import Flask, request    
app = Flask(__name__)       

@app.route('/')
def index():
    return '<h1>これは掲示板のトップページです</h1>'        

@app.route('/write', methods=['GET', 'POST'])
def write():
    if request.method == 'GET':
        return """
            <html><body>
            <h1>これは掲示板の書き込みページです</h1>
            <h3>書き込み内容：</h3>
            <form action="/write" method="POST">
                <textarea name="msg" rows="5" cols="70"></textarea><br/><br/>
                <input type="submit" value="書き込む">
            </form>
            </body></html>             
        """
    elif request.method == 'POST':
        msg = request.form['msg']
        return f'<h1>書き込み内容：{msg} 受け付けました</h1>'

@app.route('/edit/<int:message_id>')
def edit(message_id):
    return f'<h1>これはID={message_id} を編集するページです</h1>'

if __name__ == '__main__':
    app.run(debug=True)