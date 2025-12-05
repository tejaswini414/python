library = {
    'book_avaliable': 2,
    'collection': [
        {'book_id': 201, 'title': '1984', 'author': 'George Orwell', 'available': True},
        {'book_id': 202, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'available': False}
    ]
}
print("library book details:")
for book in library['collection']:
    if book['available']:
        status = "Available"
    else:
        status = "Not Available"
    print(f"\nbook id: {book['book_id']}\ntitle: {book['title']}\nauthor: {book['author']}\nstatus: {status}")