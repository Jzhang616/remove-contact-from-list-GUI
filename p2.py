#Jason Zhang
#JASZHANG
#ID: 112920652

from tkinter import *
from tkinter import messagebox

contacts = [
    {"first_name": "John", "last_name": "Doe", "phone_number": "123456789", "email": "john@example.com"},
    {"first_name": "Jane", "last_name": "Smith", "phone_number": "987654321", "email": "jane@example.com"},
    {"first_name": "Alice", "last_name": "Johnson", "phone_number": "555555555", "email": "alice@example.com"},
    {"first_name": "Bob", "last_name": "Brown", "phone_number": "111111111", "email": "bob@example.com"},
    {"first_name": "Emily", "last_name": "Davis", "phone_number": "222222222", "email": "emily@example.com"},
    {"first_name": "Michael", "last_name": "Wilson", "phone_number": "333333333", "email": "michael@example.com"},
    {"first_name": "Sophia", "last_name": "Miller", "phone_number": "444444444", "email": "sophia@example.com"},
    {"first_name": "Daniel", "last_name": "Taylor", "phone_number": "555555555", "email": "daniel@example.com"},
    {"first_name": "Olivia", "last_name": "Anderson", "phone_number": "666666666", "email": "olivia@example.com"},
    {"first_name": "David", "last_name": "Clark", "phone_number": "777777777", "email": "david@example.com"}
]

def save_contact():
	global contact_list
	contact_dict = dict()
	for field in contact_fields:
		contact_dict[field] = contact_fields[field].get()
	contact_list.append(contact_dict)
	for field in contact_fields:
		contact_fields[field].set("")

def clear_contact():
	for field in contact_fields:
			contact_fields[field].set("")

def remove_contact():
    selected_contacts = contact_list.curselection()
    if not selected_contacts:
        messagebox.showwarning("No Selection", "Please select a contact to delete.")
        return
    
    confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete the selected contact(s)?")
    if not confirmation:
        return
    
    for index in selected_contacts[::-1]:  # Delete in reverse order to avoid index issues
        contact = contact_list.get(index)
        contact_list.delete(index)
        messagebox.showinfo("Deletion Successful", f"{contact['first_name']} {contact['last_name']} has been removed from the contact list.")

def search_contacts():
    query = search_entry.get().lower()
    matching_contacts = []

    contact_list.delete(0, END)  

    for contact in contacts:
        if (
            query in contact["first_name"].lower() or
            query in contact["last_name"].lower() or
            query in contact["phone_number"] or
            query in contact["email"].lower()
        ):
            matching_contacts.append(contact)
            contact_list.insert(END, contact)  

    if not matching_contacts:
        messagebox.showinfo("No Results", "No matching contacts found.")

root = Tk()
root.title("Remove Contact")

search_frame = Frame(root)
search_frame.pack(pady=10)

search_label = Label(search_frame, text="Search:")
search_label.grid(row=0, column=0)

search_entry = Entry(search_frame, width=30)
search_entry.grid(row=0, column=1, padx=10)

search_button = Button(search_frame, text="Search", command=search_contacts)
search_button.grid(row=0, column=2)

contact_list = Listbox(root, width=50, height=10)
contact_list.pack(pady=10)

delete_button = Button(root, text="Delete", command=remove_contact)
delete_button.pack(pady=10)

root.mainloop()
