courses= ['History', 'Math', 'Physics', 'Computer']

print(courses)
print(len(courses))
print(courses[0])
print(courses[3])
print(courses[-1])

print(courses[0:2])  
print(courses[2: ])

courses.append('art')
print(courses)

courses.insert(0,'Commerce')
print(courses)

courses_2=['Education', 'Science']
courses.insert(0, courses_2)

print(courses)

courses.extend(courses_2)
print(courses)

courses.remove('Math')
print(courses)

courses.pop() #Removes the last value of the list
print(courses)

courses.reverse()
print(courses)

numlist= [1,2,5,3,4]
numlist.sort()
print(numlist)
print('Maximum value of list: ',max(numlist))
print('Minimum value of list: ',min(numlist))
print('Sum: ',sum(numlist))





numlist.sort(reverse=True)
print(numlist)


courses.remove(courses_2)
print(courses)

sorted_course= sorted(courses)
print(sorted_course)


print(courses.index('History'))

print('Kikki' in courses)
print('Commerce' in courses)

for item in courses:
	print(item)


for index, item in enumerate(courses):
	print(item, index)


course_str= ','.join(courses)
print(course_str)

new_list= course_str.split(',')
print(new_list)


list1= ['Kiki', 'Niki', 'Litu', 'Kutu']
list2=list1

print(list1)
print(list2)

list1[0]= 'Art'
print(list1)
print(list2)


tuple1=('Satwik', 'Mohanty')
tuple2=tuple1

print(tuple1)
print(tuple2)

#tuple1[0]='Art'
#We cannot modify tuple because they are immutable.


#Sets 

cs_courses={'DSA', 'DBMS', 'OS', 'ML','OS'}
print(cs_courses)

print('OS' in cs_courses)


cs_courses={'DSA', 'DBMS', 'OS', 'ML','OS'}
art_courses={'History', 'Civics', 'Geography', 'Economics', 'DSA', 'ML'}

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))

print(cs_courses.union(art_courses))

