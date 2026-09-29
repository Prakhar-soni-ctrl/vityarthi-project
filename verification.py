import datetime
from datetime import datetime, timedelta

# verification of credentials
book_issuer = ""


def collect_verification():
  global book_issuer
  book_issuer = input("is student or teacher:").strip().lower()
  print("it is :", book_issuer)

  if book_issuer == "student":
    student_ID = input("enter student ID:")
    name = str(input("enter student name:"))
    phone_no = int(input("enter student phone number:"))
    print("student ID number:", student_ID)
    print("student can borrow maximum books: 3 books ")
    print("It can keep book for maximum time: 2 weeks")
    print("student name:", name)
    print("student phone number:", phone_no)
  elif book_issuer == "teacher":
    teacher_ID = input("enter teacher ID:")
    name = str(input("enter teacher name:"))
    phone_no = int(input("enter teacher phone number:"))
    print("teacher name:", name)
    print("teacher ID number:", teacher_ID)
    print("teacher can borrow maximum books: 5 books")
    print("It can keep book for maximum time : 1 month")
    print("teacher phone number:", phone_no)
  else:
    raise ValueError("Please enter 'student' or 'teacher'.")

  return book_issuer