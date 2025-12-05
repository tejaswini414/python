contacts = {
    'number': 4,
    'students': [
        {'name': 'Alice', 'phone': '123-456-7890'},
        {'name': 'Bob', 'phone': '987-654-3210'},
        {'name': 'Charlie', 'phone': '555-666-7777'},
        {'name': 'Diana', 'phone': '444-555-6666'}]
}
print("Student Contacts:")
for student in contacts['students']:
     print(student['phone'])
