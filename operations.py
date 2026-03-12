from admin import *

class operations:
    def __init__(self):
        self.admin1 =admin()
        
    def input_is_valid(self, msg , start, end):
        while True:
            inp = input(msg)
            if not inp.isdecimal():
                print("Invalid Input . Try again")
            else:
                return int(inp)
        
    def get_choice(self, num_options):
        msg = f"Enter your choice from 1 to {num_options} ------>"
        return self.input_is_valid(msg , 1 , num_options)
    
    def menu(self):
        print("Program Options:\n ")
        print("=====================================")
        options=[
            '1) ADD Book',
            '2) Print Library books',
            '3) Search a specific book by prefix',
            '4) Add user',
            '5) Borrow book',
            '6) Return book',
            '7) Print users borrowed book',
            '8) Print all active users' 
            
        ]
        print('\n'.join(options))
        print("=====================================")
        return self.get_choice(len(options)) #---->8
        
    def add_book(self):
        book_id= input('Please Enter the book_id: \n')
        book_name = input('Please Enter the book_name: \n')
        book_quantity = input('Please Enter the book quantity: \n')
        self.admin1.add_book( book_id , book_name , book_quantity)
    
    def print_books(self):
        print(self.admin1.print_all_books())
    
    def search_books(self):
        query = input("Enter your query: \n ")
        print(', '.join(self.admin1.search_for_book(query)))
    
    def add_user(self):
        user_id = int(input("Enter user_id: "))
        user_name = input("Enter user name: ")
        self.admin1.add_user(user_id , user_name)
        
    def borrow_book(self):
        user_id = int(input("Enter user id: "))
        book_name = input('Please Enter the book_name: ')
        self.admin1.borrow_book(user_id , book_name)
        
    def return_book(self):
        user_id = int(input("Enter user id: "))
        book_name = input('Please Enter the book_name: ')
        self.admin1.return_book(user_id , book_name)
        
    def print_users_borrowed_book(self):
        self.admin1.print_users_borrowed()
    
    def print_all_users(self):
        print("working start in operations.py")
        print(self.admin1.print_all_users())
        
    
    def run(self):
        while True:
            choice = self.menu()
            
            if choice==1:
                self.add_book()
            elif choice ==2:
                self.print_books()
            elif choice == 3:
                self.search_books()
            elif choice==4:
                self.add_user()
            elif choice ==5:
                self.borrow_book()
            elif choice ==6:
                self.return_book()
            elif choice ==7:
                self.print_users_borrowed_book()
            elif choice == 8:
                self.print_all_users()
            else:
                print("exiting program")
                break