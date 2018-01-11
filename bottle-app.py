from bottle import route, run

@route('/')
def index():
  return "Hello bottle"
  
run()
