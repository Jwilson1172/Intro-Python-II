class Item:
    def __init__(self, name: str, weight: float, price: float):
        self.name = name
        self.weight = weight
        self.price = price

    def __str__(self):
        return f"{self.name} costs ${self.price}.0"


class Weapon(Item):
    def __init__(self, dam: float, *args):
        super.__init__(*args)
        self.dam = dam
        self.multi = 1
        return

    def set_multi(self, multi: float):
        self.multi = multi
        return


class Aid(Item):
    def __init__(self, str_mul: float, amt: int, *args):
        super.__init__(*args)
        self.str_mul = str_mul
        self.amt = amt
        return
