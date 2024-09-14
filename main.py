import sys
import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from school.models import Student, Teacher, Schedule, Grade, Class, Subject


while True:
    print("0 - Exit console, 1 - Subject, 2 - Teacher, 3 - Class, 4 - Student, 5 - Schedule, 6 - Grade")
    choise = int(input("Choose one option: "))
    
    if choise == 0:
        break
    
    elif choise == 1:
        s_name = input("Subject name: ")
        
        Subject.objects.create(name = s_name)
        print("Subject created successfully!")
        
    elif choise == 2:
        f = input("Name: ")
        s = input("Surname: ")
        sub = input("Subject: ")
        
        try:
            check_sub = Subject.objects.get(name=sub)
            Teacher.objects.create(name=f, surname=s, subject=check_sub)
            print("Teacher created successfully!")
        except Subject.DoesNotExist:
            print(f"Subject '{sub}' does not exist.")
        
    elif choise == 3:
        n = input("Name: ")
        cg = input("Class Grade: ")
        
        Class.objects.create(name = n, grade = cg)
        print("Class created successfully!")
        
    elif choise == 4:
        n = input("Name: ")
        s = input("Surname: ")
        sc = input("Class: ")
        
        try:
            check_sc = Class.objects.get(name = sc)
            Student.objects.create(name = n, surname = s, students_class = check_sc)
            print("Student created successfully!")
        except Class.DoesNotExist:
            print(f"Class '{sc}' does not exist.")
            
    elif choise == 5:
        d = input("Day Date(Monday, Tuesday, Wednesday, Thursday, Friday): ")
        t = input("Time (HH:MM): ")
        s = input("Subject: ")
        sc = input("Class: ")
        st = input("Teacher's Surname: ")
        
        try:   
            check_s = Subject.objects.get(name=s)
            check_sc = Class.objects.get(name=sc)
            check_st = Teacher.objects.get(surname=st)
            
            Schedule.objects.create(day=d, begining=t, subject=check_s, s_class=check_sc, s_teacher=check_st)
            print("Schedule created successfully!")
            
        except (Subject.DoesNotExist, Class.DoesNotExist, Teacher.DoesNotExist):
            print(f"Class, Subject or Teacher does not exist.")
        
    elif choise == 6:
        sn = input("Student name: ")
        subn = input("Subject name: ")
        g = input("Grade: ")
        d = input("Date (YYYY-MM-DD): ")
        
        try:
            check_student = Student.objects.get(name=sn)
            check_subject = Subject.objects.get(name=subn)
            
            Grade.objects.create(student=check_student, g_subject=check_subject, grade=g, date=d)
            print("Grade added successfully!")
            
        except (Student.DoesNotExist, Subject.DoesNotExist):
            print(f"Subject or Student does not exist.")
    
    else:
        print("Oops! Something went wrong. Try again!")