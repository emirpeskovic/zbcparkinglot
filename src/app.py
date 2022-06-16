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
        return render_template("page.html")
    elif request.method == "POST":
        return render_template("page.html", other_page="components/confirm.html")


@app.route("/register")
def register_route():
    return render_template("page.html", other_page="components/register.html")


@app.route("/users")
def users_route():
    return render_template("page.html", other_page="components/admin/users.html")


@app.route("/parking-history")
def parking_history_route():
    return render_template("page.html", other_page="components/user/parking-history.html")


@app.route("/contact-us")
def contact_route():
    return render_template("page.html", other_page="components/contact-us.html")


@app.route("/user-profile")
def user_profile_route():
    return render_template("page.html", other_page="components/user/user-profile.html")


@app.route("/user-payment")
def user_payment_route():
    return render_template("page.html", other_page="components/user/user-payment-html")


@app.route("/user-parking-lot")
def user_parking_route():
    return render_template("page.html", other_page="components/user/user-parking-lot.html")


@app.route("/car-reg")
def car_route():
    return render_template("page.html", other_page="components/car-reg.html")


@app.route("/dashboard")
def dashboard():
    return render_template("page.html", other_page="components/admin/dashboard.html")


@app.route("/users/add")
def add_user():
    user = User(name="John", address="123 Main St.", email="john@4d2oe.com", phone_number="1233678")
    res = database_manager.save(user)
    if res is True:
        return "User added successfully"
    else:
        return "User not added"


@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin.html", other_page="components/admin/dashboard.html")


@app.route("/user")
def get_all_users():
    users = database_manager.get_all(User)
    return render_template("users.html", users=users)


app.run(debug=True)
