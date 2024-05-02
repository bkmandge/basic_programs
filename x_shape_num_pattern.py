'''
	0	1	2	3	4
0	1				1
1		2		2
2			3
3		4		4
4	5				5

outer for loop - for rows - row 0 col 1, col 2, col 3, col 4..., printing is done row by row
inner for loop - for columns

'''

num = input("enter an odd length number: ")
length = len(num)

for i in range(length):
    for j in range(length):
        if i == j or i + j == length - 1:
            print(num[i], end=" ")
        else:
            print(" ", end=" ")
    print()


'''
	0	1	2	3	4
0	1				5
1		2		4	
2			3		
3		2		4	
4	1				5

'''

for i in range(length):
    for j in range(length):
        if i == j or i + j == length - 1:
            print(num[j], end=" ") # to get same value in column i.e. col 0 - value 1, col 1 - value 2...
        else:
            print(" ", end=" ")
    print()