import math
import random

class Game:
    def make_player(_, **kw):
        player = dict(kw)
        return player
    def make_city(_):
        r =         230 * random.random()
        t = 2 * math.pi * random.random()
        x = (4/3) * r * math.cos(t) + 320
        y =         r * math.sin(t) + 240
        city = dict( pos = (x, y),
                     owner = 0,
        )
        return city
    def __init__(_):
        _.wm = dict()
        _.wm['size'] = (640, 480)
        _.wm['players'] = [
            _.make_player(color='gray', ),
            _.make_player(color='yellow', human = 1),
            _.make_player(color='maroon'),
            _.make_player(color='purple'),
            _.make_player(color='yellow'),
            _.make_player(color='lime'),
        ][:_.num_players]
        _.wm['cities']  = [ _.make_city()
                            for r in range(_.max_cities) ]
        _.wm['cities'][0]['owner'] = 1
        _.wm['cities'][1]['owner'] = 2

