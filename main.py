# 1
tuple_a = (1, 2, 3, 4, 5)
tuple_b = (4, 5, 6, 7, 8)
tuple_c = (4, 5, 6, 7, 8, 9, 10, 11)
tuple_d = tuple_a + tuple_b + tuple_c
print('№1 : \n', 'tuple_d = ',tuple_d)
# 2
res = ()
for i in tuple_d:
    count = tuple_d.count(i)
    if count > 1:
        a = (i, count)
        res = res + ((i, count),)
print('№2 : \n', 'res =', res)
# 3
res = []
for index, i in enumerate(tuple_d):
    count = tuple_d.count(i)
    if tuple_d.index(i) == index:
        if count > 1:
            result_index = []
            for index1, i1 in enumerate(tuple_d):
                if i1 == i:
                    result_index.append(index1)
                    result_index_tuple = tuple(result_index)
                    result = (i, result_index_tuple)
            res.append(result)
res_tuple = tuple(res)
print('№3 : \n' 'res =', res_tuple)

# 1
list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]
list_f = [9, 3, 4, 1, 8, 6, 5, 2, 0, 7]
list_c = list_a + list_b
print('#1 : \n','list_c = ', list_c)
# 2
list_c2 = []
for index, item in enumerate(list_a):
    list_c2.append(list_a[index])
    list_c2.append(list_b[index])
print('#2\n', 'list_c2 = ', list_c2)
# 3
list_c_a = []
list_c_b = []
for index, item in enumerate(list_a):
    if list_a[index] % 2 == 0:
        list_c_a.append(list_a[index])
    if list_b[index] % 2:
        list_c_b.append(list_b[index])
print('#3\n', 'list_c_a = ', list_c_a, ' \n list_c_b = ', list_c_b)
# 4
list_d = list_c[:]
list_d.reverse()
print('#4\n', 'list_d = ',list_d)
# 5
res = []
for index, item in enumerate(list_c):
    res.append(list_c[index] + list_d[index])
print('#5\n', 'res = ',res)
# 6
list_f = [9, 3, 4, 1, 8, 6, 5, 2, 0, 7]
res1 = list_f[:]
res2 = list_f[:]
res1.sort()
res2.sort(reverse=True)
print('#6\n', 'res1 = ', res1 ,'\n', 'res2 = ', res2)
# 7
res = []
for index, item in enumerate(list_c):
    result = (list_c[index], list_d[index])
    res.append(result)
print('#7\n', 'res = ', res)








