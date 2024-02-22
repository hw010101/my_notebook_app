# notebook.py

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
        if not self.notes:
            print("No notes available.")
        else:
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
