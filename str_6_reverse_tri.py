'''
	0	1	2	3	4	5
0	n	n	n	n	n	n
1		o	o	o	o	o
2			t	t	t	t
3				h	h	h
4					y	y
5						p


'''

str1 = input("Enter string: ")
length = len(str1)

for row in range(length -1, -1, -1): # default step for range is +1, so took -1 for reverse
    for col in range(length - row - 1):
        print(" ", end=" ")
    for col in range(row + 1):
        print(str1[row], end=" ")
    print()



'''
	0	1	2	3	4	5
0	n	o	h	t	y	p
1		o	h	t	y	p
2			h	t	y	p
3				t	y	p
4					y	p
5						p

'''

str1 = input("Enter string: ")
length = len(str1)

for row in range(length -1, -1, -1): # default step for range is +1, so took -1 for reverse
    for col in range(length - row - 1):
        print(" ", end=" ")
    for col in range(row, -1, -1):
        print(str1[col], end=" ")
    print()