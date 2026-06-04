import sys


def print_header(title):
    """Helper to keep the UI looking consistent and clean."""
    print(f"\n{'=' * 40}")
    print(f" {title.upper()} ".center(40, "-"))
    print(f"{'=' * 40}")


class ContactBook:

    def __init__(self):
       
        self.contacts = []

    def add_contact(self):
        print_header("Add New Contact")

        name = input("Enter Store Name: ").strip()
        if not name:
            print("❌ Store name is required!")
            return

        phone = input("Enter Phone Number: ").strip()
        email = input("Enter Email Address: ").strip()
        address = input("Enter Physical Address: ").strip()

        
        new_contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address,
        }

        self.contacts.append(new_contact)
        print(f"\n✅ Success: '{name}' has been added to your contacts.")

    def view_all_contacts(self):
        print_header("Saved Contacts")

        if not self.contacts:
            print("Your contact list is currently empty.")
            return

       
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}. {contact['name']} | Ph: {contact['phone']}")

    def search_contact(self):
        print_header("Search Contacts")

        if not self.contacts:
            print("No contacts available to search.")
            return

        query = input("Enter name or phone number to look up: ").strip().lower()

        if not query:
            print("Search query cannot be empty.")
            return

        results = []
        for contact in self.contacts:
           
            if (
                query in contact["name"].lower()
                or query in contact["phone"].lower()
            ):
                results.append(contact)

       
        if results:
            print(f"\nFound {len(results)} matching contact(s):")
            for contact in results:
                print("-" * 30)
                print(f"Store Name : {contact['name']}")
                print(f"Phone      : {contact['phone']}")
                print(f"Email      : {contact['email']}")
                print(f"Address    : {contact['address']}")
            print("-" * 30)
        else:
            print("No matching contacts found.")

    def update_contact(self):
        print_header("Update Contact Info")

        if not self.contacts:
            print("No contacts to update.")
            return

        name_to_find = (
            input("Enter the exact Store Name you want to update: ")
            .strip()
            .lower()
        )

     
        target_index = None
        for i, contact in enumerate(self.contacts):
            if contact["name"].lower() == name_to_find:
                target_index = i
                break

        if target_index is None:
            print("Contact not found. Make sure the spelling matches exactly.")
            return

        contact = self.contacts[target_index]
        print(f"\nFound profile for '{contact['name']}'.")
        print("Press [Enter] to keep the current value unchanged.\n")

    
        new_name = input(f"Store Name [{contact['name']}]: ").strip()
        if new_name:
            contact["name"] = new_name

        new_phone = input(f"Phone [{contact['phone']}]: ").strip()
        if new_phone:
            contact["phone"] = new_phone

        new_email = input(f"Email [{contact['email']}]: ").strip()
        if new_email:
            contact["email"] = new_email

        new_address = input(f"Address [{contact['address']}]: ").strip()
        if new_address:
            contact["address"] = new_address

        print("\n✅ Contact details successfully updated!")

    def delete_contact(self):
        print_header("Delete a Contact")

        if not self.contacts:
            print("No contacts available to delete.")
            return

        name_to_find = (
            input("Enter the exact Store Name to delete: ").strip().lower()
        )

        for i, contact in enumerate(self.contacts):
            if contact["name"].lower() == name_to_find:
               
                confirm = (
                    input(
                        f"Are you sure you want to delete '{contact['name']}'? (yes/no): "
                    )
                    .strip()
                    .lower()
                )
                if confirm in ["y", "yes"]:
                    self.contacts.pop(i)
                    print("\n🗑️ Contact deleted successfully.")
                else:
                    print("\nDeletion cancelled.")
                return

        print("Contact not found.")


def main():
    
    book = ContactBook()

    while True:
        print_header("Main Menu")
        print("1. Add New Contact")
        print("2. View All Contacts (Names & Phones)")
        print("3. Search for a Contact")
        print("4. Update Existing Contact")
        print("5. Delete a Contact")
        print("6. Exit Program")

        choice = input("\nSelect an option (1-6): ").strip()

        if choice == "1":
            book.add_contact()
        elif choice == "2":
            book.view_all_contacts()
        elif choice == "3":
            book.search_contact()
        elif choice == "4":
            book.update_contact()
        elif choice == "5":
            book.delete_contact()
        elif choice == "6":
            print("\nShutting down. Goodbye!")
            sys.exit()
        else:
            print("\n❌ Invalid choice! Please type a number between 1 and 6.")

       
        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()
