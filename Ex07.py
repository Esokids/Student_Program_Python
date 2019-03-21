lists = list()

while True:
    cmd = input('Enter Command: ')
    if cmd == 'Stop':
        break

    elif cmd == 'Create':
        name = input('Enter Student Name: ')
        id = input('Enter Student ID: ')
        flag = True
        # Check Student ID is unique
        for i in range(len(lists)):
            if id in lists[i].get('id'):
                flag = False
        if flag:
            n = int(input('Enter Your Subject Count: '))
            subjects = dict()
            for i in range(n):
                subject = input(f'Enter Your Name\'s Subject {i+1}: ')
                grade = input(f'Enter Your Grade\'s Subject {i+1}: ')
                subjects[subject] = grade
            lists.append({'id':id, 'name':name, 'subjects':subjects})
        else:
            print('Command Error !!!!. Student is already used')

    elif cmd == 'Grade of Subject':
        subjects = list()
        # Add unique subject
        for i in range(len(lists)):
            for j in lists[i].get('subjects'):
                if j not in subjects:
                    subjects.append(j)
        # Print all unique subject
        for i in subjects:
            print('>>> ',i)
        # Choose subject that you want to know students grade
        subject = input('Enter Subject Name: ')
        if subject in subjects:
            print('Grade of %s: ' % subject)
            for i in range(len(lists)):
                for j in lists[i].get('subjects'):
                    if j == subject:
                        print(f'Student ID: {lists[i].get("id")}, Student Name: {lists[i].get("name")}, Grade: {lists[i].get("subjects").get(subject)}')
        else:
            print('Command Error !!!!. Subject is not exist')

    elif cmd == 'Student Detail':
        students = list()
        # Add student
        for i in range(len(lists)):
            students.append(lists[i].get('id'))
        # Print all student
        for student in students:
            print('>>> ',student)
        # Choose student ID that you want to know about this student
        student = input('Enter Student ID: ')
        if student in students:
            print('Student Detail:')
            for i in range(len(lists)):
                if lists[i].get('id') == student:
                    for j in lists[i].get('subjects'):
                        print(f'Grade of {j}: {lists[i].get("subjects").get(j)}')
        else:
            print('Command Error !!!!. Student is not exist')
