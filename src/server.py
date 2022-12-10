from flask import Flask
from bell import bell

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Returning the Bell's numbers!</p>"

@app.route('/bell/<string:cnt>')
def get_bell(cnt):
    try: 
        cnt = int(cnt)
    except Exception:
        return f"<p>Сам ты {cnt}<p>" 
    if cnt < 0:
        return "<p>Error 400<p>"
    bell_gen = bell()
    res = [next(bell_gen) for _ in range(cnt)]
    return res