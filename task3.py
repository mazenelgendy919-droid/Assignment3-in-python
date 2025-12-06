contacts = {"mazen": "01011112222", "ahmed": "01033334444", "sara": "01055556666"}
print(contacts.keys())
search_name = input("Enter the name to search for: ")
if search_name in contacts:
    print(f"the ohone number of {search_name} is {contacts[search_name]}")
else:
    print(f"{search_name} not found in contacts")