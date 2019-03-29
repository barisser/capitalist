import economics
import math
import random
import resources
import settings

class Tile:
    def __init__(self, x, y, data):
        self.productivity = []
        for i in range(0, len(data['resources'])):
            self.productivity.append(random.random())
        self.x = x
        self.y = y
        self.population = random.randint(0, 2*settings.average_pop_per_tile)
        self.commodity_stocks = [0] * len(data['resources'])
        self.prices = [0] * len(data['resources'])
        self.money = self.population * 1
        self.owner = ''

    def produce(self, data):
        resources_n = len(data['resources'])
        for i in range(0, resources_n):
            production = self.productivity[i] * self.population
            previous_supply = self.commodity_stocks[i]
            self.commodity_stocks[i] += production
            self.prices[i] = economics.find_price(previous_supply, self.commodity_stocks[i], self.prices[i], data['resources'][i].base_demand, data['resources'][i].price_elasticity)

    def consume(self, data):

