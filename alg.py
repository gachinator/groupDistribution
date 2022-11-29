print('Hello, world!')

#trying

import json

# JSON = {Id : {name : name, turn1 : subject, turn2 : subject, turn3 : subject}, Id : {name : name, turn1 : subject, turn2 : subject, turn3 : subject}, ...}

# Example

json = {1 : {"name" : "rak", "turn1" : "math", "turn2" : "bio", "turn3" : "CS"}, 2 : {"name" : "kar", "turn1" : "music", "turn2" : "bio", "turn3" : "art"}}

# subjects = (subject1, subject2, ...)
# groups = {subject1 : [name, name, ...], subject2 : [name, name, ...], ...}
# student_lessons = {name : count, name : count, ...}

groups_sizes = {
				 "math" : 20,
			     "bio" : 30,
			     "music" : 20
			    				}

def groups_init(subjects):
	groups = {}
	[groups.update({i : []}) for i in subjects]
	return(groups)

def subjects_list_init(jsonobj):
	subjects = set()
	for i in jsonobj:
		[subjects.add((jsonobj[i]["turn"+str(j)])) for j in range(1,4)]
	return(subjects)


def count_of_lessons_list_create(jsonobj):
	student_lessons = {}
	for i in jsonobj:
		if jsonobj[i]["name"] not in student_lessons:
			student_lessons[jsonobj[i]["name"]] = 0
	
	return(student_lessons)

def groups_filling(jsonobj, groups, subjects, student_lessons):
	for i in jsonobj:
		if jsonobj[i]["turn1"] in subjects:
			groups[jsonobj[i]["turn1"]].append(jsonobj[i]["name"])
			student_lessons[jsonobj[i]["name"]] += 1

		if jsonobj[i]["turn2"] in subjects:
			groups[jsonobj[i]["turn2"]].append(jsonobj[i]["name"])
			student_lessons[jsonobj[i]["name"]] += 1
	
	return(groups)

def group_size_check(groups):
	pass

student_lessons = count_of_lessons_list_create(json)
subjects = subjects_list_init(json)
groups = groups_init(subjects)

print(student_lessons,"\n",groups_filling(json, groups, subjects, student_lessons))
