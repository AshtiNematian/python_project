import csv
import logging
import pandas as pd
import hashlib

logging.basicConfig(level=logging.INFO, filename='Adminlogging.log',
                    filemode='a', format='%(asctime)s - %(levelname)s')

ADMIN = [{'id': 1, 'name': 'register'},
         {'id': 2, 'name': 'login'}]

ad_list = [{'id': 1, 'name': 'define new product'},
           {'id': 2, 'name': 'show previous factor'},
           {'id': 3, 'name': 'show list of product'},
           {'id': 4, 'name': 'log out'}]


class Admin:
    def __init__(self, username='admin', password=12345):
        self.username = username
        self.password = password

        """
      :param username :username of sys admin that we give defult 
      :param password : password of sys admin that we give defult 

        """

    def register(self):
        """
        register function is for register admin at first with defult data and after that admin
          can choose the user and password that like is only a admin and dont append is write mode
          add it to adm.csv file
        """
        try:
            print('Please enter default User name and Password')
            user = input('Default Username: ')
            passw = int(input('Default password: '))
            if user == self.username and passw == self.password:
                print('*** Welcome,You registered successfully,please define new password and User name: ')
            with open('adm.csv', mode='w', newline='') as adm:
                adm_reg = csv.writer(adm, delimiter=',')
                username = input('Please enter username: ')
                pas = input('Please enter password: ')
                hash_pd = hashlib.sha256(pas.encode('utf8')).hexdigest()
                adm_reg.writerow([username, hash_pd])
        except Exception:
            print('Please Enter valid data')

    def login(self):
        """
        in this method admin can login if the user or password be wrong cant see the list of action that can do
        so at firt have to login correctly after that do what ever want to do
        """
        try:
            usr = input("Enter username : ")
            p = input("Enter password: ")
            hash = hashlib.sha256(p.encode('utf8')).hexdigest()
            user = [usr, hash]
            with open('adm.csv', mode='r') as f:
                read = csv.reader(f, delimiter=',')
                for row in read:
                    if row[0] == usr and row[1] == hash:
                        logging.info('Admin logged in')
                        print('you are logged in')
                        going = True
                        while going:
                            for j in range(len(ad_list)):
                                print(f"{ad_list[j]['id']} - {ad_list[j]['name']}")
                                print("___***___")
                            num = int(input('choose the number of act: '))
                            if num == ad_list[0]['id']:
                                """
                                that condition is for define new product 
                                """
                                self.new_product()

                            elif num == ad_list[1]['id']:
                                """
                                with choosing this item can see factors
                                """
                                self.pervious_fac()
                            elif num == ad_list[2]['id']:
                                """
                                with this function can see list of product
                                """
                                self.product_list()
                            else:

                                going = False
                                print("******you log_out successfully*****")
                                break

                        else:
                            print('please try again')

        except Exception:
            print("Please Enter valid data")

    def new_product(self):
        """
        its for define new product that only admin can do that
        :return:
        """
        try:
            newproduct = input("*Enter* name - brand - price - barcode - product_type - number: \n").split('-')
            newproduct = [int(x.strip()) if x.isdigit() else x for x in newproduct]
            product = pd.DataFrame(data={'name': [newproduct[0]], 'brand': [newproduct[1]], 'price': [newproduct[2]],
                                         'barcode': [newproduct[3]], 'product_type': [newproduct[4]],
                                         'number': [newproduct[5]]})
            product.to_csv('product.csv', mode='a')
        except Exception:
            print('Please Enter valid data or use (-) between your each data')

    def product_list(self):
        """
        list of product with all items
        """
        cus_shop = pd.read_csv('product.csv')
        print(cus_shop)

    def pervious_fac(self):
        """
        list of factor that customer bought any thing
        """
        per_fact = pd.read_csv('purchase.csv')
        print(per_fact)

    def __str__(self):
        return f'{self.username}, {self.password}'
