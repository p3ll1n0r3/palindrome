#!/usr/bin/env python

# palindrome.py - takes any number serie : start_num and end_number and with a maximum of iterations
#                 for every number, add itself and it's reverse until it reach a palindrome.
#                 it runs until the max_iter value has been reached.
#                 some numbers does not become palindrome : example number 196

import sys

def addreverse(a):
    return a + int(str(a)[::-1])

def donumber(a,max_iter):
    iter = 0
    nums = []

    nums.append(str(a) + ' : ')

    while (str(a) != str(a)[::-1]) and (iter < max_iter):
        a = addreverse(a)
        nums.append(str(a) + ' ')
        iter += 1

    if iter == max_iter:
        nums.append(' : Reached max iterations')
    else:
        nums.append(' : ' + str(iter))

    return nums, iter

# Main starts here

num_iters = []

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print('Start with 3 argumanets : start_number stop_number max_iteration')
        print('Example: ./palindrome.py 100 196 10000')
        print('')
        exit(0)
    else:
        start_num = int(sys.argv[1])
        end_num = int(sys.argv[2]) + 1
        max_iter = int(sys.argv[3])

# for each number , run the adding until it is a palindrome or max_iter has been reached
# print the number and the resulting numbers, with the number of iterations needed
for num in range(start_num,end_num):
    result, iters = donumber(num, max_iter)
    # print(''.join(donumber(num, max_iter)))
    print(''.join(result))
    num_iters.append([num,iters])

# print a summary of each number in the serie, with number of iterations
for num_iter in num_iters:
    print(num_iter)
 
