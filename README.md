### Heroku Deployment Repository 🚀
for [this](https://github.com/abhishekarya1/EMS-Flask-CRUD-Webapp), deployed here: https://ems-beta.herokuapp.com  

### Steps to Deploy
In the virtual environment:
1. Install `pipenv`
```
(venv) $ pip install pipenv
```
2. Install `gunicorn`
```
(venv) $ pipenv install gunicorn
```
3. Generate `requirements.txt`
```
(venv) $ pip freeze > requirements.txt
```
Place `requirements.txt` in the root folder containing the `Procfile`.

4. Rename manifest to `__init__` 
5. Add `Procfile`
```
web: gunicorn appfoldername:app
```
OR
```
web: gunicorn wsgi:app
```
(Not tested)

6. Add `wsgi.py`
```
from appfoldername import app
if __name__ == "__main__":
  app.run()
```
7. Viewing real-time Heroku log
```
$ heroku login -i

(venv) $ heroku logs --app appName --tail
```

⚠️ **Fair Warning:** sqlite is not intended to use in a production environment and hence not suited for deploying to Heroku. 
<br>More here: https://devcenter.heroku.com/articles/sqlite3
