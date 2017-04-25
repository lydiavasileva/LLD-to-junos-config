import csv
with open('IJOS-Alternative-Virtual-SRX-A1.csv', 'r') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['Interface'] != '' and row['ip address'] != '':
			print('set interface ' + row['Interface'] + ' unit ' + row['Unit'] + ' family ' + row['Family'] + ' address ' + row['ip address']+row['Mask'])
		if row['Routing-Instance'] != '' and row['Main Router Virtual Router'] != '':
			print('set routing-instances ' + row['Main Router Virtual Router'] + ' instance-type ' + row['Routing-Instance'])
		if row['Routing-Instance'] == ' virtual-router':
			if row['Main Router Virtual Router'] != '':
				deviceName = row['Main Router Virtual Router']
				print('set routing-instances ' + deviceName + ' interface ' + row['Interface'] + '.' + row['Unit'])
			else:
				print('set routing-instances ' + deviceName + ' interface ' + row['Interface'] + '.' + row['Unit'])
		
		#print(row['Main Router Virtual Router'],row['Instance-Type'], row['Interface'], row['Unit'], row['ip address'])

