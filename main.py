import verification
import catalog
import issue
import return_fine


if __name__ == "__main__":
    verification.collect_verification()
    catalog.add_book()

    action = input("Do you want to issue or return a book? (issue/return): ").strip().lower()
    if action == "issue":
        issue.issue_book_for_user()
    elif action == "return":
        return_fine.return_book_for_user()
    else:
        print("Invalid action. Please choose 'issue' or 'return'.")