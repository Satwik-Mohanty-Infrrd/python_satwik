import csv

with open('new_names.csv', 'r') as csv_file:
	csv_reader= csv.reader(csv_file, delimiter='-')

	for line in csv_reader:
		print(line)

with open('names.csv', 'r') as csv_file:
	csv_reader= csv.DictReader(csv_file)

	for line in csv_reader:
		print(line)

with open('names.csv', 'r') as csv_file:
	csv_reader= csv.DictReader(csv_file)

	with open('new_names.csv', 'w') as new_file:
		fieldnames= ['\ufefffirst_name', 'last_name', 'email']

		csv_writer= csv.DictWriter(new_file,fieldnames=fieldnames, delimiter='-')

		for line in csv_reader:
			csv_writer.writerow(line)
