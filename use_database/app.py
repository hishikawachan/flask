from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app: Flask = Flask(__name__)
login_user_name: str = "osamu"

# データベースの設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.dqlite'
db = SQLAlchemy(app)
# メッセージのデータベースモデル
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    contents = db.Column(db.String(150), nullable=False)
    #timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.route("/")
def index():
    search_word: str = request.args.get("search_word")
    if search_word is None:
        message_list: list[Message] = Message.query.all()
    else:
        # 検索ワードが指定されている場合、メッセージリストをフィルタリング
        message_list: list[Message] = Message.query.filter(Message.contents.like(f"%{search_word}%")).all()
    return render_template(
        "top.html",
        login_user_name=login_user_name,
        message_list=message_list,
        search_word=search_word,
    )
    
@app.route("/write", methods=["GET", "POST"])
def write():
    if request.method == "GET":
        return render_template("write.html", login_user_name=login_user_name)
    elif request.method == "POST":
        user_name = request.form["user_name"]
        contents = request.form["contents"]
        new_message = Message(user_name=user_name, contents=contents)
        db.session.add(new_message)
        db.session.commit()
        return redirect(url_for("index"))
    
#データベース初期化
with app.app_context():
    db.create_all() 

if __name__ == "__main__":
    app.run(debug=True)