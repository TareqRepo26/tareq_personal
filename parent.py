class Parent:
    def __init__(self, name, fav_food, hobby, catchphrase):
        self.name = name
        self.fav_food = fav_food
        self.hobby = hobby
        self.catchphrase = catchphrase

    def introduce(self):
        print(self.name + "enjoys" + self.fav_food + "and likes" + self.hobby)

    def relax(self):
        print(self.name + " is now chilling")

    def indulge(self):
        print(self.name + "is eating" + self.fav_food)
