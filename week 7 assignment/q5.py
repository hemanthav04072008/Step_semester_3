class Cart:
    def __init__(self, cart_id, max_items):
        self.__cart_id = cart_id
        self.__prices = [None] * max_items
        self.__count = 0
        self.__max_items = max_items

    @property
    def cart_id(self):
        return self.__cart_id

    def addItem(self, price):
        if price < 0:
            print("Invalid price")
        elif self.__count >= self.__max_items:
            print("Cart is full")
        else:
            self.__prices[self.__count] = price
            self.__count += 1

    def getTotal(self):
        total = 0

        for i in range(self.__count):
            total += self.__prices[i]

        return total

    def getItemCount(self):
        return self.__count


cart = Cart("CART-5", 20)

cart.addItem(250)
cart.addItem(99)
cart.addItem(151)

print("Total =", cart.getTotal())
print("Item count =", cart.getItemCount())