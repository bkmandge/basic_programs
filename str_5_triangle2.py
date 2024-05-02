'''
	0	1	2	3	4	5
0	p	y	t	h	o	n
1		p	y	t	h	o
2			p	y	t	h
3				p	y	t
4					p	y
5						p


'''

str1 = input("enter string: ")
length = len(str1)

for row in range(length):
    for col in range(row):
        print(" ", end=" ")
    for col in range(length - row):
        print(str1[col], end=" ")
    print()


'''
	0	1	2	3	4	5
0	p	p	p	p	p	p
1		y	y	y	y	y
2			t	t	t	t
3				h	h	h
4					o	o
5						n

'''
print("Another pattern:- ")
str2 = input("enter string: ")
length = len(str2)

for row in range(length):
    for col in range(row):
        print(" ", end=" ")
    for col in range(length - row):
        print(str2[row], end=" ")
    print()


########################################

print("Diamond pattern:- ")
""" Just remove space from columns, from first inner for loop. """

str1 = input("enter string: ")
length = len(str1)

for row in range(length):
    for col in range(row):
        print(" ", end="")
    for col in range(length - row):
        print(str1[col], end=" ")
    print()

##############################################
print("Another diamond pattern:- ")
str2 = input("enter string: ")
length = len(str2)

for row in range(length):
    for col in range(row):
        print(" ", end="")
    for col in range(length - row):
        print(str2[row], end=" ")
    print()
