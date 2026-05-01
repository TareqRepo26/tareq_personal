from parent import Parent

parent_1 = Parent("Lucy", "Fried Chicken", "Knitting", "D")
parent_2 = Parent("David", "Burgers", "Football")
parent_3 = Parent("Jacky", "Salad", "Sewing")

print(parent_1.name)
print(parent_1.fav_food)
print(parent_1.hobby)

parent_1.relax()
parent_2.relax()
parent_3.relax()