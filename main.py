import admin
import user


ACT = [{'id': 1, 'name': 'Admin'},
       {'id': 2, 'name': 'Customer'},
       {'id': 3, 'name': 'Exit'}]
keep = True
while keep:
    """
    this is for choosing who they are
    """
    try:
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

                no = int(input('choose the number of act or Enter 0 for going to main menu: '))
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
            keep_it = True
            while keep_it:
                for i in range(len(user.CUSTOMER)):
                    c = f"{user.CUSTOMER[i]['id']} - {user.CUSTOMER[i]['name']}"
                    print(c)
                    print("___***___")

                no = int(input('choose the number of act or Enter 0 for going to main menue: '))
                if no == user.CUSTOMER[0]['id']:
                    reg= user.User()
                    reg.register()

                elif no == user.CUSTOMER[1]['id']:
                    logs = user.User()
                    logs.login()
                elif no == 0:
                    keep_it = False
                    print('Have a nice day')

        elif add_no == ACT[2]['id']:
            keep = False
            print('*****Good bye,We hope to see you again*****')
            break

    except Exception:
        print('Please enter right number and valid data')