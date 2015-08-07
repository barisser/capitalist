import data
import game_logic
import settings
import time

def init():
    datas = data.init_data()
    return datas

def cycle(data):
    data = game_logic.cycle(data)
    return data

def go():
    data = init()
    t = time.time()
    while True:
        if time.time() - t >= settings.base_cycle_interval:
            data = cycle(data)
            t = time.time()
            print t
