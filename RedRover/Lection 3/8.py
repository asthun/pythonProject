# Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'},
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга

set1 = {'z', 1, 5, 9, 21, 100, 'l'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
set1_diff = list(set1.difference(set2))
set2_diff = list(set2.difference(set1))

i = 0
while i < len(set1_diff):
    set1.remove(set1_diff[i])
    i += 1
print("Same: ")
print(set1)
print("Different: ")
print(set1_diff + set2_diff)


if len(set1_diff) == 0 or len(set2_diff) == 0:
    print("подмножества!!")
else:
    print("НЕ подмножества!!")