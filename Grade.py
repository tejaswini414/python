grade = {
    'subject': 'python',
    'students': [
        {'name': 'Alice', 'score': 55},
        {'name': 'Bob', 'score': 75},
        {'name': 'Charlie', 'score': 45}
    ]
}
print(f"\n{grade['subject']} -grade report:")
for student in grade['students']:
    print(student['name'], "Pass" if student['score'] >= 50 else "Fail")

    