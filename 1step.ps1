virtualenv env
.\env\Scripts\activate
$env:FLASK_APP = "run.py"
$env:FLASK_ENV = "development"
flask run --host=0.0.0.0 --port=5000