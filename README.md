# remove-contact-from-list-GUI

Remove Contact View will see:
1. The user should be able to search for contacts to be deleted by first name, last name, phone number or email address. Check the "Find Contact" view to see how I did this.
2. If the search returns multiple results, the user should be able to specify which of those results should be deleted.
There are several ways to accomplish this, but as one option look up the Listbox widget available from Tkinter.
https://www.tutorialspoint.com/python/tk_listbox.htm
3. The user should then be able to delete the selected contact (or contacts). It is removed from the contact list and will not show up on future searches.
4. Display the results to the user. Use the Messagebox widget to display the result of the deletion in a pop-up. The message should be: "<First_name> <Last Name> has been removed from the contact list." See the details on the MessageBox widget here: https://www.tutorialspoint.com/python3/tk_messagebox.htm
