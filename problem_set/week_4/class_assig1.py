class  Company():
    def __init__(self, name, industry_type = None, num_employees, total_revenue = 0):
        self.name = (name)
        self.industry_type = str(industry_type)
        self.num_employees = num_employees
        self.total_revenue = float(total_revenue)

    def serve_customer(self,cost):
        self.total_revenue += cost

    def gain_employees(self,employees):
        self.num_employess += len(employees)


class Tv():
    def __init__(self,brand, on_status = False, current_channel = 0, life_perc = 100):
        self.brand = brand
        self.on_status = on_status
        self.current_channel = current_channel
        self.life_perc = life_perc

    def hit_power(self):
        if self.on_status == True:
            self.on_status = False
            self.life_perc -= 0.01
            self.current_channel = 0
        elif self.on_status == False:
            self.on_status = True

    def change_channel(self,channel_num):
        if self.on_status == False:
            print ('The television is off!!!')
        else:
            self.current_channel = channel_num
            
