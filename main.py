
import admin
import product
import user

ACT = [{'id': 1, 'name': 'Admin'},
       {'id': 2, 'name': 'Customer'}]
for i in range(len(ACT)):
    choose = f"{ACT[i]['id']} - {ACT[i]['name']}"
    print(choose)
    print("___***___")

add_no = int(input('Hello,Tell us who you are: '))
if add_no == ACT[0]['id']:
    Keep_going = True
    while Keep_going:
        for i in range(len(admin.ADMIN)):
            c = f"{admin.ADMIN[i]['id']} - {admin.ADMIN[i]['name']}"
            print(c)
            print("___***___")
        no = int(input('choose the number of act: '))
        if no == admin.ADMIN[0]['id']:
            log = admin.Admin()
            log.login()
        if no == admin.ADMIN[1]['id']:
            manager = admin.Admin()
            manager.new_product()
            print("******you added new proudact successfully*****")
        if no == admin.ADMIN[2]['id']:
            pass
        if no == admin.ADMIN[3]['id']:
            pl = product.Product()
            print(pl.stock())

        if no == admin.ADMIN[4]['id']:
            Keep_going = False
            print("******you log_out successfully*****")
            break




elif add_no == ACT[1]['id']:
    going = True
    while going:
        for i in range(len(user.CUSTOMER)):
            chosen_ls = f"{user.CUSTOMER[i]['id']}, {user.CUSTOMER[i]['name']}"
            print(chosen_ls)
            print("___***___")

        numb = int(input('choose the number of act: '))
        if numb == user.CUSTOMER[0]['id']:
            reg = user.User()
            reg.register()
            print("******you Registered successfully*****")
        elif numb == user.CUSTOMER[1]['id']:
            log_cus = user.User()
            log_cus.login()

        elif numb == user.CUSTOMER[2]['id']:
            usr = user.User()
            usr.prd_list()


        elif numb == user.CUSTOMER[3]['id']:
            pass
        elif numb == user.CUSTOMER[4]['id']:
            going = False
            break

