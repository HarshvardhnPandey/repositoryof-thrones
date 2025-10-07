import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route → login page
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # You can add login logic here
        if username == "admin" and password == "admin":  # example
            return redirect(url_for("meme_page"))
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

# Meme page route
@app.route("/memes")
def meme_page():
    # Example: you can pass a list of memes to display
    memes = ["meme1.jpg", "meme2.jpg", "meme3.jpg"]
    return render_template("meme.html", memes=memes)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render dynamic port
    app.run(host="0.0.0.0", port=port)
