from write import write_rent_invoice, write_return_invoice, update_availability
from read import data_table, read


def rent_land(mydictionary):
    """
    Allows the user to rent land by selecting kitta numbers and specifying the rental duration.
    Generates a rent invoice and updates the availability of the rented land.
    """
    while True:
        print()
        name = input("Enter your name: ")
        if name.isdigit() == True:
            print("Invalid name. Please enter a valid name.")
            continue            
        break


    while True:
        print()
        try:
            phone = int(input("Enter your phone number: "))
            if len(str(phone)) != 10:
                print("Invalid phone number. Please enter a 10-digit phone number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

    user_land = []
    continue_loop = True
    while continue_loop:
        # selecting kitta number
        while True:
            print()
            try:
                kitta_number = int(input("Please select the kitta number you want to rent: "))
                if kitta_number <= 100 or kitta_number>len(mydictionary)+100:
                    print("Invalid kitta number. Please enter a valid kitta number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
        
        # checking if land is available
        is_available = mydictionary[kitta_number][5]
        if is_available.strip().lower() != "available":
            print()
            print("This land is not available for rent.")
            continue

        # informing the user
        aana_land = int(mydictionary[kitta_number][3])
        print("\n")
        print(kitta_number,"kitta number has",aana_land,"aana of land\n")

        # asking for rental duration
        while True:
            print()
            try:
                month = int(input("Enter the number of months you want to rent for: "))
                if month <= 0:
                    print("Invalid months. Please enter a valid number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

        # calculating bill
        per_month_price = int(mydictionary[kitta_number][4])
        bill_kitta_number = kitta_number
        aana = aana_land
        month = month
        per_month_price_land = per_month_price
        total_price = month * per_month_price_land

        # adding to list
        user_land.append([bill_kitta_number, aana, month, per_month_price_land, total_price])

        # asking if user wants to rent more lands
        print()
        while True:
            try:
                more = input("Do you want to rent more lands?(yes/no): ")
                if more.strip().lower() not in ["yes", "no"]:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter 'yes' or 'no'.")
                continue

        if more.strip().lower() == "yes":
            continue_loop = True
        else:
            grand_total = 0
            for land in user_land:
                grand_total += land[4]
            
            # generating invoice
            generate_rent_invoice(name, str(phone), user_land, grand_total)
            for land in user_land:
                # updating availability
                update_availability("data.txt", land[0], "Not Available")
            print()
            print('Thank you for using Technorental services.\n')
            break


def return_land(mydictionary):
    """
    Allows the user to return rented land and generates a return invoice.
    Calculates any fines for extended rental periods and updates the availability of the returned land.
    """
    # getting user details
    print()
    print("Returning land process...")
    while True:
        print()
        name = input("Enter your name: ")
        if name.isdigit() == True:
            print("Invalid name. Please enter a valid name.")
            continue            
        break

    while True:
        print()
        try:
            phone = int(input("Enter your phone number: "))
            if len(str(phone)) != 10:
                print("Invalid phone number. Please enter a 10-digit phone number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
    user_land = []
    continue_loop = True
    while continue_loop:

        # selecting kitta number
        while True:
            print()
            try:
                kitta_number = int(input("Please select the kitta number you want to return: "))
                if kitta_number <= 100 or kitta_number>len(mydictionary)+100:
                    print("Invalid kitta number. Please enter a valid kitta number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
        
        # checking if land is available
        is_available = mydictionary[kitta_number][5]
        if is_available.strip().lower() != "not available":
            print("This land is not rented for rent Please select another land.")
            continue

        # informing the user
        aana_land = int(mydictionary[kitta_number][3])
        print("\n")
        print(kitta_number,"kitta number has",aana_land,"aana of land\n")

        # asking for rental duration
        while True:
            print()
            try:
                months_initial = int(input("Enter the number of months you initially wanted to rent for: "))
                if months_initial <= 0:
                    print("Invalid months. Please enter a valid number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
        while True:
            print()
            try:
                months_returned = int(input("Enter the number of months you actually rented the land for: "))
                if months_returned <= 0:
                    print("Invalid months. Please enter a valid number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

        # calculating fine
        if months_returned > months_initial:
            fine_months = months_returned - months_initial
            fine_amount = 0.2 * fine_months * int(mydictionary[kitta_number][4])
            print("You rented the land for", months_returned, "months which is more than initially intended.\n")

            print("Fine for extended months (20% per month):", fine_amount, "Nepalese Rupees \n")
        else:
            fine_amount = 0

        # calculating bill
        per_month_price = int(mydictionary[kitta_number][4])
        bill_kitta_number = kitta_number
        aana = aana_land
        per_month_price_land = per_month_price
        total_price = months_returned * per_month_price_land + fine_amount

        # adding to list
        user_land.append([bill_kitta_number, aana, months_returned, per_month_price_land, total_price])

        # asking if user wants to return more lands
        while True:
            try:
                more = input("Do you want to return more lands?(yes/no) ")
                if more.strip().lower() not in ["yes", "no"]:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter 'yes' or 'no'.")
                continue
        if more.strip().lower() == "yes":
            continue_loop = True
        else:
            grand_total = 0
            for land in user_land:
                grand_total += land[4]

            # generating invoice
            generate_return_invoice(name, str(phone), user_land, grand_total)
            for land in user_land:
                # updating availability
                update_availability("data.txt", land[0], "Available")
            print()
            print('Thank you for using Technorental services.\n')
            break



def generate_rent_invoice(name, phone, rented_lands, grand_total):
    """
    Generates a rent invoice for the rented lands.
    """
    invoice_name = name + phone + "_invoice.txt"
    user_details = {"name": name, "phone": phone}
    write_rent_invoice(invoice_name, user_details, rented_lands, grand_total)

def generate_return_invoice(name, phone, rented_lands, grand_total):
    """
    Generates a return invoice for the returned lands.
    """
    invoice_name = name + phone + "_invoice.txt"
    user_details = {"name": name, "phone": phone}
    write_return_invoice(invoice_name, user_details, rented_lands, grand_total)



