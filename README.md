## Heroku Deployment Repository 🚀
for [this](https://github.com/abhishekarya1/EMS-Flask-CRUD-Webapp), deployed here: https://ems-beta.herokuapp.com  

### Steps to Deploy
In the virtual environment:
1. Install `pipenv`
```
(venv) $ pip install pipenv
```
2. Install `gunicorn`
```
(venv) $ pip install gunicorn
```
3. Generate `requirements.txt`
```
(venv) $ pip freeze > requirements.txt
```
Place `requirements.txt` in the root folder containing the `Procfile`.
3. Rename manifest to `__init__` 
4. Add `Procfile`
```
web: gunicorn appfoldername:app
```
OR
```
web: gunicorn wsgi:app
```
(Not tested)
5. Add `wsgi.py`
```
from appfoldername import app
if __name__ == "__main__":
  app.run()
```
6. Viewing real-time Heroku log
```
$ heroku login -i

(venv) $ heroku logs --app appName --tail
```
