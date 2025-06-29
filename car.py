class Tesla():
    def made_in(self):
        print("Tesla was made in 2003.")

class Ferrari():
    def made_in(self):
        print("Ferrari was made in 1939.")
obj1=Tesla()
obj2=Ferrari()

for car in (obj1,obj2):
    car.made_in()