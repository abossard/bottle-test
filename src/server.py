from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello Mr. {{name}}</b>!', name=name)

run(host='localhost', reloader=True, port=8080)
