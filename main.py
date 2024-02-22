# main.py

from notebook import NoteBook

def main():
    note_book = NoteBook()

    note_book.load_notes()

    while True:
        print("\nNotebook Menu:")
        print("1. Show All Notes")
        print("2. Add New Note")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("Enter an option (1/2/3/4): ")

        if choice == "1":
            note_book.show_notes()
        elif choice == "2":
            title = input("Note Title: ")
            content = input("Note Content: ")
            note_book.add_note(title, content)
        elif choice == "3":
            note_book.show_notes()
            index = int(input("Enter the index of the note to delete: "))
            note_book.delete_note(index)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
