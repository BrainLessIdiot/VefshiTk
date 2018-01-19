from bottle import *

@route('/')
def index():
    return "<a href='/gaman?tala=55'>Hlekkur 0</a><a href='/sida/1'>Hlekkur 1</a><a href='/sida/2'>Hlekkur 2</a>"
@route('/sida/<id>')
def index(id):
   return "Þetta er síða rawr xd ", id
def index():
    return "Welkommen til jungelen!"
@error(404)
def villa(error):
   return "<h2>Þessi síða er ekki til, reyndu aftur!</h2>"
run(host="localhost", port=8080)
