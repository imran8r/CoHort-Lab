
a = 'bro'
b = 'bor'

if len(a) != len(b):
    print(False)
else:
    a_list1 = [char for char in a]
    a_list2 = [char for char in b]
    a_list1.sort()
    a_list2.sort()
    if a_list1 == a_list2:
        print(True)
    else:
        print(False)
