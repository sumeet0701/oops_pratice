class Customer:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


def greet(customer):
    if customer.gender == 'male':
        print("hello", customer.name, "sir")
    else:
        print("hello", customer.name, "ma'am")

cust = Customer("sumeet", 'male')
print(greet(cust))

