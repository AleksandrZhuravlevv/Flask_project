from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Юля, я тебя люблю. Попой не тарахти')

@app.route('/aaa')
def aaa():
    return render_template('aaa.html')

@app.route('/bbb')
def bbb():
    return render_template('bbb.html')

@app.route('/ccc')
def ccc():
    return render_template('ccc.html')

@app.route('/ddd')
def ddd():
    return render_template('ddd.html')
@app.route('/eee')
def eee():
    return render_template('eee.html')
@app.route('/fff')
def fff():
    return render_template('fff.html')


if __name__ == '__main__':
    app.run(debug=True, port=5656)

