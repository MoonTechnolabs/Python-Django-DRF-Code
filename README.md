# Django

## Setup

Create a virtual environment to install dependencies in and activate it:

We recommend using Python 3.10.12 to run this project.

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
Create the .env from the env.example and add the data into it.
```sh
(env)$ cd project
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```

Run the server
```
(env)$ python manage.py runserver
```

And navigate to `http://127.0.0.1:8000/`.

