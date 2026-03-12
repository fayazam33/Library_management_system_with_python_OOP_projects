# Library_management_system_with_python_OOP_projects
📚 Library Management System (Python OOP)

A simple Library Management System built using Object-Oriented Programming (OOP) in Python.
This project simulates a basic library where an admin can manage books and users, and users can borrow and return books.

The system stores data persistently using a JSON file, allowing the program to retain library data even after it closes.

🚀 Features
📖 Book Management

Add new books to the library

View all available books

Search books by prefix

Track available book quantity

👤 User Management

Add new users

View all active users

🔄 Borrow / Return System

Borrow books (maximum 2 books per user)

Return borrowed books

Track which user borrowed which book

💾 Data Persistence

Library data is stored in library.json

Books and user records automatically load when the program starts

Data automatically saves after every change

🏗️ Project Structure
Library_management_system/
│
├── admin.py          # Core library logic
├── operations.py     # Menu system and user interaction
├── book.py           # Book class
├── user.py           # User class
├── library.json      # Persistent storage for books and users
└── main.py           # Program entry point
⚙️ Technologies Used

Python 3

Object-Oriented Programming (OOP)

JSON for data storage

Standard Python libraries:

json

os

🧠 OOP Concepts Used

This project demonstrates several important OOP principles:

Classes & Objects

Encapsulation

Modular Design

Separation of Concerns

Classes used in the project:

Book

User

admin

operations

📋 Program Menu

When the program runs, the following options appear:

1) Add Book
2) Print Library Books
3) Search a Specific Book
4) Add User
5) Borrow Book
6) Return Book
7) Print Users Borrowed Books
8) Print All Active Users
9) 
▶️ How to Run the Project
'''
1️⃣ Clone the repository
git clone https://github.com/fayazam33/Library_management_system_with_python_OOP_projects.git
'''
2️⃣ Navigate to the project folder
cd Library_management_system_with_python_OOP_projects

3️⃣ Run the program
python main.py

💾 Example Data Format (library.json)
{
  "books": [
    {
      "id": "1",
      "name": "Python Programming",
      "quantity": 3
    }
  ],
  "users": [
    {
      "id": 101,
      "name": "Alice",
      "borrowed": ["Python Programming"]
    }
  ]
}
📌 System Rules

A user can borrow maximum 2 books

Books must be available in quantity to be borrowed

Users can only return books they borrowed

Book search works using prefix matching

🎯 Learning Objectives

This project was created to practice:

Python Object-Oriented Programming

Data persistence using JSON

CLI-based program design

Modular project architecture
