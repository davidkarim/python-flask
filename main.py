from flask import Flask, render_template, redirect, request
import base64

app = Flask(__name__)
domain_name = 'python-flask-dk'
client_id = '1234'
client_secret = 'howdydoody'
region = 'us-east-1'

@app.route('/')
def main():
  return render_template('index.html')

@app.route('/login')
def login():
  loginendpoint = 'https://xxx.auth.us-east-1.amazoncognito.com/oauth2/authorize?'
  loginurl = loginendpoint + 'response_type=code' + '&client_id=XXX' + '&scope=xxx&redirect_uri=xxx'
  loginurl = 'https://python-flask-dk.auth.us-east-1.amazoncognito.com/login?response_type=code&client_id=6jtq1ve64uccv0j7k2ul0m4e7l&redirect_uri=https://127.0.0.1:5000'
  return redirect(loginurl)

@app.route('login_callback')
def login_callback():
  code = request.args.get("code")
  authheader = base64.b64encode(client_id + ':' + client_secret)
  headers = {}
  headers['Authorization'] = 'Basic {}'.format(authheader)
  headers['Content-type'] = 'application/x-www-form-urlencoded'
  tokenendpoint = 'https://' + domain_name + '.auth.' + region + 'amazoncognito.com/oauth2/token'
  data = {}
  data['client_id'] = client_id
  data['grant_type'] = 'authorization_code'
  data['redirect_uri'] = redirect_target
  data ['code'] = code