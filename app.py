from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

DATA_FILE = "data.json"


# -------- UTILIDADES PARA LEER Y GUARDAR -------- #
def load_contacts():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_contacts(contacts):
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=4)


# -------- RUTAS DEL CRUD -------- #

@app.route("/")
def index():
    contacts = load_contacts()
    return render_template("index.html", contacts=contacts)


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        contacts = load_contacts()
        new_contact = {
            "id": len(contacts) + 1,
            "name": request.form["name"],
            "phone": request.form["phone"],
            "email": request.form["email"]
        }
        contacts.append(new_contact)
        save_contacts(contacts)
        return redirect(url_for("index"))
    return render_template("create.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    contacts = load_contacts()
    contact = next((c for c in contacts if c["id"] == id), None)

    if request.method == "POST":
        contact["name"] = request.form["name"]
        contact["phone"] = request.form["phone"]
        contact["email"] = request.form["email"]
        save_contacts(contacts)
        return redirect(url_for("index"))

    return render_template("edit.html", contact=contact)


@app.route("/delete/<int:id>")
def delete(id):
    contacts = load_contacts()
    contacts = [c for c in contacts if c["id"] != id]
    save_contacts(contacts)
    return redirect(url_for("index"))


# -------- EJECUCIÓN -------- #
if __name__ == "__main__":
    app.run(debug=True)
