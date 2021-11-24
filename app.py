"""
app: the flask app serving the svg and recieving webhooks
"""
import configparser

from flask import Flask, request, render_template
app = Flask(__name__)

config = configparser.ConfigParser()
config.read('secrets.ini')

ONLINE = None
TOKEN = config['secrets']['webhook_token']


@app.route("/", methods=["GET", "POST"])
def index():
    """
    index: show the on/off/onoff svg depending on the current status
    """
    global ONLINE
    if request.method == "GET":
        # Return the correct svg
        if ONLINE is None:
            path = "onoff.svg"
        elif ONLINE:
            path = "on.svg"
        else:
            path = "off.svg"

        return render_template(path)
    if request.method == "POST":
        # Get the POST-ed data
        data = request.json

        # Make sure the right fields exist
        if ("trigger_word" not in data or
                "user_name" not in data or
                "token" not in data):
            return "Missing some fields", 400

        # Make sure the token matches
        if data["token"] != TOKEN:
            return "Invalid token", 401

        # Set the status
        if data["trigger_word"].lower() in ["on", "aan"]:
            ONLINE = True
        if data["trigger_word"].lower() in ["off", "uit"]:
            ONLINE = False

        # Return the new status (unused by Mattermost)
        return str(ONLINE)
    return "This shouldn't be possible...", 400


@app.route("/toggle")
def toggle():
    """
    toggle: for debugging only, toggles the on/off state
    """
    global ONLINE
    if ONLINE:
        ONLINE = False
    else:
        ONLINE = True
    return str(ONLINE)
