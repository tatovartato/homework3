from django.shortcuts import render
import random

def get_random_students():
    names = ["mariami", "ana", "barbare", "lulu", "vaso", "doi", "gio", "andria", "niko", "data"]
    surnames = ["Nikolashvili", " Managadze", "Narmania", "Tchikadze", "gelashvili", "maxaradze", "angisa", "messi", "elia", "tutashxia"]
    students = []

    for _ in range(1,101):
        student = {
            'name': random.choice(names),
            'surname': random.choice(surnames),
            'gpa': round(random.uniform(1.0, 4.0), 1),
            'course': random.randint(1, 4)
        }
        students.append(student)

    return students

def students_page_view(request):
    students = get_random_students() 
    return render(request, 'students_page.html', {'students': students})


def main_page_view(request):
    students = get_random_students()
    student = random.choice(students)
    return render(request, 'main_page.html', {'student': student})