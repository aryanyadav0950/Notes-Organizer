# Notes Organizer 

import os

FILE_NAME = "notes.txt"


def add_note():
    print("\n--- Add Note ---")
    title = input("Enter note title: ")
    content = input("Enter note content: ")

    with open(FILE_NAME, "a") as f:
        f.write(f"{title}|{content}\n")

    print("✔ Note added successfully!\n")


def view_notes():
    print("\n--- All Notes ---")
    if not os.path.exists(FILE_NAME):
        print("No notes found.\n")
        return

    with open(FILE_NAME, "r") as f:
        lines = f.readlines()

    if not lines:
        print("No notes available.\n")
        return

    for line in lines:
        title, content = line.strip().split("|")
        print(f"Title: {title}")
        print(f"Content: {content}")
        print("-----------------------------")

    print()


def search_note():
    print("\n--- Search Note ---")
    search_title = input("Enter title to search: ").lower()

    if not os.path.exists(FILE_NAME):
        print("No notes found.\n")
        return

    with open(FILE_NAME, "r") as f:
        lines = f.readlines()

    found = False
    for line in lines:
        title, content = line.strip().split("|")
        if title.lower() == search_title:
            print("\nNote Found:")
            print(f"Title: {title}")
            print(f"Content: {content}\n")
            found = True

    if not found:
        print("No note found with that title.\n")


def delete_note():
    print("\n--- Delete Note ---")
    del_title = input("Enter title to delete: ").lower()

    if not os.path.exists(FILE_NAME):
        print("No notes found.\n")
        return

    with open(FILE_NAME, "r") as f:
        lines = f.readlines()

    new_lines = []
    deleted = False

    for line in lines:
        title, content = line.strip().split("|")
        if title.lower() == del_title:
            deleted = True
            continue
        new_lines.append(line)

    with open(FILE_NAME, "w") as f:
        f.writelines(new_lines)

    if deleted:
        print("✔ Note deleted successfully!\n")
    else:
        print("No note found with that title.\n")


def main_menu():
    while True:
        print("===== NOTES ORGANIZER =====")
        print("1. Add Note")
        print("2. View All Notes")
        print("3. Search Note")
        print("4. Delete Note")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            search_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main_menu()
