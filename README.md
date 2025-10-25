# Library Management System 

## Project Overview
This Library_Management_System is a simple yet efficient Python project designed to manage library operations using **dictionaries, lists, and tuples**.  
It allows users to **add, update, delete, search, borrow, and return books**, while maintaining accurate records of members and book availability.

## Project Aim
To design and implement a **Python-based library system** that demonstrates real-world data management concepts using built-in data structures without external databases.

## System Features
1. Add new books and members  
2. Update or delete records  
3. Borrow and return books (max 3 per member)  
4. Prevent duplicate entries  
5. Track available vs. total copies  
6. Enforce borrowing limits  
7. Genre validation via tuple list  

## Entities and Attributes

## Book
- ISBN (unique ID)  
- Title  
- Author  
- Genre  
- Total Copies  
- Available Copies  

## Member
- Member ID (unique ID)  
- Name  
- Email  
- Borrowed Books (list of ISBNs)

## Genre
- Genre Name (stored as tuple of valid genres)

## Data Structure Representation

```python
books = {
    "9781234567890": {
        "title": "Python for Beginners",
        "author": "John Doe",
        "genre": "Non-Fiction",
        "total_copies": 5,
        "available_copies": 5
    }
}

members = [
    {
        "member_id": "M001",
        "name": "Jonathan Moriwah",
        "email": "jonathan@example.com",
        "borrowed_books": []
    }
]

genres = ("Fiction", "Non-Fiction", "Sci-Fi", "Biography", "Children")
```
## Core Functionalities

| **Function** | **Description** |
|---------------|----------------|
| `add_book()` | Add new book to collection |
| `add_member()` | Register new library member |
| `search_books()` | Find books by title, author, or genre |
| `update_book()` | Modify book info safely |
| `update_member()` | Edit member info |
| `borrow_book()` | Allow member to borrow book (limit 3) |
| `return_book()` | Return borrowed book |
| `delete_book()` | Remove book if no copies borrowed |
| `delete_member()` | Remove member if no active loans |

## Testing
Use the included `tests.py` file to run simple validation tests:

```bash
python tests.py
```

---

## Demo
You can explore system usage by running the demo script:

```bash
python demo.py
```

---

## UML Diagram
Below is the class relationship overview between `Book`, `Member`, and `Genre` entities:

```
+-----------+         +-----------+         +----------+
|   Member  | 1..* -> |   Book    | *..1 -> |  Genre   |
+-----------+         +-----------+         +----------+
| member_id |         | ISBN      |         | genre_name |
| name      |         | title     |         +----------+
| email     |         | author    |
| borrowed_books[] |  | genre     |
+-----------+         +-----------+
```

---

## Project Files
| **File** | **Purpose** |
|-----------|-------------|
| `operations.py` | Core functions for managing the system |
| `demo.py` | Demonstration script |
| `tests.py` | Test cases |
| `DesignRationale.txt` | Design explanation |
| `UML.png` | UML class diagram |
| `README.md` | Documentation |

---

## Author
**Jonathan Moriwah**
📍 Limkokwing University of Creative Technology, Sierra Leone  
💻 Software Engineering with Multimedia  

---

## License
This project is open for academic use and demonstration purposes.
