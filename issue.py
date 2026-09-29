import datetime
from datetime import datetime, timedelta
import catalog
import verification


def issue_book(student_ID, name, book_ID, days_allowed=14):
    if catalog.copies_available <= 0:
        raise ValueError("No copies available to issue.")

    issue_date = datetime.now()
    due_date = issue_date + timedelta(days=days_allowed)
    catalog.copies_available -= 1

    print("\n[✓][======Book 'ISSUED' successfully======]")
    print("date when book is issued:", issue_date.strftime("%Y/%m/%d"))
    print("date when book has to be retuned:", due_date.strftime("%Y/%m/%d"))
    print("copies left:", catalog.copies_available)
    return due_date


def issue_book_for_user():
    if not verification.book_issuer:
        verification.collect_verification()

    if verification.book_issuer == "student":
        student_ID = input("enter student ID to issue book:")
        book_ID = input("enter book ID to issue:")
        name = input("enter student name for issue:")
        issue_book(student_ID, name, book_ID)
    elif verification.book_issuer == "teacher":
        teacher_ID = input("enter teacher ID to issue book:")
        book_ID = input("enter book ID to issue:")
        name = input("enter teacher name for issue:")
        issue_book(teacher_ID, name, book_ID, days_allowed=30)
    else:
        raise ValueError("Invalid issuer type.")