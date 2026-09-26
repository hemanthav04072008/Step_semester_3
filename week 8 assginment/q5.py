from datetime import datetime, timedelta


class Plan:
    def __init__(self, name, start_date):
        self.name = name
        self.start_date = start_date

    def renewal_date(self):
        pass


class BasicPlan(Plan):
    def renewal_date(self):
        return self.start_date + timedelta(days=30)


class StandardPlan(Plan):
    def renewal_date(self):
        return self.start_date + timedelta(days=90)


class PremiumPlan(Plan):
    def renewal_date(self):
        return self.start_date + timedelta(days=365)


n = int(input())

for i in range(n):
    plan_type, name, date_string = input().split()

    start_date = datetime.strptime(
        date_string, "%Y-%m-%d"
    ).date()

    if plan_type == "BASIC":
        plan = BasicPlan(name, start_date)

    elif plan_type == "STANDARD":
        plan = StandardPlan(name, start_date)

    else:
        plan = PremiumPlan(name, start_date)

    renewal = plan.renewal_date()

    print(f"{name}: {renewal}")