import json
from flask import Flask, request, jsonify
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "happy"}

db = MongoEngine(app)

from utils import shortcuts
from models import User, Job

@app.route("/")
def home():
    return jsonify({"content": "Welcome to our app."})

@app.route("/users/login", methods=["POST"])
def login():
    logged = False
    data = request.json

    if app.config["debug"]:
        logged = True
    elif persona.verify_assertion(data["assertion"], data["audience"]):
        if User.objects(email=data["audience"]):
            logged = True

    if logged:
        return jsonify({"content": "Logged in."})
    else:
        return shortcuts.abort(401, {"error": "Authentication failed."})

@app.route("/users/register", methods=["POST"])
def register():
    data = request.json
    if User.objects(email=data["email"]):
        return shortcuts.abort(409, {"error": "Email account already used."})
    else:
        user = User(email=data["email"])
        user.save()
        return jsonify(json.loads(user.to_json()))

@app.route("/jobs", methods=["POST"])
def new_job():
    #TODO: check if user is already in session
    data = request.json
    user = User.objects.get(email=data["email"])
    if not user:
        return shortcuts.abort(401, {"Authentication failed."})
    job = Job(user_id=user, 
        job_service=data["job_service"],
        job_action=data["job_action"],
        data=data["data"])
    job.save()
    return jsonify(json.loads(job.to_json()))

if __name__ == '__main__':
    app.run(debug=True)
