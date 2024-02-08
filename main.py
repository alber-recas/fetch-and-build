from flask import Flask, send_file
from flask import request
import controller

app = Flask(__name__)


@app.route("/compile", methods=["GET"])
def compile():
    repo_url = request.args.get("repo_url")

    if repo_url == None:
        return "Missing repo_url request parameter", 400

    filename = controller.get_and_build_repository(repo_url)

    if not filename:
        return "Impossible to build the project", 500

    return send_file(filename, as_attachment=True)
