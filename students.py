first_name = "Eren"
last_name = "Caglar"
idnex_number = "35095"
nationality = "Turkish"
starting_date = "03/13/2025"
courses = ["Computer science"] 


print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Index Number: {index_number}")
print(f"Nationality: {nationality}")
print(f"Starting Date: {starting_date}")
print(f"Courses: {', '.join(courses)}")


# List containing student dictionaries
students = [
    {
        'first_name': 'Oliver',
        'last_name': 'Johnson',
        'index_number': '66001',
        'nationality': 'Canadian',
        'starting_date': '3/10/2025',
        'courses': ['Computer Science', 'Mathematics']
    },
    {
        'first_name': 'Emma',
        'last_name': 'Garcia',
        'index_number': '66002',
        'nationality': 'Spanish',
        'starting_date': '3/12/2025',
        'courses': ['Physics', 'Biology']
    },
    {
        'first_name': 'Noah',
        'last_name': 'Kim',
        'index_number': '66003',
        'nationality': 'Korean',
        'starting_date': '3/15/2025',
        'courses': ['History', 'Philosophy']
    }
]

# Print each student's name and index number
for student in students:
    print(f"Name: {student['first_name']} {student['last_name']}, Index Number: {student['index_number']}")


