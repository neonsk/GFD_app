from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('first_app.html')

@app.route('/confirm', methods = ['POST', 'GET'])
def confirm():
    if request.method == 'POST':
        result = request.form.getlist("name")
    return render_template("confirm.html",result = result)

if __name__ == '__main__':
    app.run()
    