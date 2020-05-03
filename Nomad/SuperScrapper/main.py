from flask import Flask, render_template

app = Flask("Super Scrapper")


@app.route("/")
def home():
    return render_template("potato.html")

# 연습용
# @app.route("/")
# def home():
#     return "Hello! Welcome to mi case!"

# @app.route("/contact")
# def contact():
#     return "Contact me!"

# @app.route("/<username>")  # 인스타그램 같은
# def dynamicURL(username):
#     return f"Hello {username}, how are you doing"


app.run(host="127.0.0.1", port=3000)
