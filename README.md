# Flask Blueprint Template

This template created using this great tutorial page from Digital Ocean:

https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications

## Getting started
Clone this repo
```bash
git clone https://github.com/cohenamitc/flask_blueprint_template.git
cd flask_blueprint_template
```
***
Create and activate virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```
***
Install libraries
```bash
pip3 install -r requirements.txt
```
***
Run this to test everything is working
```bash
python3 run.py
```
***
Open web browser session to `http://127.0.0.1:5000/api/status` to verify that everything is working

## Our App Structure

```
📦flask_blueprint_template
 ┣ 📂app
 ┃ ┣ 📂api
 ┃ ┃ ┣ 📜controllers.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂auth
 ┃ ┃ ┣ 📜controllers.py
 ┃ ┃ ┣ 📜forms.py
 ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂static
 ┃ ┣ 📂templates
 ┃ ┃ ┣ 📂auth
 ┃ ┃ ┃ ┣ 📜register.html
 ┃ ┃ ┃ ┣ 📜signin.html
 ┃ ┃ ┃ ┗ 📜signout.html
 ┃ ┃ ┗ 📜404.html
 ┃ ┗ 📜__init__.py
 ┣ 📂scripts
 ┃ ┗ 📜secret_generator.py
 ┣ 📜app.db
 ┣ 📜config.py
 ┣ 📜requirements.txt
 ┗ 📜run.py
```

## Useful Scripts

Generate Flask Secrets

`python3 scripts/secret_generator.py`

## More Resources
### Flask
https://flask.palletsprojects.com/en/2.0.x/

### Flask-WTF
https://flask-wtf.readthedocs.io/en/0.15.x/

### Flask-SQLAlchemy
https://flask-sqlalchemy.palletsprojects.com/en/2.x/

***
Happy coding!