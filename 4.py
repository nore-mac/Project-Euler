"""
Project Euler: Problem 4

"A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers."

Easiest immediate solution is by brute force, as the calculations required are simple.
"""
pal_list = []
for i in range(999,100,-1):
    for j in range(999,100,-1):
        if list(str(i*j)) == list(str(i*j))[::-1]:
            pal_list.append(i*j)

print(max(pal_list))