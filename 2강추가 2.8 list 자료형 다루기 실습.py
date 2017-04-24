Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> sample_list1 = ['eggs', 'butter', 'flour', 'bread', 'cheese']
>>> sample_list1
['eggs', 'butter', 'flour', 'bread', 'cheese']
>>> sample_list2 = list([1, 'drink', 10, 'sandwiches', 0.45e-2])
>>> sample_list2
[1, 'drink', 10, 'sandwiches', 0.0045]
>>> sample_list1, sample_list2
(['eggs', 'butter', 'flour', 'bread', 'cheese'], [1, 'drink', 10, 'sandwiches', 0.0045])
>>> sample_list1[0]
'eggs'
>>> sample_list1[1]
'butter'
>>> sample_list1[0] + ' ' + sample_list1[1]
'eggs butter'
>>> sample_list1[1:3]
['butter', 'flour']
>>> sample_list2[1:3]
['drink', 10]
>>> numbers = list(range(10))
>>> numbers
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> numbers[2:5]
[2, 3, 4]
>>> numbers[:]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> numbers[::2]
[0, 2, 4, 6, 8]
>>> numbers * 2
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> numbers + sample_list2
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 'drink', 10, 'sandwiches', 0.0045]
>>> sample_list3 = [1, 2, 3, ['a', 'b', 'c'], ['Hello', 'Python']]
>>> sample_list3
[1, 2, 3, ['a', 'b', 'c'], ['Hello', 'Python']]
>>> sample_list3[3]
['a', 'b', 'c']
>>> sample_list3[3][1]
'b'
>>> sample_list3[4]
['Hello', 'Python']
>>> sample_list3.append(' '.join(sample_list3[4]))
>>> sample_list3
[1, 2, 3, ['a', 'b', 'c'], ['Hello', 'Python'], 'Hello Python']
>>> sample_list3.pop(3)
['a', 'b', 'c']
>>> sample_list3.pop(2)
3
>>> sample_list3
[1, 2, ['Hello', 'Python'], 'Hello Python']
>>> sample_list3.pop(2)
['Hello', 'Python']
>>> sample_list3
[1, 2, 'Hello Python']
>>> sample_list3.insert(2, 3)
>>> sample_list3
[1, 2, 3, 'Hello Python']
>>> sample_list3.insert(3, ['a', 'b', 'c'])
>>> sample_list3
[1, 2, 3, ['a', 'b', 'c'], 'Hello Python']
>>> sample_list3.pop(4)
'Hello Python'
>>> sample_list3.insert(4,['Hello', 'Python'])
>>> sample_list3
[1, 2, 3, ['a', 'b', 'c'], ['Hello', 'Python']]
>>> 
