"""
Prob 1 : Write a program that takes an integer, then a string, then a char from the user and prints them in the screen.

Input:  2 Name y
Expected Output:
2
Name
y

int_in = int(input())
str_in = int(input())
char_in = int(input())

# Getting inputs in a single line

int_in, str_in, char_in = input().split()
int_in = int(int_in)

print(int_in)
print(str_in)
print(char_in)


Prob 2: Write a program to check whether a triangle can be formed with the given values for the angles.

If sum of angles is equal to 180, then triangle can be formed, else it can't be formed.

Input: 45 45 45

Expected Output: 
Triangle cannot be formed

Explanation -> We are getting 3 inputs, that is three angles of triangle, but here the sum of three angles that is 45+45+45 is not equal to 180 so Triangle cannot be formed is the output.


a = int(input())
b = int(input())
c = int(input())

if a+b+c == 180:
    print("Triangle be formed")

else:
    print("Triangle cannot be formed")



#####################################################################################



Prob 3: 

Given mark of student, Print the Grade

Grade A if mark is greater than or equal to 90

Grade B if mark is greater than or equal to 80

Grade C if mark if greater than or equal to 60

Grade D if mark if greaer than or equal to 35

Fail if mark is lesser than 35


Input: 95

Expected Output:

Grade A

Explanation: Here 95 is greater than or equal to 90 so its Grade A

mark=int(input("Enter your mark:"))

if mark >= 90:
    print("Grade A")

elif mark >= 80 and mark < 90:
    print("Grade B")

elif mark >= 60 and mark < 80:
    print("Grade C")

elif mark >= 35 and mark < 60:
    print("Grade D")

else:
    print("Fail")



Prob 4: Write a program using switch case which takes a value and prints the respective Size.
If size is 29 then its small

If size is 30 then its Medium

If size is 38 then its Large

If size is 42 then its XLarge

If size is not any of the above then Invalid.


Input: 29
Expected Output: 
Small

"""

size=int(input("Enter your size:"))

if size == 29:
    print("Small")

elif size == 30:
    print("Medium")

elif size == 38:
    print("Large")

elif size == 42:
    print("X Large")

else:
    print("Invalid")