class Cart:
    def __init__(self, cart_id, max_items):
        self.__cart_id = cart_id
        self.__prices = [0] * max_items
        self.__count = 0

    def addItem(self, price):
        if self.__count < len(self.__prices):
            self.__prices[self.__count] = price
            self.__count += 1

    def getTotal(self):
        total = 0
        for i in range(self.__count):
            total += self.__prices[i]
        return total

    def getItemCount(self):
        return self.__count

    def getCartId(self):
        return self.__cart_id


cart = Cart("CART-5", 20)
cart.addItem(250)
cart.addItem(99)
cart.addItem(151)

print(cart.getTotal())
print(cart.getItemCount())