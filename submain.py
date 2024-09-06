
def display_bill_gate_money():
    try:
        with open("total_net_worth.txt", "r") as file:
            line = file.read()
            print(f"\nTotal remaining net worth of Bill gates is: {line}")
            
    except FileNotFoundError:
        print(f"\nThe file 'total_net_worth.txt' does not exist.")

def for_choice_2():
    print("k chha?")