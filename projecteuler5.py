# Karen Alves 2018-03-11
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# Week 5 Exercise Project Euler 5
# https://projecteuler.net/problem=5

for i in range (2520,99999999999999999999, 2520):  #as the next number will be a multiple of 2520 and the first number would be bigger than 2520
  count=0
  for j in range (11,21):
    if i % j != 0:
      count = count+1
  if count == 0:
    print(i)
    break

