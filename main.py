import admin
import user


ACT = [{'id': 1, 'name': 'Admin'},
       {'id': 2, 'name': 'Customer'},
       {'id': 3, 'name': 'Exit'}]
keep = True
while keep:
    try:
        """
        this is for choosing who they are
        """
        for i in range(len(ACT)):
            choose = f"{ACT[i]['id']} - {ACT[i]['name']}"
            print(choose)
            print("___***___")

        add_no = int(input('Hello,Tell us who you are: '))

        if add_no == ACT[0]['id']:
            keep_going = True
            while keep_going:
                for i in range(len(admin.ADMIN)):
                    c = f"{admin.ADMIN[i]['id']} - {admin.ADMIN[i]['name']}"
                    print(c)
                    print("___***___")

                no = int(input('choose the number of act or Enter 0 for going to main menue: '))
                if no == admin.ADMIN[0]['id']:
                    regs = admin.Admin()
                    regs.register()

                elif no == admin.ADMIN[1]['id']:
                    log = admin.Admin()
                    log.login()
                elif no == 0:
                    keep_going = False
                    print('Have a nice day')




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

                elif numb == user.CUSTOMER[1]['id']:
                    login_user = user.User()
                    login_user.login()


                elif numb == user.CUSTOMER[2]['id']:
                    usr = user
                    usr.prd_list()


                elif numb == user.CUSTOMER[3]['id']:
                    u = user.User()
                    u.shopping()
                elif numb == user.CUSTOMER[4]['id']:
                    use = user.User()
                    use.change_password()

                else:
                    going = False
                    print("******you log_out successfully*****")
                    break
        else:
            keep = False
            print('Bye,thanks for your perchase')
            break
    except Exception:
        print('Please enter right number and valid data')