import csv
import admin

CUSTOMER = [{'id': 1, 'name': 'rigester'},
            {'id': 2, 'name': 'login'},
            {'id': 3, 'name': 'Show only list of product'},
            {'id': 4, 'name': 'buy product'},
            {'id': 5, 'name': 'log out'}]


class User:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __str__(self):
        return f'{self.username}, {self.password}'

    def register(self):
        name = []
        self.username = input("Enter username: ")
        self.password = int(input("Enter password: "))
        with open("customer.csv", "a") as customer:
            customer_ap = csv.DictWriter(customer, fieldnames=["username", "password"])
            customer_ap.writeheader()
            customer_ap.writerow({'username': self.username, 'password': self.password})
            name.append(customer_ap)
        return customer_ap

    def login(self):
        l_name = input("Enter username : ")
        l_pass = int(input("Enter password: "))
        with open('customer.csv', newline='') as cus:
            c_reader = csv.DictReader(cus)
            for row in cus:
                for name in range(0, 3):
                    count_no = 0
                    if l_name == c_reader['username'] and l_pass == c_reader['password']:
                        print(f'Welcome {l_name} , You logged in successfully')
                        break
                    else:
                        count_no +=1
                        print("Wrong username or password,Try again")
                        if count_no ==3:
                            print("You cant login for an hour")

    def prd_list(self):
        with open('product.csv', newline='') as p:
            p_reader = csv.DictReader(p)
            for row in p:
                    print(row["name"], row["price"])
        return

    def buy(self):
        #with open('product.csv', newline='') as b_ls:
            #bought = csv.DictReader(b_ls)
            #for item in bought:




