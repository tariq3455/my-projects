from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    return render_template('index.html', number1=2000, number2=4000)

@app.route('/multiple')
def number():
    var1, var2 = 34, 55
    return render_template('body.html', num1 = 34, num2 = 55, multiplication = var1*var2)


if __name__== '__main__':
    app.run(debug=True)