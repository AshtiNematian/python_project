import csv
import hashlib
import logging
import pandas as pd

logging.basicConfig(level=logging.INFO, filename='new_factor.log', filemode='a', format='%(asctime)s - %(levelname)s')

CUSTOMER = [{'id': 1, 'name': 'register'},
            {'id': 2, 'name': 'login'},
            {'id': 3, 'name': 'Show only list of product'},
            {'id': 4, 'name': 'buy product'},
            {'id': 5, 'name': 'change password'},
            {'id': 6, 'name': 'log out'}]

shop = [{'id': 1, 'name': 'Add item'},
        {'id': 2, 'name': 'See the factor'},
        {'id': 0, 'name': 'Exit Program'}]


'''
the function of reading csv file of product to show customer
'''
def prd_list():
    with open('product.csv', newline='') as p:
        p_reader = csv.DictReader(p)
        line_count = 0
        for row in p_reader:
            if line_count == 0:
                print(f'Column name are {", ".join(row)}')
                line_count += 1
            print(f' name :{row["name"]}, price : {row["price"]}')
            line_count += 1


class User:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

        """
            :param username :username of customer  
            :param password : password of customer  
        """




    def register(self):
        """
        register function is for register user and we add it to account.csv file
        """
        try:
            self.username = input("*Enter* username: ")
            self.password = input("*Enter* password: ")
            hash_password = hashlib.sha256(self.password.encode('utf8')).hexdigest()
            user = [self.username, hash_password]
            print(user)
            """
            this part is for checking if new user pick same username that before exist
            and tell user pick another username
            """
            with open('account.csv') as csv_log:
                read = csv.reader(csv_log)
                col0 = [x[0] for x in read]
                if user[0] in col0:
                    print('This username already taken,please try another one')
                else:
                    user_account = pd.DataFrame([[user[0], user[1]]])
                    user_account.to_csv('account.csv', mode='a', index=False, header=False)
                    print('*****You are registered successfully')
                    return user

        except Exception:
            print("Please enter valid data ")

    def login(self):
        """
        this fuction is for user login and checking user name and
        password that user enter is valid or not if is valid can use program

        :return: data is list
        """
        try:
            data = []
            with open('account.csv') as csv_log:
                reader = csv.reader(csv_log)
                for row in reader:
                    data.append(row)
            un = input("please Enter user name: ")
            pw = input('Please Enter password: ')
            hash_pw = hashlib.sha256(pw.encode('utf8')).hexdigest()

            col0 = [x[0] for x in data]
            col1 = [x[1] for x in data]
            if un in col0:
                for k in range(len(col0)):
                    if col0[k] == un and col1[k] == hash_pw:
                        print('You are logged in ')
                        login = True
            else:

                print('wrong username or password')
                return data
        except:
            print('Please enter valid data')

    def shopping(self):
        """
        this function is for user shopping basket after trying buy somthing can factor of it
        """


        try:
            keeping = True
            while keeping:
                for i in range(len(shop)):
                    print(f"{shop[i]['id']} - {shop[i]['name']}")
                    print("___***___")
                option = int(input('Enter the no of option you want: '))
                if option == shop[0]['id']:
                    """
                    this condition is for when user try to add item to shopping basket
                    """
                    cus_shop = pd.read_csv('product.csv', usecols=["name", "price", "number"])
                    print(cus_shop)
                    purch_c = input(
                        "Please enter name  of row and  and number of how many of"
                        "  product you want(Please separate Enter with (-)): \n").split('-')
                    purch_c = [int(x.strip()) if x.isdigit() else x for x in purch_c]
                    print(purch_c)
                    factor = pd.DataFrame(data={'name': [purch_c[0]], 'number': [purch_c[1]]})
                    factor.to_csv('purchase.csv', mode='a')
                    pro = pd.read_csv('product.csv', usecols=['name', 'number'])
                    logging.info('new factor')
                    p = pd.read_csv('product.csv', usecols=['name', 'number'])
                    p_reader = csv.reader(p)

                if option == shop[1]['id']:
                    """
                    this condition is for when user try to see factor
                    """
                    basket1 = pd.read_csv('purchase.csv', usecols=["name", "number"])

                    print(basket1)
                else:
                    keeping = False
                    break


        except Exception:
            print('Please enter valid data or seprate data with (-)')

    def change_password(self):
        """
        for changing password
        """
        try:
            change = pd.read_csv('account.csv')
            location = 0
            old_password = input("Enter old password: ")
            new_password = input("Enter new password: ")
            hash_old_pass = hashlib.sha256(old_password.encode()).hexdigest()
            hash_new_pass = hashlib.sha256(new_password.encode()).hexdigest()
            with open('account.csv', 'r') as my_file:
                csv_reader = csv.reader(my_file)
                for row in csv_reader:
                    print(self.password)
                    if row[0] == self.username and row[1] == hash_old_pass:
                        self.password = hash_new_pass
                        print(self.password)
                        print("Your password is changed.")
                        change.loc[location, row[1]] = hash_new_pass
                        change.to_csv('account.csv', index=False)
                    location += 1


        except Exception:
            print('Please enter valid data')


    def __str__(self):
        return f'{self.username}, {self.password}'
