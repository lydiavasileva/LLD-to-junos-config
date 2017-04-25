import csv
output = open('setCommands','w')
with open('IJOS-Alternative-Virtual-SRX-A1.csv', 'r') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['Interface'] != '' and row['ip address'] != '':
			output.write('set interface ' + row['Interface'] + ' unit ' + row['Unit'] + ' family ' + row['Family'] + ' address ' + row['ip address']+row['Mask'] +'\n')
		if row['Routing-Instance'] != '' and row['Main Router Virtual Router'] != '':
			output.write('set routing-instances ' + row['Main Router Virtual Router'] + ' instance-type ' + row['Routing-Instance'] +'\n')
		if row['Routing-Instance'] == ' virtual-router':
			if row['Main Router Virtual Router'] != '':
				deviceName = row['Main Router Virtual Router']
				output.write('set routing-instances ' + deviceName + ' interface ' + row['Interface'] + '.' + row['Unit'] +'\n')
			else:
				output.write('set routing-instances ' + deviceName + ' interface ' + row['Interface'] + '.' + row['Unit'] +'\n')
		if row['Routing Protocol'] != '' and  row['Routing Protocol'] != 'N/A' and row['Status'] == 'Passive':
			output.write('set routing-instances' + deviceName + ' protocols ' + row['Routing Protocol'] + ' area ' + row['Area/AS/Level'] + ' interface ' + row['Interface'] + '.' + row['Unit'] + ' passive' +'\n')
		elif row['Routing Protocol'] != '' and  row['Routing Protocol'] != 'N/A' and row['Status'] != 'Passive':
			output.write('set routing-instances' + deviceName + ' protocols ' + row['Routing Protocol'] + ' area ' + row['Area/AS/Level'] + ' interface ' + row['Interface'] + '.' + row['Unit'] +'\n')
		if row['Static Network'] != '' and row['Static Network'] != 'N/A':
			output.write('set routing-options static route ' + row['Static Network'] + ' next-hop ' + row['Static Next-Hop'] +'\n')
		#output.write(row['Main Router Virtual Router'],row['Instance-Type'], row['Interface'], row['Unit'], row['ip address'])

#
