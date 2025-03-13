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



    {
        'first_name': 'Mert',
        'last_name': 'Kaya',
        'index_number': '45001',
        'nationality': 'Turkish',
        'starting_date': '3/10/2025',
        'courses': ['Computer Science', 'Mathematics']
    },
    {
        'first_name': 'Anna',
        'last_name': 'Kowalska',
        'index_number': '45002',
        'nationality': 'Polish',
        'starting_date': '3/12/2025',
        'courses': ['Physics', 'Chemistry']
    },
    {
        'first_name': 'Luca',
        'last_name': 'Rossi',
        'index_number': '45003',
        'nationality': 'Italian',
        'starting_date': '3/15/2025',
        'courses': ['History', 'Philosophy']
    }
]

for student in students:
    print(f"Name: {student['first_name']} {student['last_name']}, Index Number: {student['index_number']}")
