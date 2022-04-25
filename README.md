# [React Flask BackendDev]
<br />

## Quick-start in Docker

> Clone/Download the source code

```bash
$ git clone  https://github.com/iVampy/BackendDev.git
```

<br />

## Manual build

### Start the Flask API 

```bash
$ cd backend
$ 
$ # Create a virtual environment
$ virtualenv env
$ source env/bin/activate
$
$ # Install modules
$ pip install -r requirements.txt
$
$ # Set Up the Environment
$ export FLASK_APP=wsgi.py
$ export FLASK_ENV=development
$ 
$ # Start the API
$ flask run 
```

<br />

### Compile & start the React UI

```bash
$ cd frontend
$
$ # Install Modules
$ yarn
$
$ # Start for development (LIVE Reload)
$ yarn start 
```

## Project structure
```bash
📦BackendDev
 ┣ 📂backend
 ┃ ┣ 📜app.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜routes.py
 ┃ ┗ 📜__init__.py
 ┣ 📂frontend
 ┃ ┗ 📂build
 ┣ 📜.env
 ┣ 📜config.py
 ┣ 📜Procfile
 ┣ 📜README.md
 ┣ 📜requirements.txt
 ┗ 📜wsgi.py
 ```