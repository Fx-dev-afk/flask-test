from flask import Flask, render_template, url_for

app = Flask(__name__)

menu = ['О нас', 'Загрузка', 'Поддержка']

@app.route('/')
def index():
    return render_template('index.html', title = 'Главная страница', menu = menu)

@app.route('/about')
def about():
    return render_template('about.html', title = 'О нас', menu = menu)

@app.route('/profile/<string:username>')
def profile(username):
    return f'Пользователь: {username}'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('about'))
    print(url_for('profile', username = 'test'))

if __name__ == '__main__':
    app.run(debug = True)