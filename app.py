import os
from flask import Flask, render_template, request, redirect, url_for

# Create the Flask app
app = Flask(__name__)

# -------------------------------
# Login Page Route
# -------------------------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Simple example login check (you can connect DB later)
        if username == "admin" and password == "admin":
            return redirect(url_for("meme_page"))
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")


# -------------------------------
# Meme Page Route
# -------------------------------
@app.route("/memes")
def meme_page():
    # Render meme.html that shows your meme video
    return render_template("meme.html")


# -------------------------------
# Logout Route
# -------------------------------
@app.route("/logout")
def logout():
    # Redirect back to login page
    return redirect(url_for("login"))


# -------------------------------
# Run the app (Render compatible)
# -------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render provides PORT dynamically
    app.run(host="0.0.0.0", port=port)
