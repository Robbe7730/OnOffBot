from flask import Flask, request
app = Flask(__name__)

online = None

@app.route("/", methods = ["GET", "POST"])
def index():
    global online
    if request.method == "GET":
        if (online is None):
            path = "onoff.svg"
        elif (online):
            path = "on.svg"
        else:
            path = "off.svg"
        return app.send_static_file(path)
    elif request.method == "POST":
        data = request.json()
        if "trigger_word" not in data:
            return "no trigger word found"
        if data["trigger_word"].lower() == "on":
            online = True
        if data["trigger_word"].lower() == "off":
            online = False
        return str("online")

@app.route("/toggle")
def toggle():
    global online
    if online:
        online = False
    else:
        online = True
    return str(online)

