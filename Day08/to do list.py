tasks = []
q = int(input('enter theno.of tasks you want to perform: '))
for a in range(q):
    tsk = input('Enter the task you want to perform: ')
    tasks.append(tsk)
print(tasks)

k = 1
for tsk in tasks:                   
       print(k,'.',i)               
       k+=1                         
       
index = int(input('Enter the number of which task you want to remove: '))
index = index - 1
if index >= 0 and index < len(tasks):
    tasks.pop(index)
    print(tasks)
else:
    print('enter correct number')

    '''

'''
values = input('enter words seperated by space: ')
s = set(int (x) for x in values.split())
print(s)