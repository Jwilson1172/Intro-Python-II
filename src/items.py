class Item:
    """Abstract base class of all items that can be stored in a bag
    Init:
    --------
    `name` {str}: name of the object
    `weight {float}: floating point weight of object
    `price` {float}: float for the item's price
    `rarity` {float}: scalar value that applies to higher rarity
    """

    def __init__(self, name: str, weight: float, price: float, rarity: float):
        self.name = name
        self.weight = weight
        self.price = price
        return

    def __str__(self):
        """Return the string repre when called
        """
        return f"{self.name}({self.weight}lbs) costs ${self.price}.0"


class Weapon(Item):
    """A class reperesenting damage dealing items.
    """

    def __init__(self, dam: float, *args):
        super.__init__(args)
        self.dam = dam
        self.multi = 1
        return

    def set_multi(self, multi: float):
        """Multi for the weapons special ability scalar value
        """
        self.multi = multi
        return


class Aid(Item):
    """Aid items that can be used when health is low
    str_mul is a float that acts as a scalar for the rarity of the item
    """

    def __init__(self, str_mul: float, amt: int, *args):
        super.__init__(*args)
        self.str_mul = str_mul
        self.amt = amt
        return
