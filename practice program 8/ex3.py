class Delivery:
    def __init__(self, weight, distance):
        self.weight = weight
        self.distance = distance

    def calculate_fee(self):
        pass


class StandardDelivery(Delivery):
    def calculate_fee(self):
        return 5 + (0.50 * self.weight) + (0.10 * self.distance)


class ExpressDelivery(Delivery):
    def calculate_fee(self):
        return 15 + (1.00 * self.weight) + (0.20 * self.distance)


class InternationalDelivery(Delivery):
    def __init__(self, weight, distance, customs_fee):
        super().__init__(weight, distance)
        self.customs_fee = customs_fee

    def calculate_fee(self):
        return 25 + (2.00 * self.weight) + (0.50 * self.distance) + self.customs_fee


n = int(input())
total = 0

for i in range(n):
    data = input().split()

    delivery_type = data[0]
    weight = float(data[1])
    distance = float(data[2])

    if delivery_type == "STANDARD":
        delivery = StandardDelivery(weight, distance)

    elif delivery_type == "EXPRESS":
        delivery = ExpressDelivery(weight, distance)

    else:
        customs_fee = float(data[3])
        delivery = InternationalDelivery(weight, distance, customs_fee)

    fee = delivery.calculate_fee()
    total += fee

    print(f"{delivery_type}: {fee:.2f}")

print(f"Total: {total:.2f}")