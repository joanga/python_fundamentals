class OurClass():

    def __init__(self, name, location, members, size=0):
        self.name = name
        self.location = location
        self.size = size
        self.members(members)
        self.questions_asked = []
        if self.size >= 20:
            self.at_capacity = True
        else:
            self.at_capacity = False

    def add_class_members(self, num):
        self.size += num

        if self.size >= 20:
            print('Capacity Reached!!')
            self.at_capacity = True

   def check_if_at_capacity(self):
        return self.at_capacity
