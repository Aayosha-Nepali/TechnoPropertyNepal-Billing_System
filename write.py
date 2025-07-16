from read import read

def update_availability(file_name, kitta_number, status):
    """
    Update the availability status of a land plot in the lands data file.

    Args:
        file_name (str): The name of the file containing the lands data.
        kitta_number (int): The kitta number of the land plot to update.
        status (str): The new availability status ('available' or 'rented').

    Returns:
        None
    """
    lands_dict = read(file_name)
    # upfdate the 
    lands_dict[kitta_number][5] = status
    with open(file_name, 'w') as file:
        for kitta_number, details in lands_dict.items():
            line = ''
            for detail in details:
                line += str(detail) + ','
            line = line[:-1] + '\n'
            file.write(line)


def write_rent_invoice(file_name, user_details, rented_lands, grand_total):
    """
    This function generates a rent invoice for the given user details, rented lands, and grand total.
    It writes the invoice details to a file with the specified file name.
    """
    with open(file_name, 'w') as file:
        file.write("\t \t \t Technoproperty Nepal\n")
        file.write("\t \t \t Address: Kamalpokhari Kathmandu Metropolitan\n")
        file.write("\t \t \t Contact: 9800780046 || Email: technorental@gmail.com\n")
        file.write("Name of customer: " + user_details["name"] + "\n")
        file.write("Phone of customer: " + user_details["phone"] + "\n")
        file.write("-" * 90 + "\n")
        file.write('\t \t \t\t STATUS: RENTING INVOICE\n')
        file.write("-" * 90 + "\n")
        file.write('\t \t \t Kitta NO.\t Aana \t Month \t Price per month \t Total Price\n')
        file.write("-" * 90 + "\n")
        for land in rented_lands:
            file.write("\t\t\t " + str(land[0]) + "\t\t" + str(land[1]) + "\t" + str(land[2]) + "\t" +
                       str(land[3]) + "\t\t\t" + str(land[4]) + "\n")
        file.write("Grand total is: " + str(grand_total) + "\n")
        file.write('Thank you for using Technorental services\n')
    
    #printing the contents of the file
    with open(file_name, 'r') as file:
        print(file.read())

def write_return_invoice(file_name, user_details, returned_lands, grand_total):
    """
    This function generates a return invoice for the given user details, returned lands, and grand total.
    It writes the invoice details to a file with the specified file name.
    """
    with open(file_name, 'w') as file:
        file.write("-" * 90 + "\n")

        file.write("\t \t \t\t    Technoproperty Nepal\n")
        file.write("\t \t \t Address: Kamalpokhari Kathmandu Metropolitan\n")
        file.write("\t \t \t Contact: 9800780046 || Email: technorental@gmail.com\n")
        file.write("-" * 90 + "\n")

        file.write("Name of customer: " + user_details["name"] + "\n")
        file.write("Phone of customer: " + user_details["phone"] + "\n")

        file.write("-" * 90 + "\n")
        file.write('\t \t \t\t STATUS: RETURNING INVOICE\n')
        file.write("-" * 90 + "\n")

        file.write('\t \t \t Kitta NO.\t Aana \t Month \t Price per month \t Total Price\n')
        file.write("-" * 90 + "\n")

        for land in returned_lands:
            file.write("\t\t\t " + str(land[0]) + "\t\t" + str(land[1]) + "\t" + str(land[2]) + "\t" +
                       str(land[3]) + "\t\t\t" + str(land[4]) + "\n")
        file.write("Grand total is: " + str(grand_total) + "\n")
        file.write('Thank you for using Technorental services\n')

    #printing the contents of the file
    with open(file_name, 'r') as file:
        print(file.read())
