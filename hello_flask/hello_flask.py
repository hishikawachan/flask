from flask import Flask
app: Flask = Flask(__name__)

@app.route('/')
def hello_world():
    age: int = 30
    return '<h1>Hello,' + str(age) +  'World!<h1>'

if __name__ == '__main__':
    app.run(debug=True)