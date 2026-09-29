import datetime
from datetime import datetime, timedelta
import catalog
import verification

# return and fine system


def return_book(student_ID, name, book_ID, days_allowed=14, issuer_type="student"):
    issue_date_str = input("enter original issue date (YYYY/MM/DD) for return:")
    issue_date = datetime.strptime(issue_date_str, "%Y/%m/%d")
    due_date = issue_date + timedelta(days=days_allowed)

    return_date = input("enter return date(YYYY/MM/DD):")
    return_date = datetime.strptime(return_date, "%Y/%m/%d")

    if return_date <= due_date:
        print("\n[✓][======= Book 'RETURNED' successfully ======]")
        print(" NO FINE REQUIRED!")
        print("\n--------!THANK YOU!---------")
    else:
        if issuer_type == "student":
            fine_amount = 10.0
            id_label = "student_ID"
        else:
            fine_amount = 5.0
            id_label = "teacher_ID"

        extra_days = return_date - due_date
        total_penalty = extra_days.days * fine_amount
        catalog.copies_available += 1
        return_list = [
            f"{id_label}:{student_ID}",
            f"name:{name}",
            f"fine per day: {fine_amount}",
            f"total penalty: {total_penalty}",
            f"copies now available:{catalog.copies_available}",
        ]
        print(*return_list, sep="||")
        print("\n[✓][======= Book 'RETURNED' successfully =======]")
        print(" FINE PAID SUCCESSFULLY !")
        print("\n--------!THANK YOU!---------")


def return_book_for_user():
    if not verification.book_issuer:
        verification.collect_verification()

    if verification.book_issuer == "student":
        student_ID = input("enter student ID for return:")
        book_ID = input("enter book ID for return:")
        name = input("enter student name for return:")
        return_book(student_ID, name, book_ID)
    elif verification.book_issuer == "teacher":
        teacher_ID = input("enter teacher ID for return:")
        book_ID = input("enter teacher ID for return:")
        name = input("enter teacher name for return:")
        return_book(teacher_ID, name, book_ID, days_allowed=30, issuer_type="teacher")
    else:
        raise ValueError("Invalid issuer type.")