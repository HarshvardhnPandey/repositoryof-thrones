from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecret"  # Needed for session management

# Dummy credentials
USERNAME = "admin"
PASSWORD = "123"
@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == USERNAME and password == PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("meme"))
        else:
            error = "Invalid credentials. Try again!"
    return render_template("login.html", error=error)

@app.route("/meme")
def meme():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("meme.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
