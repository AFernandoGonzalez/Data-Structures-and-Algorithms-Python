

# Strings ############################################################
# greet = 'hello world'
# print(greet[1])
# print(greet[0:8])
# print(greet[0:8:2])
# print(greet[0::2])
# print(greet[1+2])
# print(greet[len(greet)-1])
# # print(len(greet)-1)

# print('For Loop String')
# for i in enumerate(greet[0:5]):
#     print(i)

# ins_value = greet[:5] + ' universe and' + greet[5:]
# print(ins_value)


# x='3'
# y='2'
# # sum = x+y
# sum = int(x) + int(y)
# print(sum) 


# Lists ############################################################

# x = 1
# y = 2
# z = 3

# list1 = [x,y,z]
# list2 = list1
# print(list1)
# list2[1] = 4
# print(list1)

# items = [["rice", 2.4, 8], ["flour", 1.9, 5], ['corn', 4.7, 6]]
# # for item in items:
# #     print("Product: %s Price : %.2f Quality: %i" % (item[0], item[1], item[2] ))

# # same for loop as above
# for item in items:
#     print( f"Product: {item[0]}, Price: {item[1]}, Quality: {item[2]}")

# # items[1][1] = items[1][1] * 1.2
# items[0][1] = items[0][1] * 1.2
# print(items)


# l = [2,4,8,16]
# for i in l:
#     print(i**3)


# def f1(x): 
#     return x*2

# def f2(x): 
#     return x*4

# lst = []
# for i in range(16):
#     lst.append(f1(f2(i)))

# print(lst)
# print([f1(x) for x in range(64) if x in [f2(j) for j in range(16)]])


# list1 = [[1,2,3], [4,5,6]]

# [i * j for i in list1[0] for j in list1[1]]

# for i in list1[0]:
#     for j in list1[1]:
#         print([i*j])


# words = 'Here is a sentence'.split()
# for word in words:
#     print([word, len(word)])



# Functions as first class objects
# def greeting(language):
#     if language == 'eng':
#         return 'hello world'
#     elif language =='fr':
#         return 'Bonjour le mode'
#     else:
#         return 'Language not supported'


# l = [greeting('eng'), greeting('fr'), greeting('ger')]
# l = l[1]
# print(l)



# Higher order functions
# list = [1,2,3,4]

# for item in map(lambda n: n*2, list): 
#     print(item)


# list2 = [1,2,3,4]

# for item in filter(lambda n: n<2, list2): 
#     print(item)




# words = str.split('The longest word in this sentence')
# w = sorted(words, key=len)
# # w = sorted(words, key=str.lower)
# print(w)





# Recursive functions

# iteration
# def iterTest(low,high):
#     while low <= high:
#         print(low)
#         low=low+1

# # recursion
# def recurTest(low, high):
#     if low <= high:
#         print(low)
#         recurTest(low+1, high)


#compares the running time of a list compared to a generator
# import time
# #generator function creates an iterator of odd numbers between n and m
# def oddGen(n,m):
#     while n<m:
#         yield n
#         n+=2

#builds a list of odd numbers between n and m
# def oddList(n,m):
#     lst = []
#     while n<m:
#         lst.append(n)
#         n+=2
#     return lst


# #the time it takes to perform sum on an iterator
# t1=time.time()
# sum(oddGen(1,1000000))
# print('Time to sum an iteration: %f' % (time.time()-t1))

# #the time it takes to build and sum a list
# t1=time.time()
# sum(oddList(1,1000000))
# print("Time to build and sum a list: %f" % (time.time() - t1))





# Classes and object programming


# class Employee(object):
#     numEmp = 0

#     def __init__(self, name, rate):
#         self.owed = 0
#         self.name = name
#         self.rate = rate
#         Employee.numEmp += 1
    
#     def __del__(self):
#         Employee.numEmp -= 1
    
#     def hours(self, numHours):
#         self.owed += numHours*self.rate
#         return ('%.2f hours worked' % numHours)
    
#     def pay(self):
#         self.owed = 0
#         return('payed %s ' % self.name)

# emp1 = Employee('Jill', 18.50)
# emp2 = Employee('Fer', 48.50)

# print(Employee.numEmp)
# print(emp1.hours(20))
# print(emp1.owed)
# print(emp1.pay())



