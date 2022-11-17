class Entity:
    def __init__(self, name, type, belong):
        self.name = name
        self.type = type
        self.belong = belong


class Relation:
    def __init__(self, name, belong):
        self.name = name
        self.belong = belong
