book_ID = ""
book_title = ""
book_author = ""
Total_copies = 0
copies_issued = 0
copies_available = 0


def add_book():
    global book_ID, book_title, book_author, Total_copies, copies_issued, copies_available
    book_ID = input("enter book ID:")
    book_title = input("enter book title:")
    book_author = input("enter book author:")
    Total_copies = int(input("enter total copies:"))
    copies_issued = int(input("enter copies issued:"))
    copies_available = Total_copies - copies_issued

    print("\n**********STATUS OF BOOK**********")
    List1 = [
        f"book ID: {book_ID}",
        f"title of book: {book_title}",
        f"author of book: {book_author}",
        f"copies available in library: {copies_available}",
    ]
    print(*List1, sep="\n")
    return copies_available