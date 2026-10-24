class Delivery:
    def __init__(self, weight, distance):
        self.weight = weight
        self.distance = distance

    def calculate_fee(self):
        return 0.0


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
        return (
            25
            + (2.00 * self.weight)
            + (0.50 * self.distance)
            + self.customs_fee
        )


DELIVERY_TYPES = {
    "STANDARD": StandardDelivery,
    "EXPRESS": ExpressDelivery,
    "INTERNATIONAL": InternationalDelivery
}

n = int(input())
total = 0.0

for _ in range(n):
    parts = input().split()
    delivery_type = parts[0]
    weight = float(parts[1])
    distance = float(parts[2])

    if delivery_type == "INTERNATIONAL":
        customs_fee = float(parts[3])
        delivery = DELIVERY_TYPES[delivery_type](
            weight, distance, customs_fee
        )
    else:
        delivery = DELIVERY_TYPES[delivery_type](weight, distance)

    fee = delivery.calculate_fee()
    print(f"{delivery_type}: {fee:.2f}")
    total += fee

print(f"Total: {total:.2f}")