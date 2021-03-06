import resources
import world

def init_data():
    data = {}
    data['resources'] = resources.init_resources()
    protoworld = world.World(data)
    data['world'] = protoworld
    data['players'] = []
    return data
