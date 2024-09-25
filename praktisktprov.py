#author: Samuel Nyberg
#Date: 2024-09-25


myList = []

myList.append(input("ange dina värden")) 

x = str(myList)
print(f'{x[2]}')

c = len(x)
if c < 2:
    for i in range(11):
        b = int(x[2])*i
        print(f'{x[2]} * {i} = {b}')
elif c > 2 < 5:   
    for i in range(11):
        b = int(x[4])*i
        print(f'{x[4]} * {i} = {b}')

#Funkar ej men gav det mitt bästa försök :)