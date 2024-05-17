from flask import Flask
from database.database import db
from flask import jsonify, request
from database.models import User

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

import sys
if len(sys.argv) > 1 and sys.argv[1] == 'create_db':
    with app.app_context():
        db.create_all()
    print("Database created successfully")
    sys.exit(0)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/pedidos", methods=['GET'])
def get_pedidos():
    users = User.query.all()
    return_users = []
    for user in users:
        return_users.append(user.serialize())
    return jsonify(return_users)


@app.route("/novo", methods=['POST'])
def create_pedidos():
    data = request.json
    user = User(name=data["name"], item=data["item"], descricao=data["descricao"])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize())

@app.route("/pedidos/<int:id>", methods=["PUT"])
def update_user(id):
    data = request.json
    user = User.query.get(id)
    user.name = data["name"]
    user.item = data["item"]
    user.descricao = data["descicao"]
    db.session.commit()
    return jsonify(user.serialize())
