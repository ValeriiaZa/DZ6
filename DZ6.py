
lst1 = [1, 2, 3, 4]
if len(lst1) == 0:
    print(lst1)
else:
    a = lst1.pop(-1)
    lst1.insert(0, a)
    print(lst1)
