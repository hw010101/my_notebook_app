import os

class NoteBook:
    def __init__(self, file_name="notes.txt"):
        self.file_name = file_name
        self.notes = []

    def load_notes(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                for line in file.readlines():
                    title, content = line.strip().split("|")
                    self.notes.append({"title": title, "content": content})
        except FileNotFoundError:
            pass

    def show_notes(self):
        for index, note_info in enumerate(self.notes, 1):
            print(f"{index}. Title: {note_info['title']}")
            print(f"   Content: {note_info['content']}")
            print("-" * 30)

    def add_note(self, title, content):
        self.notes.append({"title": title, "content": content})
        self.save_notes()

    def delete_note(self, index):
        if 1 <= index <= len(self.notes):
            deleted_note = self.notes.pop(index - 1)
            print(f"Note with title '{deleted_note['title']}' deleted.")
            self.save_notes()
        else:
            print("Invalid note index.")

    def save_notes(self):
        with open(self.file_name, "w", encoding="utf-8") as file:
            for note_info in self.notes:
                file.write(f"{note_info['title']}|{note_info['content']}\n")

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
