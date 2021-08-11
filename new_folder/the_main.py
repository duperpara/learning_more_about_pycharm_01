


class working_on_info:
    def __init__(self, inpt, actions):
        self.inpt = inpt
        self.actios = actions
        self. dict = {}
        for action in self.actios:
            self.dict[action] = self.gen(action)

    def gen(self, var):
        if var == "x":
            return self.inpt + "xxx"
        if var == "y":
            return self.inpt + "yyy"
        if var == "z":
            return self.inpt + "zzz"



