from operations import *

# Load sample data
load_sample_data()

# Test 1: Add and search for a book
add_book("978-0-444", "Mystery Manor", "D. Sleuth", "Mystery", 2)
result = search_books("Mystery Manor", "title")
assert any("Mystery Manor" in b["title"] for _, b in result), "Test 1 failed"

# Test 2: Add member and ensure unique ID
add_member("M003", "Sam Smith", "sam@example.com")
try:
    add_member("M003", "Duplicate", "dup@example.com")
    raise AssertionError("Test 2 failed: duplicate member ID allowed")
except ValueError:
    pass

# Test 3: Borrow book updates availability
borrow_book("M003", "978-0-444")
assert books["978-0-444"]["available_copies"] == 1, "Test 3 failed"
assert "978-0-444" in find_member("M003")["borrowed_books"]

# Test 4: Borrow limit (3 books max)
add_book("978-0-555", "Book A", "Author A", "Fiction", 1)
add_book("978-0-666", "Book B", "Author B", "Fiction", 1)
borrow_book("M003", "978-0-555")
borrow_book("M003", "978-0-666")
add_book("978-0-777", "Book C", "Author C", "Fiction", 1)
try:
    borrow_book("M003", "978-0-777")
    raise AssertionError("Test 4 failed: allowed >3 borrows")
except ValueError:
    pass

# Test 5: Returning a book restores availability
return_book("M003", "978-0-444")
assert books["978-0-444"]["available_copies"] == 2, "Test 5 failed"
assert "978-0-444" not in find_member("M003")["borrowed_books"]

# Test 6: Delete book only when all copies available
add_book("978-0-888", "Disposable", "Author D", "Fiction", 1)
delete_book("978-0-888")

# Test 7: Delete member only when no borrowed books
add_member("M010", "ToDelete", "del@example.com")
delete_member("M010")

print("✅ All tests passed successfully!")
