class Guest:
    def __init__(self, firstname,lastname, city, status):
        self.firstname = firstname
        self.lastname = lastname
        self.city = city
        self.status = status
    def our_guest(self):
        my_guest = (self.firstname + ' ' + self.lastname + ' ' + self.city + ' ' + self.status)
        return my_guest.title()

guest_1 = Guest('Иван', 'Иванович', 'г.Москва', 'доктор')
guest_2 = Guest('Петр', 'Степанович', 'г.Тюмень', 'студент')

print(guest_1.our_guest())
print(guest_2.our_guest())