print('Hello, world!')

# trying

import json

# JSON = {Id : {name : name, turn1 : subject, turn2 : subject, turn3 : subject}, Id : {name : name, turn1 : subject, turn2 : subject, turn3 : subject}, ...}

# Example

#json = {1: {"name": "rak", "turn1": "math", "turn2": "bio", "turn3": "CS"},
        #2: {"name": "kar", "turn1": "music", "turn2": "bio", "turn3": "art"}}

json = {1: {"name": "rak", "mail": "aaa@aaa.ru", "turn1": "math", "turn2": "bio", "turn3": "CS"},
        2: {"name": "kar", "mail": "aaa@aaa.ru", "turn1": "music", "turn2": "bio", "turn3": "art"}}

# subjects = (subject1, subject2, ...)
# groups = {subject1 : [name, name, ...], subject2 : [name, name, ...], ...}
# student_lessons = {name : count, name : count, ...}

groups_sizes = {
    "math": [20, 1],
    "bio": [1, 1],
    "music": [20, 3],
    "CS": [2, 3],
    "art": [3, 2]
}


# Создание групп
def groups_init(subjects):
    groups = {}
    [groups.update({i: []}) for i in subjects]
    return (groups)


# Создание списка предметов
def subjects_list_init(jsonobj):
    subjects = set()
    for i in jsonobj:
        [subjects.add((jsonobj[i]["turn" + str(j)])) for j in range(1, 4)]
    return (subjects)


# Создание счетчика предметов у каждого ученика
def count_of_lessons_list_create(jsonobj):
    student_lessons = {}
    for i in jsonobj:
        if jsonobj[i]["name"] not in student_lessons:
            student_lessons[jsonobj[i]["name"]] = 0

    return (student_lessons)


# Создание счетчика групп по предмету
def groups_number_init(jsonobj):
    groups_number = dict()
    for i in jsonobj:
        if jsonobj[i]["turn1"] not in groups_number:
            groups_number.update({jsonobj[i]["turn1"]: 1})
        if jsonobj[i]["turn2"] not in groups_number:
            groups_number.update({jsonobj[i]["turn2"]: 1})
        if jsonobj[i]["turn3"] not in groups_number:
            groups_number.update({jsonobj[i]["turn3"]: 1})

    return (groups_number)


# Заполнение групп учениками и счетчика предметов у каждого ученика
def groups_filling(jsonobj, groups, subjects, student_lessons):
    for i in jsonobj:
        if jsonobj[i]["turn1"] in subjects:
            groups[jsonobj[i]["turn1"]].append(jsonobj[i]["name"])
            student_lessons[jsonobj[i]["name"]] += 1

        if jsonobj[i]["turn2"] in subjects:
            groups[jsonobj[i]["turn2"]].append(jsonobj[i]["name"])
            student_lessons[jsonobj[i]["name"]] += 1

    return (groups)


# Проверка размерности групп - создание новых групп
def group_size_check(groups, groups_sizes, groups_number):
    for subject in list(groups):
        temp = []
        while len(groups[subject]) > groups_sizes[subject][0]:
            temp.append(groups[subject][-1])
            groups[subject].pop(-1)
        ex = {}
        if len(temp) % groups_sizes[subject][0] != 0:
            for i in range(len(temp) // groups_sizes[subject][0] + 1):
                ex.update({i: []})
                for student in range(groups_sizes[subject][0]):
                    ex[i].append(temp[-1])
                    temp.pop(-1)
        else:
            for i in range(len(temp) // groups_sizes[subject][0]):
                ex.update({i: []})
                for student in range(groups_sizes[subject][0]):
                    ex[i].append(temp[-1])
                    temp.pop(-1)
        for i in ex:
            groups_number[subject] += 1
            groups.update({"subj": ex[i]})
            groups[subject + str(i + 2)] = groups.pop("subj")
    return (groups)

def group_count_check(jsonobj, groups, groups_number):
    lishnie_groups=[]
    lishnie_stud=[]
    temp=''
    lishnie_stud_new=[]
    stud_id=[]
    names=[]
    new_subj=[]
    for i in list(groups_sizes):
        for j in list(groups_number):
            if i==j:
                if groups_sizes.get(i)[1] < groups_number.get(i):
                    lishnie_groups.append(i)

    for subj in lishnie_groups:
        for c in range (len(lishnie_groups)):
            lishnie_stud.append(groups.get(str(subj+str(c+2))))
            groups.pop(str(subj+str(c+2)))

    for d in range (len (lishnie_stud)):
        for e in range (len (lishnie_stud[d])):
            if lishnie_stud[d][e] != '[' and  lishnie_stud[d][e] != ']':
                temp+=lishnie_stud[d][e]
        lishnie_stud_new.append(temp)

    for d in range(1,len(list(jsonobj))+1):
        names.append(jsonobj[d]['name'])
    lishnie_stud_final=lishnie_stud_new.copy()
    for i in range (len(names)):
        for stud in lishnie_stud_new:
            if stud == names[i]:
                stud_id.append(i+1)
                lishnie_stud_new.remove(stud)
    for k in stud_id:
        stud=jsonobj.get(k)
    new_subj.append(stud.get('turn3'))

    for i in range (len(lishnie_stud_final)):
        if new_subj[i] in list(groups):
            groups[new_subj[i]].append(lishnie_stud_final[i])
        else:
            groups.update({i: []})
            groups[new_subj[i]].append(lishnie_stud_final[i])
        lishnie_stud_final.remove(lishnie_stud_final[i])
    return groups







student_lessons = count_of_lessons_list_create(json)
subjects = subjects_list_init(json)
groups = groups_init(subjects)
groups_number = groups_number_init(json)

groups_init(subjects)
groups_filling(json, groups, subjects, student_lessons)
group_size_check(groups, groups_sizes, groups_number)
print('1 - ', groups_sizes)
print('2 - ', groups)
print('3 - ', groups_number)

print('4 - ', group_count_check(json, groups,groups_number))

