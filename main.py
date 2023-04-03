import csv
import re

with open('phonebook_raw.csv', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=',')
    contacts_list = list(rows)

dict_ = {}

for i in contacts_list:
    j = ', '.join(i)
    pattern1 = r'(8|\+7)\s*[\s|\(]*(\d{3})\)*[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})\s*\(*([доб.]*)\s*(\d*)\)*'
    subst1 = r'+7(\2)\3-\4-\5 \6\7'
    result1 = re.sub(pattern1, subst1, j)
    pattern = r'^(\w+)[\s|\,]*(\w+)\,*\s*(\w*)'
    subst = r'\1, \2, \3'
    result = re.sub(pattern, subst, result1)
    sp = result.split()
    unific = ' '.join(sp[0:2])
    unific1 = ' '.join(sp[2:])

    if unific not in dict_.keys():
        dict_[unific] = [unific1]
    else:
        dict_[unific] += [unific1]

list1_ = []
counter = 0
for i in dict_.values():
    for j in i:
        counter += 1
        if counter >= 1:
            list1_.append(j)

p = dict_.keys()
res = list(zip(p, list1_))
list2_ = []
for x in res:
    m = x[0] + x[1]
    list2_.append(m)

res1 = []
for el in list2_:
    sub = el.split(',')
    res1.append(sub)
print(res1)

with open("phonebook.csv", "w") as f:

    datawriter = csv.writer(f, delimiter=",")
    datawriter.writerows(res1)