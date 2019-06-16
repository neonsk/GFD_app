from flask import Flask, render_template, request
import main

app = Flask(__name__)

#最初に表示される画面
@app.route('/')
def index():
    return render_template('first_app.html')

#submitされた際に表示される画面
@app.route('/confirm', methods = ['POST', 'GET'])
def confirm():
    if request.method == 'POST':
        text = request.form["Name"]
        print(text)

        mecab = main.mecab()
        result = mecab.execute(text)
        print(result)
    
    return render_template("confirm.html", text = text, result = result)

if __name__ == '__main__':
    app.run()
    