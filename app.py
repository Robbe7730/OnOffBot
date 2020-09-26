from flask import Flask, request, render_template
app = Flask(__name__)

online = None
username = ""

@app.route("/", methods = ["GET", "POST"])
def index():
    global online
    global username
    if request.method == "GET":
        if (online is None):
            path = "onoff.svg"
        elif (online):
            path = "on.svg"
        else:
            path = "off.svg"
        return render_template(path, username=username)
    elif request.method == "POST":
        data = request.json
        if "trigger_word" not in data:
            return "no trigger word found"
        if "user_name" not in data:
            return "no username found"
        username = data["user_name"]
        if data["trigger_word"].lower() == "on":
            online = True
        if data["trigger_word"].lower() == "off":
            online = False
        return str("online")

@app.route("/toggle")
def toggle():
    global online
    global username
    if online:
        online = False
        username = "onbekend"
    else:
        online = True
        username = "onbekend"
    return str(online)

