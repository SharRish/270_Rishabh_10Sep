'''
1. Implement palindrome using iterator(for loop) and generator mechanism.
'''
print("================Program 1================")
print("========Using Iterator========")
def isPal(s1):
	rev = ''.join(reversed(s1))

	if (s1 == rev):
		return True
	return False

# testing the code
s1 = str(12321)
res = isPal(s1)
# s1 = "123456"
# res = isPal(s1)

if(res):
	print("Given input", s1, "is a Palindrome")
else:
	print("Given input", s1, "is not a Palindrome")

print("========Using Generator========")
def isPal(s1):
	rev = ''.join(reversed(s1))

	if (s1 == rev):
		yield True
	yield False

# testing the code
s1 = "babbab"
res = isPal(s1)
# s1 = "baba"
# res = isPal(s1)

if(res):
	print("Given input", s1, "is a Palindrome")
else:
	print("Given input", s1, "is not a Palindrome")
print("--------------------------------------------------------------------------------------------")

'''
2. 2. Sum of 2 digits into output
		n1 = 1234 # int(input("Enter number1 :" ))
		n2 = 9999 # int(input("Enter number2 :" ))
		Output: 9+1 2+9 3+9 4+9 
		        10 + 11 + 12 + 13
    			  46
'''
print("================Program 2================")

num1 = input("Enter first number:")
num2 = input("Enter second number:")

num1 = list(num1)
num2 = list(num2)

out_sum = []
n = 0
for i in num1:
    res = int(i) + int(num2[n])
    out_sum.append(res)
    n += 1

print("Final sum of both given numbers is:", sum(out_sum))
print("--------------------------------------------------------------------------------------------")

'''
3. st = "ab@#cd!ef"
   Reverse string considering only alphabets. Symobls should not be reversed
   # Output: fe@#dc!ba
'''
print("================Program 3================")

def rev_str(st):
    out = []
    for char in st:
        if char.isalpha():
            out.append(char)
    result = ''
    for char in st:
        if char.isalpha():
            result += out.pop()
        else:
            result += char
    return result

st = "ab@#cd!ef"
print("Original string:", st, "\nReversed string without symbol reversal:", rev_str(st))
print("--------------------------------------------------------------------------------------------")

'''
4. some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
   Find the duplicate count output in dict format.
'''
print("================Program 4================")

from collections import Counter

some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]

counts = dict(Counter(some_list))
duplicates = {key:value for key, value in counts.items() if value > 1}
print("Count of characters and their duplicates are:\n", duplicates)
print("--------------------------------------------------------------------------------------------")

'''
5. t1 = (1, 2, 3, "a", "c") 
   t2 = ("b", "d", 9, 8, 7)
   Output: (10,10,10,"ab","cd")
'''
print("================Program 5================")

t1 = (1, 2, 3, "a", "c") 
t2 = ("b", "d", 9, 8, 7)

l1 = []
l2 = []

for ele in t1:
    if isinstance(ele, int):
        for i in t2:
            if i not in l2 and isinstance(i, int):
                l2.append(i)
                l1.append((ele + i))
    else:
        for i in t2:
            if i not in l2 and isinstance(i, str):
                l2.append(i)
                l1.append((ele + i))

tt = tuple(l1)        # converting output list to tuple

print("Input:", t1, "\n      ",t2)
print("Output:", tt)
print("--------------------------------------------------------------------------------------------")

'''
6. Write a Python program to remove leading zeros from an IP address.
'''
print("================Program 6================")

def removeLeadZero(inp):
   zeroip = ".".join([str(int(i)) for i in inp.split(".")])
   return zeroip

inp = "216.08.094.196"
print("IP address:", inp, "\nIP address post removal of leading zeroes:",removeLeadZero(inp))
print("--------------------------------------------------------------------------------------------")

'''
7. Flattening of list
Input = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
Output = [1,2,3,4,5,6,7,8,9,10]
'''
print("================Program 7================")

inp_l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
out_l = []
 
def flatLst(l):
    for i in l:
        if type(i) == list:
            flatLst(i)
        else:
            out_l.append(i)
 
print("Original List:", inp_l)
flatLst(inp_l)
print("Flattened List:", out_l)
print("--------------------------------------------------------------------------------------------")

'''
8. Load sample content in text file. Read data and find
   1. No of lines in file
	2. No of words in each line 
	3. No of chars in each line
	4. No of vowels and consonants
	5. No of special chars linewise and total 
'''

print("================Program 8================")

with open('F:\Coding Problems\PyNative\cc.txt', 'r') as data:
    data = data.readlines()
    print("========8.1========\nNumber of lines in the text file:", len(data))


with open('F:\Coding Problems\PyNative\cc.txt', 'r') as data:
    data = data.readlines()
print("========8.2========")
c = 1
for line in data:
    line = line.split(' ')
    print(f"Number words in line {c}: {len(line)}")
    c += 1


with open('F:\Coding Problems\PyNative\cc.txt', 'r') as data:
    data = data.readlines()
print("========8.3========")
c = 0
l = 1
for i in range(1, len(data)+1):
    with open('F:\Coding Problems\PyNative\cc.txt', 'r') as data:
        data = data.readline()
        for char in data:
            if char.isalpha:
                c += 1
        print(f"Number of characters in line {l}: {c}")
        l += 1


with open('F:\Coding Problems\PyNative\cc.txt', 'r') as data:
    data = data.read()
print("========8.4========")
vow = 'aeiou'
sc = '\.n'
vow_count = 0
con_count = 0
for char in data:
    if char in vow:
        vow_count += 1
    elif char in sc:
        continue
    else:
        con_count += 1

print(f"Total number of vowels: {vow_count}")
print(f"Total number of consonants: {con_count}")


with open('F:\Coding Problems\PyNative\cc.txt', 'r') as data:
    data = data.read()
print("========8.5========")
spec_count = 0
for char in data:
   spec_count += sum(not x.isalnum() for x in char)

print(f"Total number of special characters: {spec_count}")

# with open('F:\Coding Problems\PyNative\cc.txt', 'r') as data:
#     data = data.readlines()
# print("========8.5========")
# spec_count = 0
# l = 1
# for i in range(1, len(data)+1):
#     with open('F:\Coding Problems\PyNative\cc.txt', 'r') as data:
#         data = data.readline()
#         for char in data:
#             spec_count += sum(not x.isalnum() for x in char)
#             spec_count += 1
#         print(f"Number of characters in line {l}: {spec_count}")
#         l += 1