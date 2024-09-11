
def display_bill_gate_money():
    # Function to display Bill Gates' total net worth from a text file
    try:
        with open("total_net_worth.txt", "r") as file:
            line = file.read()
            print(f"\nTotal remaining net worth of Bill Gates is: {line}")
            
    except FileNotFoundError:
        print(f"\nThe file 'total_net_worth.txt' does not exist.")


def display_available_products():
    # Function to display available products and their prices from a file
    try:
        with open("products.txt", "r") as file:  # Reading from 'products.txt'
            lines = file.readlines()
        
        print(f"\n{'S.N.':<5} | {'Products':<40} | {'Price':<15}")
        print("-" * 65)
        
        serial_number = 1  # Manually track serial number
        for line in lines:
            stripped_line = line.strip()
            split_line = stripped_line.split(":")
            if len(split_line) == 2:  # Ensure there are exactly two parts: product and price
                product, price = split_line[0].strip(), split_line[1].strip()
                print(f"{serial_number:<5} | {product:<40} | {price:<15}")
                print("-" * 65)
                serial_number += 1  # Increment serial number manually
            else:
                print(f"Invalid data format in: {line}")
            
    except FileNotFoundError:
        print(f"\nThe file 'products.txt' does not exist.")

def for_choice_2():
    # Function to handle option 2 and display the available products
    display_available_products()
    print("\nWhat would you like to do next?")
