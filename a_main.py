import new_folder.the_main as stuff

if __name__ == '__main__':
    print("Hellho World!!")
    actions = ["x", "y", "z"]
    obj = stuff.working_on_info("txt", actions)
    print(obj.dict["x"])
    print(obj.dict["y"])
    print(obj.dict["z"])

    print("Yay!! new update!")