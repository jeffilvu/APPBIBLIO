#API - lugar para disponibilizar recursos ou funcionalidades

# objetivo -- criar uma api que disponibiliza a consulta, criaçao, ediçao e exclusao de livros
# url Base -- localhost.com
# endpoint
    # -localhost/livros (get)
    # -localhost/livros (post)
    # -localhost/livros/id(get)
    # -localhost/livro/id(put)
    # -localhost/livro/id(DELETE)
# quais recursos - LIVROS

import os
from flask import Flask
from flask_cors import CORS
from extensions import db
from routes import init_routes

app = Flask(__name__)
CORS(app)


base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, 'instance', 'database.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path


db.init_app(app)
init_routes(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
    app.run(port=5000, host='localhost', debug=True)