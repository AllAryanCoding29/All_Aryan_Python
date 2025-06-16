class Product:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def check(self):
        return self.price > 1000

    def final_price(self):
        if self.check():
            self.price = (90/100) * self.price
        print(f"The product price is {self.price}.")

product1 = Product("Banana", 10)
product2 = Product("Refrigerator", 1050)
product3 = Product("Cricket Bat", 300)

product1.final_price()