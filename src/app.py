from flask import Flask, render_template, request, jsonify, session

from car import Car
from database_manager import DatabaseManager
from manager import Manager
from user import User

app = Flask(__name__, template_folder="../templates", static_folder="../assets")
app.secret_key = b'_5#y2L"FgTK9T30293124Q8z\n\126P5HL4YK7x\\ec]/'

database_manager = DatabaseManager()
main_manager = Manager()


@app.route("/", methods=["GET"])
@app.route("/login", methods=["POST"])
def index():
    if request.method == "GET":
        return render_template("page.html")
    elif request.method == "POST":
        if "phone" in request.form:
            phone = request.form["phone"]

            if not phone.isdigit():
                return jsonify({"status": "error", "message": "Phone number must be digits"}), 400

            if len(phone) != 8:
                return jsonify({"status": "error", "message": "Phone number must be 8 digits"}), 400

            session["phone"] = phone

            user = database_manager.get(User, User.phone_number == phone)
            if user is None:
                return jsonify({"status": "register"}), 201
            else:
                return jsonify({"status": "success"}), 200
        else:
            return jsonify({"status": "error"}), 400  # 400 means a bad request


@app.route("/register/car")
def register_car():
    if request.method == "GET":
        return render_template("page.html", other_page="components/register-car.html")
    elif request.method == "POST":
        if "license" in request.form:
            car_license = request.form["license"]

            session["license"] = car_license

            car = database_manager.get(Car, Car.license_plate == car_license)
            if car is None:
                user = database_manager.get(User, User.phone_number == "12457889")
                if user:
                    car = Car(license_plate=car_license, owner=user.id)
                    database_manager.save(car)
                    return jsonify({"status": "success"}), 201
            else:
                return jsonify({"status": "error"}), 400


@app.route("/login/confirm")
def confirm():
    return render_template("page.html", other_page="components/confirm.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("page.html", other_page="components/register.html")
    elif request.method == "POST":
        if "name" in request.form:
            name = request.form["name"]
            address = request.form["address"]
            email = request.form["email"]
            phone_number = request.form["phone_number"]

            session["name"] = name
            session["address"] = address
            session["email"] = email
            session["phone_number"] = phone_number

            user = User(phone_number=phone_number, name=name, address=address, email=email)
            database_manager.save(user)


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
    return render_template('page.html', other_page="components/user/user-profile.html")


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


@app.route("/test")
def test():
    user = database_manager.get(User, User.phone_number == "12345678")

    if user:
        car = Car(license_plate="g", owner=user.id)
        database_manager.save(car)
        return "fedt"
    else:
        return "nej ikke fedt"


app.run(debug=True)
