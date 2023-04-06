import csv
import re

with open('phonebook_raw.csv', encoding='utf-8', newline='') as f:
    rows = csv.reader(f, delimiter=',')
    contacts_list = list(rows)


def reg():
    dict_ = {}
    dict1_ = {}
    for i in contacts_list:
        j = ','.join(i)
        pattern = r'(8|\+7)\s*[\s|\(]*(\d{3})\)*[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})\s*\(*([доб.]*)\s*(\d*)\)*'
        subst = r'+7(\2)\3-\4-\5 \6\7'
        result = re.sub(pattern, subst, j)
        pattern1 = r'^(\w+)[\s|\,]*(\w+)\s?\,?(\w*)\,\,*(\,*)'
        subst1 = r'\1,\2,\3,'
        result1 = re.sub(pattern1, subst1, result)
        pattern2 = r'Иван(\,,)'
        subst2 = r'Иван,,,,,'
        result2 = re.sub(pattern2, subst2, result1)
        sp = result2.split(',')
        unific_ = ','.join(sp[0:2])
        unific1_ = ','.join(sp[2:])
        if unific_ not in dict_.keys():
            dict_[unific_] = unific1_.split(',')
        else:
            dict1_[unific_] = unific1_.split(',')
    return dict_, dict1_


def dict_add():
    dict3_ = {}
    for m, o in reg()[1].items():
        for i, j in reg()[0].items():
            if i == m:
                list3_ = []
                for p in range(len(j)):
                    if j[p] == '':
                        list3_.append(o[p])
                        # dict3_[i] = j
                    else:
                        list3_.append(j[p])
                        # dict3_[i] = o
                dict3_[m] = list3_
    return dict3_


def total_dict():
    dict4_ = {}
    for m, o in dict_add().items():
        # dict4_ = {}
        for i, j in reg()[0].items():
            if m != i:
                dict4_[i] = j
            else:
                dict4_[m] = o
    return dict4_


list5_ = []
for i, j in total_dict().items():
    m = (i + ',' + ','.join(j))
    list5_.append(m.split(','))


if __name__ == '__main__':
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=",")
        datawriter.writerows(list5_)

        datawriter.writerows(list5_)