class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} costs ${self.price}."


class Equipment(Product):
    def __init__(self, name, price, weight, sport):
        super().__init__(name, price)
        self.weight = weight
        self.sport = sport

    def __str__(self):
        return (
            f"A {self.sport} {self.name} "
            + f"that weighs {self.weight} and costs ${self.price}."
        )


class Clothing(Product):
    def __init__(self, name, price, material, color):
        super().__init__(name, price)
        self.material = material
        self.color = color

    def __str__(self):
        return f"A {self.color} {self.material} {self.name} that costs ${self.price}."


clothing = Clothing("Football Jersey", 20, "Jersey Knit", "Red")

# equipment = Equipment("Bat", 50, 2, "Baseball")

print(clothing)
