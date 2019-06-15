import csv, json, sys

# sys.setdefaultencoding("UTF-8")

if sys.argv[1] is not None and sys.argv[2] is not None:

	file_json = sys.argv[1]

	file_csv = sys.argv[2]

	data_json = json.load(open(file_json))
	print(data_json)
	file_json.close()

	data_csv = open(file_csv, 'w')
	output = csv.writer(data_csv)
	output.writerow(data_json[0].keys())

	for row in data_json:
		output.writerow(row.values().encode('UTF-8'))


