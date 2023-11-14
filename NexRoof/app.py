from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
def products():
    stone_coat_data = []
    Colored_data = []

    return render_template('products.html', products=product_data) 