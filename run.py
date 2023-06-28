from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Юля, я тебя люблю. Попой не тарахти')

if __name__ == '__main__':
    app.run(debug=True, port=5656)

