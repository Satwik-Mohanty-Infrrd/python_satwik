import memory_profiler as mem_profile
import random 
import psutil
import time 

names=['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors=['Math', 'Engineering', 'Computer', 'Arts', 'Business']

print('Memory (Before): {}Mb'.format(mem_profile.memory_usage_resource()))
def people_list(numpeople):
	res=[]
	for i in xrange(numpeople):
		person={
			'id':i,
			'name':random.choice(names),
			'major':raandom.choice(major)
		}
		res.append(person)
	return res

def people_generator(numpeople):
	for i in xrange(numpeople):
		person={
				'id':i,
				'name':random.choice(names),
				'major':random.choice(majors)
		}
		yield person

t1=time.clock()
people=people_list(1000000)
t2=time.clock()

print('Memory (After): {}Mb'.format(mem_profile.memory_usage()))
print('Took {} Seconds'.format(t2-t1))