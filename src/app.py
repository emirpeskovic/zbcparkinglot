from flask import Flask, render_template, request
from database_manager import DatabaseManager
from manager import Manager
from user import User

app = Flask(__name__, template_folder="../templates", static_folder="../assets")

database_manager = DatabaseManager()
main_manager = Manager()


@app.route("/", methods=["GET"])
@app.route("/login", methods=["POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", test=True)
    elif request.method == "POST":
        return render_template("components/confirm.html", test=False)


@app.route("/register")
def patter():
    return render_template("etellerandet.html")


@app.route("/test")
@app.route("/test/<name>")
def test(name=None):
    return render_template("test.html", name=name)


@app.route("/users/add")
def add_user():
    user = User(name="John", address="123 Main St.", email="john@4d2oe.com", phone_number="1233678")
    res = database_manager.save(user)
    if res is True:
        return "User added successfully"
    else:
        return "User not added"


@app.route("/user")
def get_all_users():
    users = database_manager.get_all(User)
    return render_template("users.html", users=users)


app.run(debug=True)
