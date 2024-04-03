my_dict = {'tuple', 'list', 'dict', 'set'}

tuple = (1, 10, 'text', 3.14, True)
print(tuple[-1])

list = [2, 111, 'Hello!', 'number', False]
list.append(3333)
list.pop(1)
print(list)

dict = {1:1, 'one':"biger_zero", 'two':'2', 2-2: 0, False:True}
dict['i am a tuple'] = 'six value'
removed_value = dict.pop(1)
print(dict)

set = {1, 'one', 'two', 2.2, False}
set.add(111)
set.remove(1)
print(set)

print(my_dict)
