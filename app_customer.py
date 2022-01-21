from customer import Customer
from database import Database


def create_customer():

    name = input("Please enter the new customer's name: ")
    addr = input("Please enter the new customer's address: ")
   # option = input("Please confirm save or not: s for save, otherwise cancel: ")
   # option = input("Please confirm: S -- save M -- modify ")
    option ='s'
    if option!='s':
       c1 =None
    else:
        c1 = Customer(name, addr)

        c_no = c1.new_customer_in_db()
        print(c_no)
        if c_no == -1 :
            print("creation failed!")
        else:
            print("%%%%%%%% customer has been created %%%%%%%% ")
            print("         The customer_no is: {} ".format(c_no))

    return c1


def create_customer1():
    name = input("Please enter the new customer's name: ")
    addr = input("Please enter the new customer's address: ")

    c1 = Customer(None, name, addr)
    print('custer will be created as:')
    print(c1)

    c_no = c1.new_customer_in_db()
    if c_no == -1 :
        print("creation failed!")
    else:
        print("customer has been created. The customer_no is: {}".format(c_no))

    return c1


def print_customer_list(customers):
    for i, customer in enumerate(customers):
        print("ID: {}".format(i))
        print_customer_details(customer)


def menu():

    def menu_00_main():
        selection = input("************ welcome to banking system **********\n"
                          "Enter:\n"
                          "'1'-- customer manangement \n"
                          "'2'-- account mangement \n"
                          "'q' to quit. \n"
                          "Enter your selection: ")
        return selection

    def menu_10_customer():
        selection = input("-----------  Customer Management -------------\n"
                          "Enter:\n"
                          "'1'-- Add a customer \n"
                          "'2'-- Add an account to customer \n"
                          "'q' to quit. \n"
                          "Enter your selection: ")
        return selection

    selection= menu_00_main()

    while selection != 'q':
        if selection == '1':
            print_customer_list(customer_list)
        elif selection == '2':
            print('-----------------function not available yet------------------------')

        selection = menu_00_main()
        print("you select {}".format(selection))


Database.initialise()
session = Database.get_session()

create_customer()

