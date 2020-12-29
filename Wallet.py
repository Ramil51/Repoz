class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def customer_info(self):
        self.name = input('имя:')
        self.balance = input('баланс:')
        rez = 'Имя: "{0}" Баланс: "{1}"'.format(self.name, self.balance)
        return rez


    def customer_make(self):
        print('Имя: "{0}"  Баланс: "{1}"'.format(self.name, self.balance))


customer = Customer(name='Иван', balance=450)
customer.customer_make()


class Database():

    def __init__(self, dict1, name, balance):
        self.dict1 = dict()
        self.name = name
        self.balance = balance
        self.customer = Customer(self.name, self.balance)

    def get_info(self):
        dict1 = {'Имя:': '','Баланс:':''}
        self.dict1[self.name] = input('Имя:')
        self.dict1[self.balance] = input('Баланс:')
        return dict1

    def get_make(self):
        print(db.dict1)


db = Database(dict, name="имя", balance="баланс")
db.get_info()
db.get_make()

