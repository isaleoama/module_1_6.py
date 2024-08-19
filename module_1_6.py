my_dict = {'Alex': 2011, 'Steve': 1999, 'Robin': 1512, 'Olga': 1911}
print(my_dict)
print(my_dict['Alex'])
print(my_dict.get('Denis'))
my_dict['Karina'] = 2013
my_dict.update( {'Maria' : 1913 ,
                 'Mark' : 2122})
print(my_dict)
del_value = my_dict.pop('Mark')
print(del_value)

my_set = {1, 2, 4, 7, 8, 'Mayki', 'String', 1, 4, 3}
print(my_set)
print(my_set.add(5), my_set.add(11.53))
print(my_set.discard(1))
print(my_set)
