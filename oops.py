class Mobile:
    def __init__(self,brand,ram,price):
        self.brand=brand
        self.ram=ram
        self.price=price
    def display(self):
        print("Brand:",self.brand)
        print("price:", self.price)
        print("-------------------")
# for i in range(3):
obj=Mobile("Apple","8gb","90000")
obj.display()
410
obj2=Mobile("oppoA31","8gb","90000")
obj2.display()
obj3=Mobile("oppoA31","8gb","90000")
obj3.display()

