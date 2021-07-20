from study_address import Address

class Person:
    def __init__(self, name, age, birth, email):
        self.name = name
        self.age = age
        self.birth = birth
        self.email = email
        self.place = []

    def add_address(self, street, number, state, country):
        endereco = Address(street, number, state, country)
        self.place.append(endereco)

    def change_name(self, new_name):
        self.name = new_name

    def print_person(self):
        print("Name: " + self.name,
        "Age: " + str(self.age),
        "Birth: " + self.birth,
        "Email: " + self.email
        #"Place: " + list(self.place)
        )

    def print_address_person(self):
        for end in self.place:
            print (end.print_address())
        


person1 = Person("Pessoa 1", 45, '1990-05-23', "person1@email.com")
#person2 = Person("Pessoa 2", 21, '2003-11-03', "person2@email.com")
person1.add_address("Satoshi Toori", 25, "Okinawa", "Japan")

person1.print_person()
person1.print_address_person()
#person2.print_person()


# if __name__ == "__main__":
#     app.run()
#     app.run(debug=True)