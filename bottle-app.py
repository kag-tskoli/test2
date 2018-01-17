from bottle import route, run
import os

@route('/')
def index():
  return "<a href="/about">About</a> <a href="/staff">Staff</a> <a href="/contact">Contact</a>

@route('/about')
def hello():
  return "<h2>About us</h2>"

@route('/staff')
def staff():
  return "<h2>Our staff</h2>"

@route('/contact')
def contact():
  return "<h2>Contact us</h2>"

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

