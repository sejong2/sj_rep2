Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list1 = [1, 1, 2, 3, 5, 5, 7, 9, 1]
>>> list1
[1, 1, 2, 3, 5, 5, 7, 9, 1]
>>> set1 = set(list1)
>>> set1
set([1, 2, 3, 5, 7, 9])
>>> 1 in set1
True
>>> 100 in set1
False
>>> set1 = {1, 2, 3, 5, 7}
>>> set2 = {5, 7, 11}
>>> set1 | set2
set([1, 2, 3, 5, 7, 11])
>>> set1 & set2
set([5, 7])
>>> set1 - set2
set([1, 2, 3])
>>> set1 ^ set2
set([1, 2, 3, 11])
>>> dic1 = {1:'egg', 2:'ham', 3: 'milk'}
>>> dic1
{1: 'egg', 2: 'ham', 3: 'milk'}
>>> dic1.get(2)
'ham'
>>> dic1[3]
'milk'
>>> dic1 = {1:'egg', 2:'ham', 3: 'milk', 4:'egg'}
>>> dic1
{1: 'egg', 2: 'ham', 3: 'milk', 4: 'egg'}
>>> dic1 = {1:'egg', 2:'ham', 3: 'milk', 4:'egg', 3:'cheese'}
>>> dic1
{1: 'egg', 2: 'ham', 3: 'cheese', 4: 'egg'}
>>> dic1.get(5)
>>> dic1.get(5)
>>> dic1[5]

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    dic1[5]
KeyError: 5
>>> dic1.get(5)
>>> dic1[5]

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    dic1[5]
KeyError: 5
>>> dic1.get(4)
'egg'
>>> dic1[4]
'egg'
>>> dic2 = {'egg':2, 'milk':4, 'spam':10, 'ham':15}
>>> dic2
{'ham': 15, 'egg': 2, 'milk': 4, 'spam': 10}
>>> dic2 = {'egg':2, 'milk':4, 'spam':10, 'ham':15, 'milk':9}
>>> dic2
{'ham': 15, 'egg': 2, 'milk': 9, 'spam': 10}
>>> dic2.get('egg')
2
>>> dic2['egg']
2
>>> dic1 = {1:'egg', 2:'ham', 3: 'milk'}
>>> dic1
{1: 'egg', 2: 'ham', 3: 'milk'}
>>> dic1[4] = 'cheese'
>>> dic1
{1: 'egg', 2: 'ham', 3: 'milk', 4: 'cheese'}
>>> dic1.keys()
[1, 2, 3, 4]
>>> dic1.values()
['egg', 'ham', 'milk', 'cheese']
>>> dic3 = {'orange':5, 'melon':17, 'banana':10}
>>> dic3
{'orange': 5, 'melon': 17, 'banana': 10}
>>> dic3.items()
[('orange', 5), ('melon', 17), ('banana', 10)]
>>> sorted(dic3.items())
[('banana', 10), ('melon', 17), ('orange', 5)]
>>> dic4 = {1:'egg', 2:'ham', 3: 'milk'}
>>> dic5 = {5:'orange', 17:'melon', 10:'banana'}
>>> dic4.update(dic5)
>>> dic4
{1: 'egg', 2: 'ham', 3: 'milk', 5: 'orange', 17: 'melon', 10: 'banana'}
>>> dic6 = {'k1':5, 'k2':[1,2,3,4,5], 'k3':{'a':1, 'b':2, 'c':[1,2,3]}}
>>> dic6
{'k3': {'a': 1, 'c': [1, 2, 3], 'b': 2}, 'k2': [1, 2, 3, 4, 5], 'k1': 5}
>>> dic6.get('k3')
{'a': 1, 'c': [1, 2, 3], 'b': 2}
>>> dic6.get('k3').get('c')
[1, 2, 3]
>>> dic6.get('k3').get('c')[1]
2
>>> single_tuple = (1,)
>>> single_tuple
(1,)
>>> single_tuple = single_tuple + (2,3,4,5)
>>> single_tuple
(1, 2, 3, 4, 5)
>>> single_tuple[3]
4
>>> single_tuple[3] = 100

Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    single_tuple[3] = 100
TypeError: 'tuple' object does not support item assignment
>>> tup = (['this', 'is', 'list','1'], ['this', 'is', 'list', '2'])
>>> tup[0]
['this', 'is', 'list', '1']
>>> tup[1]
['this', 'is', 'list', '2']
>>> list1, list2 = tup
>>> list1
['this', 'is', 'list', '1']
>>> list2
['this', 'is', 'list', '2']
>>> list1[3]
'1'
>>> tup[0][3]
'1'
>>> 
