from book import *
from user import *
import json
import os

class admin:
    def __init__(self):
        self.book=[]
        self.users={}
        self.load_data()
       
    def load_data(self):
        if not os.path.exists("library.json"):
            return
        with open("library.json" , "r") as f:
            data = json.load(f)
        
        for i in data["books"]:
            self.book.append(Book(i["id"],i["name"],i["quantity"]))
        
        for i in data["users"]:
            a = User(i["id"], i["name"])
            self.users[a]=i["borrowed"]
            
            
    def save_data(self):
        data={
            "books":[],
            "users":[]
        }
        for i in self.book:
            data["books"].append(
            {
                "id" : i.id,
                "name": i.name,
                "quantity": i.quantity
            }
            )
        for user, borrowed in self.users.items():
            data["users"].append(
                {
                    "id": user.id,
                    "name": user.name,
                    "borrowed": borrowed
                }
            )
        with open("library.json", "w") as f:
            json.dump(data, f ,indent=4)        
        
    def add_book(self , book_id , book_name , book_quantity):
        for i in self.book:
            if book_id== i.id:
                return print("This book is already exist")
        # adding quantity
        new_book = Book(book_id , book_name , book_quantity)
        self.book.append(new_book)
        self.save_data()
        print("Book is added successfully")
        
        
    def print_all_books(self):
        list_of_books=[]
        
        for i in self.book:
            list_of_books.append(i.name)
            
        
        if not list_of_books:
            return "there is no book"
        
        return ", ".join(list_of_books)
    # book_name = sonar_tori
    # sonar_Tori
    # SONAR_TORI_by_rabindrath
    
    def search_for_book(self , query):
        x = []
        for i in self.book:
            if i.name[:len(query)].upper() == query.upper():
                x.append(i.name)
        if not x:
            return "No book found"
        return x
    
    def add_user(self , user_id , user_name):
        for i in self.users:
            if i.id == user_id:
                return "This user already exists"
            
        new_user = User(user_id , user_name)
        
        self.users[new_user]=[] 
        self.save_data()
        print("user created successfully")
        
    def borrow_book(self , user_id , book_name):
        found_book=''.join(self.search_for_book(book_name))
        user_found=False

        available_books = []
        for book in self.book:
            if book.name == found_book and book.quantity > 0:
                available_books.append(book)

        if not available_books:
            return print("Insufficient quantity")

        for i , j in self.users.items():
            if i.id == user_id:

                if len(self.users[i]) >= 2:
                    return print("sorry you crossed the limit")

                self.users[i].append(book_name)
                available_books[0].quantity -= 1  
                user_found=True
                self.save_data()

        if not user_found:
            return print("there is no user with this id")

        return print(f"The user {user_id} borrowed {book_name} and the available quantity of this book is {available_books[0].quantity}")
        
    def return_book(self , user_id , book_name):
        found_book=''.join(self.search_for_book(book_name)) # jodi naam 
        user_found=False
        
        available_books = []
        for book in self.book:
             if book.name == found_book :
                available_books.append(book)
        
        if not available_books:
           return print("There is no book in this name")
        
        for i , j in self.users.items():
            if i.id == user_id:

                if not j or book_name not in j:
                    return print("This user did not borrow this book")

                j.remove(book_name)

                if len(j) == 0:
                     self.users[i] = []

                user_found = True
            
                  
        if not user_found: 
            return print("There is no user with this id")
        
        available_books[0].quantity+=1
        self.save_data()
        return print(f"The user {user_id} returned {book_name} and the available quantity of this book is {available_books[0].quantity}")   
    
        # (id , name ) = book1 , book2 -----> users 
          #  i              j
        
    def print_all_users(self):
        all_users = []

        for user in self.users:
             all_users.append(user.name)
        print("working is on admin.py")
        return ", ".join(all_users)
        
    def print_users_borrowed(self):
        users1 = []
        #user_id
        for i in self.users:
            if len(self.users[i]) > 0:
                 users1.append(i)          
        if users1:
            for i in users1:
                print(f'The user {i.name} borrowed the books {" and ".join(self.users[i])}') 
        else :
            print('There are no users borrowed any book')    
        