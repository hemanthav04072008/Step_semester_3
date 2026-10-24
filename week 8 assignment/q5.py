from datetime import date, timedelta


class StreamingPlan:
    validity_days = 0

    def __init__(self, name, start_date):
        self.name = name
        self.start_date = date.fromisoformat(start_date)

    def renewal_date(self):
        return self.start_date + timedelta(days=self.validity_days)


class BasicPlan(StreamingPlan):
    validity_days = 30


class StandardPlan(StreamingPlan):
    validity_days = 90


class PremiumPlan(StreamingPlan):
    validity_days = 365


PLAN_TYPES = {
    "BASIC": BasicPlan,
    "STANDARD": StandardPlan,
    "PREMIUM": PremiumPlan
}

n = int(input())

for _ in range(n):
    plan_type, name, start_date = input().split()
    subscriber = PLAN_TYPES[plan_type](name, start_date)

    print(f"{subscriber.name}: {subscriber.renewal_date()}")