import csv


def new_product():
    q = []
    newproduct = input("*Enter* name - brand - price - barcode - product_type: \n").split('-')
    newproduct = [int(x.strip()) if x.isdigit() else x for x in newproduct]
    print(newproduct)
    with open("product.csv", "a") as product:
        product_list = csv.DictWriter(product,
                                      fieldnames=["name", "brand", "post", "barcode", "product_type"])
        product_list.writeheader()
        product_list.writerow({'name': newproduct[0], 'brand': newproduct[1], 'post': newproduct[2], 'barcode': newproduct[3],

                               'product_type': newproduct[4]})
        q.append(product_list)

    def register(self):
        mainAdmin = input("*Enter* name - password: \n").split('-')
        maniAdmin = [int(x.strip()) if x.isdigit() else x for x in mainAdmin]
        with open("new_admin.csv", "a") as new_add:
            admin_ap = csv.DictWriter(new_add, fieldnames=["name", "password"])
            admin_ap.writeheader()
            admin_ap.writerow({'name': "admin", 'password': 12345})

