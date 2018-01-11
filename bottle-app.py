from bottle import route, run
import os

@route('/')
def index():
  return "Hello bottle"

@route('/hello')
def hello():
  return "This is route hello"

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

