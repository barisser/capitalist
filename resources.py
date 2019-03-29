class Resource:
    def __init__(self, name, base_demand, price_elasticity):
        self.name = name
        self.base_demand = base_demand
        self.price_elasticity = price_elasticity


def init_resources():
    resources = []
    food = Resource('food', 10, 0.01)
    wood = Resource('wood', 4, 1)
    iron = Resource('iron', 20, 5)
    labor = Resource('labor', 0, 0)
    power = Resource('power', 5, 5)
    resources.append(food)
    resources.append(wood)
    resources.append(iron)
    resources.append(labor)
    resources.append(power)
    return resources
