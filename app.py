import random
from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'secret_key'


@app.route('/', methods=['GET', 'POST'])
def index():
    rand = (random.sample(range(1, 50), 6))
    list = (rand)
    list_loss = []
    x = 1
    list_cor = 0
    selected_numbers = []

    if request.method == 'POST':
        for i in range(1, 7):
            number = int(request.form['number{}'.format(i)])
            selected_numbers.append(number)
            if number in list:
                list_cor += 1
                list_loss.append(number)

    return render_template('index.html', list_loss=list_loss, list=list, list_cor=list_cor, selected_numbers=selected_numbers)


if __name__ == '__main__':
    app.run(debug=True)
