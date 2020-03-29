import os
import sys
import gevent
import bottle as B
import game

class Appl(B.Bottle,game.Game):
    def load_config(_):
        _.config.load_config('config.ini')
        _.max_cities  = int(_.config.get('game.max cities',0))
        _.num_players = int(_.config.get('game.number of players',2))
    def __init__(_):
        B.Bottle.__init__(_)
        _.load_config()
        game.Game.__init__(_)

app = Appl()

@app.route('/map')
def _():
    return app.wm

@app.route('/')
@app.route('/<path:path>')
def _(path='/index.html'):
    return B.static_file(path, root='static')

