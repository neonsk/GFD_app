from flask import Flask, render_template, request

app = Flask(__name__)

#最初に表示される画面
@app.route('/')
def index():
    return render_template('first_app.html')

#submitされた際に表示される画面
@app.route('/confirm', methods = ['POST', 'GET'])
def confirm():
    if request.method == 'POST':
        result = request.form["Name"]
    print(result)
    return render_template("confirm.html",result = result)

if __name__ == '__main__':
    app.run()
    