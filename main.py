# spend bill gates money
from  submain import display_bill_gate_money, for_choice_2

def main():
    '''
    desctription

    '''
    while True:
        print("\n===================================================")
        print(" Welcome to Spend Bill Gates Money Simulator")
        print("====================================================")
        print("\n1. Display total net Worth of Bill Gates")
        print("2. Purchase Various items from the store")
        print("3. Exit")
        choice = input("\nEnter your choice => | 1 | 2 | 3 : ")
        
        if choice == "1":
            display_bill_gate_money()
            
        elif choice == "2": 
            for_choice_2()
            
        elif choice == '3':
            print("\n---------------Exiting-----------------\n")
            print("\n-----------------------------------------")
            print("Thank you exploring 'Spend Bill Gates Money Simulator.'")
            print("-----------------------------------------\n")
            break
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == '__main__':
    main()
    