from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home/")
def home():
    return render_template('index.html')

@app.get('/order/')
def order():
    pizzas = [
        {
            'name': 'Папероні',
            'description': 'Класична піца з тонкими шматочками пікантної ковбаски папероні, соусом з томатів та сиром моцарела. Ідеальний вибір для любителів гострих страв!',
            'price': 29.99,
            'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Pepperoni_pizza.jpg/330px-Pepperoni_pizza.jpg'
        },
        {
            'name': 'Чотири сири',
            'description': 'Вишукана піца з чотирма видами сиру: моцарела, горгонзола, пармезан та ементаль. Справжнє свято для гурманів!',
            'price': 39.99,
            'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Pizza_quattro_formaggi_at_restaurant%2C_Chalk_Farm_Road%2C_London.jpg/330px-Pizza_quattro_formaggi_at_restaurant%2C_Chalk_Farm_Road%2C_London.jpg'
        },
        {
            'name': 'Маргарита',
            'description': 'Проста і смачна піца з томатним соусом, моцарелою та свіжим базиліком. Ідеальний вибір для тих, хто любить класику!',
            'price': 24.99,
            'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Pizza_Margherita_stu_spivack.jpg/411px-Pizza_Margherita_stu_spivack.jpg'
        },
        {
            'name': 'Гавайська',
            'description': 'Піца з ароматною шинкою, ананасами та моцарелою. Солодке та солоне поєднання для незвичайного смаку!',
            'price': 32.99,
            'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Pizza_Hawaii_02.jpg/330px-Pizza_Hawaii_02.jpg'
        }
    ]

    return render_template('order.html', pizzas=pizzas)

if __name__ == '__main__':
    app.run(port=6969, debug=True)