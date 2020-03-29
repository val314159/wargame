import os
import sys
from functools import partial
import random
import gevent
import bottle as B

class Appl(B.Bottle):
    def make_city(_):
        city = dict( pos = [ random.randint(0, 640),
                             random.randint(0, 480), ],
                     owner = 0,
                     
        )
        return city
    def make_map(_):
        print(_.config)
        wm = dict()
        wm['w'] = 640
        wm['h'] = 480
        wm['cities'] = [ _.make_city()
                         for r in range(10) ]
        wm['cities'][0]['owner'] = 1
        wm['cities'][1]['owner'] = 2
        return wm
    def load_config(_):
        _.config.load_config('config.ini')
        _.max_cities = int(_.config.get('game.max cities',0))
    def __init__(_):
        B.Bottle.__init__(_)
        _.load_config()
        _.wm = _.make_map()

app = Appl()

@app.route('/map')
def _():
    return app.wm

@app.route('/')
@app.route('/<path:path>')
def _(path='/index.html'):
    return B.static_file(path, root='static')

