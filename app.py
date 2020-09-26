from flask import Flask
app = Flask(__name__)

online = None

@app.route("/")
def index():
    global online
    if (online is None):
        path = "onoff.svg"
    elif (online):
        path = "on.svg"
    else:
        path = "off.svg"
    return app.send_static_file(path)

@app.route("/toggle")
def toggle():
    global online
    if online:
        online = False
    else:
        online = True
    return str(online)

