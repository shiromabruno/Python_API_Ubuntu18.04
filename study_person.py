import study_address

class Person:
    def __init__(self, name, age, birth, email, PRECISO PASSAR OBJETO ADDRESS AKI):
        self.name = name
        self.age = age
        self.birth = birth
        self.email = email
        self.place = OBJETO ADDRESS
    
    def change_name(self, new_name):
        self.name = new_name

    def print_person(self):
        print("Name: " + self.name,
        "Age: " + str(self.age),
        "Birth: " + self.birth,
        "Email: " + self.email,
        "Place: " + self.place
        )

address3 = study_address.Address("Rua Amarildo", 1290, "Rio de Janeiro", "Brazil")
address4 = study_address.Address("Satoshi Toori", 25, "Okinawa", "Japan")
person1 = Person("Pessoa 1", 45, '1990-05-23', "person1@email.com", address3)
person2 = Person("Pessoa 2", 21, '2003-11-03', "person2@email.com", address4)

person1.print_person()
person2.print_person()


# if __name__ == "__main__":
#     app.run()
#     app.run(debug=True)