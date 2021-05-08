import admin
import csv

import product


class Product:
    def __init__(self, name=None, brand=None, cost=None, barcode=None, product_type=None, number=None):
        self.name = name
        self.brand = brand
        self.cost = cost
        self.barcode = barcode
        self.product_type = product_type
        self.number = number

    def stock(self):
        with open('product.csv', newline='') as pu:
            pc = csv.DictReader(pu)
            for i in pc:
                print(i['name'], i['number'])
                if i == 0:
                   print(f'warning,{i["name"]}is finished')
                else:
                    continue
        return

