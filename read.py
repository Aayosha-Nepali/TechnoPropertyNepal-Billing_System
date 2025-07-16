#to read file data.txt
def read(path):
    """
    Reads a file and creates a dictionary with line numbers as keys and lines as values.

    Args:
        path (str): The path to the file to be read.

    Returns:
        dict: A dictionary with line numbers as keys and lines as values.
    """
    with open (path,"r") as file:
        kitta_number = 101
        mydictionary = {}
        for line in file:
            line=line.replace("\n",'')#replacing \n by space
            #kittanumber is key of mydictionary and lines pf dtaa.txt is value
            mydictionary[kitta_number]=(line.split(",")) 
            kitta_number += 1
    return mydictionary


def data_table(path):
    """
    Prints a formatted table of data from a file.

    Args:
        path (str): The path to the file to be read.
    """
    print("\n")
    print("-"*100)
    print("kitta no. \t District \t\t Direction \t Aana \t\t Price \t\t Availability \t")
    print("-"*100)
    with open(path,'r') as file:
        for line in file:
            print(line.replace(',',"\t\t"))