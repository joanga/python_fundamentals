class TipOutTracker():
    def __init__(self):
        self.bill = 0.0
        self.rate = 0.0
        self.total = 0.0

    def add_bill(self, bill, rate = 0.15):
        self.rate = rate
        self.bill = bill
        self.total += 1

    def total_tip_out(self):
        tip = self.rate * self.bill
        return tip

    def __len__(self):
        return self.total



if __name__ == '__main__':
    tot = TipOutTracker()
    tot.add_bill(10)
    tot.add_bill(50, 0.18)
    tot.add_bill(40, 0.17)
    tot.add_bill(60)
    print(tot.total_tip_out())
    print(len(tot))
