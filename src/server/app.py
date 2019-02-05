from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/products/<id>')
def products(id):
    return f"Hello, World!{id}"

if __name__ == '__main__':
    app.run(debug=True)