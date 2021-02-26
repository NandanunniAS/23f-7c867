from flask import Flask, request, render_template
from fcloud import Friday

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def bot():
    if request.method == "POST":
        Friday.listen(request.form["msg"])
        return {"reply": Friday.reply().replace("[newline]", "<br />")}
    else:
        return render_template("friday.html")


if __name__ == "__main__":
    app.run()
