# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

To run this app you will also need to sign up for a trello account (https://trello.com/signup). By doing so you can then generate and API key and a token. You will need to add these as values in your `.env` file.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:

```bash
$ poetry run flask run
```

You should see output similar to the following:

```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```

Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running tests

Firstly install pytest as a dev dependency by running the following command:

```bash
$ poetry add pytest --dev
```

To add new tests, create a file in the tests folder and make sure it starts with test\_ or it won't be picked up.
This naming convention extends to all test methods defined in the test file.

```Running specific tests
* To run tests within a module: run
$ pytest <directory>/<filename.py>, e.g. poetry run pytest tests/test_view_model.py

* To run tests within a directory: run
$ pytest <directory> e.g. poetry run pytest tests

* To run a specific test within a module: run
$ poetry run pytest <module>::<method> e.g. poetry run pytest tests/test_view_model.py::test_view_model_to_do_items_returns_to_do_items
```
