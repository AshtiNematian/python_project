import csv

ADMIN = [{'id': 1, 'name': 'login'},
         {'id': 2, 'name': 'define new product'},
         {'id': 3, 'name': 'show previous factor'},
        {'id': 4, 'name': 'show list of product'},
         {'id': 5, 'name': 'log out'}]


class Admin:
    def __init__(self, username="admin", password=12345):
        self.username = username
        self.password = password

        """
      :param username :username of sys admin that we give defult 
      :param password : password of sys admin that we give defult 

        """

    def __str__(self):
        return f'{self.username}, {self.password}'

    def login(self):
        for name in range(0, 3):
            count_no = 0
            name = input("Enter username : ")
            pw = int(input("Enter password: "))
            if name == self.username and pw == self.password:
                print(f'Welcome {name} , You logged in successfully')
                break
            else:
                count_no += 1
                print("Wrong username or password,Try again")
                if count_no == 3:
                    print("You cant login for an hour")

    def new_product(self):
        q = []
        newproduct = input("*Enter* name - brand - price - barcode - product_type - number: \n").split('-')
        newproduct = [int(x.strip()) if x.isdigit() else x for x in newproduct]
        with open("product.csv", "a",newline='') as product:
            product_ap = csv.DictWriter(product,
                                        fieldnames=["name", "brand", "price", "barcode", "product_type", "number"])
            product_ap.writeheader()
            product_ap.writerow(
                {'name': newproduct[0], 'brand': newproduct[1], 'price': newproduct[2], 'barcode': newproduct[3],
                 'product_type': newproduct[4], 'number': newproduct[5]})

            q.append(product_ap)

    def factor(self):
        print('for showing admin a previous factor')
