

class SmolangFunction():
    def __init__(self, name):
        self.name = name
        self.strings = {}
        self.vars = {}
        self.lists = {}
        self.type = 'void'
        self.param_types = []
        self.code = ""
