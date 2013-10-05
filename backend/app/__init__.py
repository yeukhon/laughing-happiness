# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from flask import Flask, jsonify, request

from utils import shortcuts, persona

app = Flask(__name__)
app.config["debug"] = True

@app.route("/")
def home():
    return jsonify({"content": "Welcome to our app."})

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return jsonify({"content": "Login with a Persona email and assertion token."})

    data = request.json
    if app.config["debug"] or persona.verify_assertion(
            data["assertion"], data["audience"]):
        # add user to the session
        return jsonify({"content": "Logged in."})
    else:
        return shortcuts.abort(401, {"error": "Authentication failed."})

if __name__ == "__main__":
    app.run()
