


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


if __name__ == '__main__':
    print("Hellho World!!")
    actions = ["x", "y", "z"]
    obj = working_on_info("txt", actions)
    print(obj.dict["x"])
    print(obj.dict["y"])
    print(obj.dict["z"])

    print("Yay!! new update!")
