import csv


with open('names.csv', 'r') as csv_file:
	csv_reader= csv.reader(csv_file)

	for line in csv_reader:
		print(line)
		print(line[2])
		

with open('names.csv', 'r') as csv_file:
	csv_reader= csv.reader(csv_file)

	next(csv_file) #It is used to remove the heading attributes like first_name, last_name, email.
	for line in csv_reader:
		print(line[2])


with open('names.csv', 'r') as csv_file:
	csv_reader= csv.reader(csv_file)

	with open('new_names.csv', 'w') as new_file:
		csv_writer= csv.writer(new_file, delimiter='-')

		for line in csv_reader:
			csv_writer.writerow(line)

