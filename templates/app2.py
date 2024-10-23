from flask import Flask, render_template

app = Flask(__name__)

max_score = 100
test_name = "Python Challenge"
students = [
  {"name": "Vlad", "job": "junior python developer"},
]

@app.get("/results/")
def results():
    context = {
        "title": "Results",
        "students": students,
        "test_name": test_name,
        "max_score": max_score,
    }
    return render_template("results.html", **context)

@app.get("/portpholio/")
def portpholio():
    context1 = {
        "Телеграм-бот": telegram_bot,
        "Game": game,
        "сайт": 2023
    }
    return render_template("results.html", **context1)
@app.get("/")

@app.get("/")
def index():
    return render_template("index3.html",
                           title="Flask and Djinja",
                           info="I learn IT skills"
                           )

if __name__ == '__main__':
    app.run(port=5001, debug=True)