import datetime

class Hall:
    def __init__(self, start_date, end_date, cost_per_day):
        self.start_date = datetime.datetime.strptime(start_date, '%b %d %Y')
        self.end_date = datetime.datetime.strptime(end_date, '%b %d %Y')
        self.cost_per_day = cost_per_day

    def no_days(self):
        total_days = (self.end_date - self.start_date).days + 1
        print("Total number of days:", total_days)
        self.cost(total_days)
        return total_days

    def cost(self, d):
        total_cost = d * self.cost_per_day
        print("Total cost:", total_cost)
