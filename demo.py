from operations import *

def show_books():
    print("\n--- Books ---")
    for isbn, b in books.items():
        print(f"{isbn}: {b['title']} | {b['author']} | {b['genre']} | Total: {b['total_copies']} | Available: {b['available_copies']}")

def show_members():
    print("\n--- Members ---")
    for m in members:
        print(f"{m['member_id']}: {m['name']} | {m['email']} | Borrowed: {m['borrowed_books']}")

if __name__ == "__main__":
    print("📚 Loading sample data...")
    load_sample_data()
    show_books()
    show_members()

    print("\n🔍 Search for 'Python':")
    print(search_books("Python", "title"))

    print("\n👤 M001 borrows 'Python Basics'...")
    borrow_book("M001", "978-0-111")
    show_members()
    show_books()

    print("\n📦 Returning 'Python Basics'...")
    return_book("M001", "978-0-111")
    show_members()
    show_books()
