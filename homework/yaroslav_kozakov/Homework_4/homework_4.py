my_dict = {
    'tuple':(1, 10, 'text', 3.14, True),
    'list':[2, 111, 'Hello!', 'number', False],
    'dict':{1: 1, 'one': "biger_zero", 'two': '2', 'Love': 'love', False: True},
    'set':{1, 'one', 'two', 2.2, False}
}

print(my_dict['tuple'][-1])

my_dict['list'].append(3333)
my_dict['list'].pop(1)
print(my_dict['list'])

my_dict['dict'][('i am a tuple','six')] = 'six'
removed_value = my_dict['dict'].pop('two')
print(my_dict['dict'])

my_dict['set'].add(111)
my_dict['set'].remove(1)
print(my_dict['set'])

print(my_dict)
