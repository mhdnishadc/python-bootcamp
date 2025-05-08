class Cars:
    def __init__(self, name, price, color):
        self.name = name
        
        self.price = price 
        self.color = color

    def start(self):
        print(self.name + "Car started")

car1 = Cars("BMW", 1000000, "Black")
car2 = Cars("Audi", 2000000, "White")
car1.price= 1900000
print(car1.name, car1.price)
print(car2.price)


 