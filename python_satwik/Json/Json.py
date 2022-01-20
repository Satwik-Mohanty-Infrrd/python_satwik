import json

people_string = '''
{
	"people":[
	{
		"name":"Satwik Mohanty",
		"phone":"9079605204",
		"emails":["satwik0810@gmail.com", "satwik.mohanty2021@gmail.com"],
		"has_license": true
	},
	{
		"name":"Jane Doe",
		"phone":"560-555-5153",
		"emails":null,
		"has_license":true
	}

	]
}
'''

data=json.loads(people_string)
print(data)

print(type(data))
print(type(data['people']))

for person in data['people']:
	print(person)

for person in data['people']:
	print(person['name'])

for person in data['people']:
	del person['phone']

new_string= json.dumps(data)
print(new_string)

new_string= json.dumps(data, indent=2, sort_keys=True)
print(new_string)