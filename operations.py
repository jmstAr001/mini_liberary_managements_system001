# Define a tuple for valid genres
VALID_GENRES = ("Fiction", "Non-Fiction", "Sci-Fi", "Fantasy", "Biography", "Mystery", "Romance")

# Books dictionary: ISBN -> book details
books = {}
# Members list: each member is a dictionary
members = []

# ---------------- Core Helper ----------------
def find_member(member_id):
    """Find a member by ID."""
    for m in members:
        if m["member_id"] == member_id:
            return m
    return None

# ---------------- CRUD for Books ----------------
def add_book(isbn, title, author, genre, total_copies):
    """Add a book if ISBN is unique and genre is valid."""
    if isbn in books:
        raise ValueError(f"ISBN {isbn} already exists.")
    if genre not in VALID_GENRES:
        raise ValueError(f"Invalid genre. Valid options: {VALID_GENRES}")
    if total_copies < 1:
        raise ValueError("Total copies must be at least 1.")
    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": int(total_copies),
        "available_copies": int(total_copies)
    }
    return books[isbn]

def update_book(isbn, **kwargs):
    """Update details of an existing book."""
    if isbn not in books:
        raise KeyError(f"Book {isbn} not found.")
    book = books[isbn]
    if "genre" in kwargs and kwargs["genre"] not in VALID_GENRES:
        raise ValueError("Invalid genre.")
    if "total_copies" in kwargs:
        new_total = int(kwargs["total_copies"])
        borrowed = book["total_copies"] - book["available_copies"]
        if new_total < borrowed:
            raise ValueError("New total cannot be less than borrowed copies.")
        book["available_copies"] = new_total - borrowed
        book["total_copies"] = new_total
    for key in ("title", "author", "genre"):
        if key in kwargs:
            book[key] = kwargs[key]
    return book

def delete_book(isbn):
    """Delete a book only if no copies are borrowed."""
    if isbn not in books:
        raise KeyError("Book not found.")
    book = books[isbn]
    borrowed = book["total_copies"] - book["available_copies"]
    if borrowed > 0:
        raise ValueError("Cannot delete book while copies are borrowed.")
    del books[isbn]
    return True

# ---------------- CRUD for Members ----------------
def add_member(member_id, name, email):
    """Add a new member if ID is unique."""
    if find_member(member_id):
        raise ValueError("Member ID must be unique.")
    member = {"member_id": member_id, "name": name, "email": email, "borrowed_books": []}
    members.append(member)
    return member

def update_member(member_id, **kwargs):
    """Update member details."""
    m = find_member(member_id)
    if not m:
        raise KeyError("Member not found.")
    for key in ("name", "email"):
        if key in kwargs:
            m[key] = kwargs[key]
    return m

def delete_member(member_id):
    """Delete a member only if they have no borrowed books."""
    m = find_member(member_id)
    if not m:
        raise KeyError("Member not found.")
    if m["borrowed_books"]:
        raise ValueError("Cannot delete member with borrowed books.")
    members.remove(m)
    return True

# ---------------- Search ----------------
def search_books(query, by="title"):
    """Search for books by title, author, or genre."""
    q = query.strip().lower()
    results = []
    for isbn, b in books.items():
        if by == "title" and q in b["title"].lower():
            results.append((isbn, b))
        elif by == "author" and q in b["author"].lower():
            results.append((isbn, b))
        elif by == "genre" and q == b["genre"].lower():
            results.append((isbn, b))
    return results

# ---------------- Borrow / Return ----------------
def borrow_book(member_id, isbn):
    """Member borrows a book (max 3 books per member)."""
    m = find_member(member_id)
    if not m:
        raise KeyError("Member not found.")
    if isbn not in books:
        raise KeyError("Book not found.")
    if len(m["borrowed_books"]) >= 3:
        raise ValueError("Member has reached borrow limit (3 books).")
    book = books[isbn]
    if book["available_copies"] <= 0:
        raise ValueError("No available copies left.")
    book["available_copies"] -= 1
    m["borrowed_books"].append(isbn)
    return True

def return_book(member_id, isbn):
    """Return a borrowed book."""
    m = find_member(member_id)
    if not m:
        raise KeyError("Member not found.")
    if isbn not in m["borrowed_books"]:
        raise ValueError("Member did not borrow this book.")
    m["borrowed_books"].remove(isbn)
    books[isbn]["available_copies"] += 1
    return True

# ---------------- Sample Data ----------------
def load_sample_data():
    """Load some sample data for testing/demo."""
    books.clear()
    members.clear()
    add_book("978-0-111", "Python Basics", "Alice Smith", "Non-Fiction", 3)
    add_book("978-0-222", "Deep Space", "Bob Star", "Sci-Fi", 2)
    add_book("978-0-333", "Love in Time", "C. Heart", "Romance", 1)
    add_member("M001", "John Doe", "john@example.com")
    add_member("M002", "Jane Roe", "jane@example.com")
