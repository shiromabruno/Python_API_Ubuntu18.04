class Address:

    # def __init__(self, street='', number='', state='', country=''):
    #     self.street = street
    #     self.number = number
    #     self.state = state
    #     self.country = country

    def __init__(self, street, number, state, country):
        self.street = street
        self.number = number
        self.state = state
        self.country = country
    
    # def add_values(self, street, number, state, country):
    #     self.street = street
    #     self.number = number
    #     self.state = state
    #     self.country = country

    def print_address(self):
        print("Street: " + self.street,
        "Number: " + str(self.number),
        "State: " + self.state,
        "Country: " + self.country
        )

    def get_street(self):
        return self.street
    def get_number(self):
        return self.number
    def get_state(self):
        return self.state
    def get_country(self):
        return self.country

    
#address1 = Address("Street 1", 123, "Sao Paulo", "Brazil")   
#address2 = Address("Street Urban Field", 7421, "New York", "America")   
# address1.add_values("Street 1", 123, "Sao Paulo", "Brazil")
# address2.add_values("Street Urban Field", 7421, "New York", "America")

# #print(address1.get_state())
#address1.print_address()
#address2.print_address()