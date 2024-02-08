# Fetch and build

This project is a Server that fecthes a Git repository, builds the repository using CMake and returns the built project.

It depends on the following Python packages:

* [Flask](https://flask.palletsprojects.com/en/3.0.x/)
* [GitPython](https://gitpython.readthedocs.io/en/stable/intro.html)

It is highly recommended to build a Virtual Environment before installing this Python dependencies.

## Starting the server

To start the Flask server, run the following command:

`flask --app main.py run`

This command will launch the server listening in `127.0.0.1:5000`

## Send a query to build a project

As this project is quite simple. It only has one working endpoint `127.0.0.1:5000/compile` . To build a project just send a GET message using a `repo_url` parameter e.g:

`http://127.0.0.1:5000/compile?repo_url=https://github.com/alber-recas/cmake-basic-example`
