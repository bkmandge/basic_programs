'''
	0	1	2	3	4	5
0	-	-	-	-		p
1	-	-	-	-	y	y
2	-	-	-	t	t	t
3	-	-	h	h	h	h
4	-	o	o	o	o	o
5	n	n	n	n	n	n

'''

str1 = input("enter the string: ")
length = len(str1)

for i in range(length):
    for j in range(length - i - 1): # when row 0 we want 5 spaces, row 1 space = 4 so...
        print("-", end=" ")
    for j in range(i + 1):
        print(str1[i], end=" ")
    print()


'''
     p 
    y y 
   t t t 
  h h h h 
 o o o o o 
n n n n n n
'''
str1 = input("enter the string: ")
length = len(str1)

for i in range(length):
    for j in range(length - i - 1): # when row 0 we want 5 spaces, row 1 space = 4 so...
        print(" ", end="")
    for j in range(i + 1):
        print(str1[i], end=" ")
    print()