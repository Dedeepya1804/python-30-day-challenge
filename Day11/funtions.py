student = {}


def add_std():
    name = input('enter the student name: ')
    stu = {}
    n = int(input('how many no.of sub marks u want to enter: '))
    for i in range(0,n):
        subject = input('enter the subject: ')
        marks = int(input('enter the marks: '))
        stu[subject] = marks
        student[name] = stu 
    print('student detail entered successfully') 
    print(student) 
        
def view_std():
    print(student.items())
    
def search_std():
    name = input('enter name u want to search: ')
    if name in student:
        print(student.get(name))
        
def cal_res():
    name = input('enter the name of student you want to calculate: ')
    if name in student:
        marks = student[name].values()
        total = sum(marks)
        avg = total/len(marks)
        print('total: ' , total)
        print('average: ' , avg)
    
while True:
    print('1.add student')
    print('2.display student')
    print('3.search student')
    print('4.result')


    choice = input('enter your choice: ')

    if choice == '1':
        add_std()
    elif choice == '2':
        view_std()
    elif choice == '3':
        search_std()
    elif choice == '4':
        cal_res()
    elif choice == '5:
        break
        
    else:
        print('invalid')
       
