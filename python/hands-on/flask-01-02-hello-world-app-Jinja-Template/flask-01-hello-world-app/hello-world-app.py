from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World from Flask!!!"

@app.route('/second')
def second():
    return "bize samsun!!"

@app.route('/third/subthird')
def third():
    return 'bu başka bir sayfa öyle böyle değil'

@app.route('/forth/<string:id>')
def forth(id):
    return f'bu nasıl birşeymiş yahu! {id}'











if __name__ == '__main__':
    app.run(debug=True, port=3000)