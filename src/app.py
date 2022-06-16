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
def register():
    return render_template("page.html", other_page="components/register.html")


@app.route("/register/car")
def register_car():
    return render_template("page.html", other_page="components/register-car.html")


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
    return render_template("page.html", other_page="components/user/user-payment.html")


@app.route("/user-parking-lot")
def user_parking_route():
    return render_template("page.html", other_page="components/user/user-parking-lot.html")


@app.route("/dashboard")
def dashboard():
    return render_template("page.html", other_page="components/admin/dashboard.html")


@app.route("/admin")
@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin.html", other_page="components/admin/dashboard.html")


app.run(debug=True)
