# Created a Python virtual environment

```bash
python -m venv ./.venv
source ./.venv/bin/activate
pip install flask
pip install pyopenssl # To use adhoc certs
```
## Check that flask was installed properly

```bash
python -c "import flask; print(flask.__version__)"
```

## Set Flask environment variable telling flask where to find application

```bash
export FLASK_APP=main
export FLASK_ENV=development
flask run --cert=adhoc
```

## Use a self-signed cert

```bash
# See here: https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https
flask run --cert=cert.pem --key=key.pem
```
