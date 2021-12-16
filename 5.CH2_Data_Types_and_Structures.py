# Beginning with dictionaries

dict1 = {'a': 1, 'b':2, 'c':3}
print(dict1)

dict2 = ({'a':1, 'b':2, 'c':3})
print(dict2)

dict3 = dict(zip(['a', 'b', 'c'], [1,2,3]))
print(dict3)

dict4 = dict([('a',1), ('b',2), ('c',3)])
print(dict4)

dict1['d'] = 4
print(dict1)
dict1.update({'e':5, 'f':6})
print(dict1)
dict1.update({'g':7})
print(dict1)

# membership test (only in keys)
print('d' in dict1)

# membership do not check in values
print('dd' in dict1)

# page 48