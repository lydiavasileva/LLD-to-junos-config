import csv
def main():
	output = open('setCommands','w')
	with open('IJOS-Alternative-Virtual-SRX-A1.csv', 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			setInterface(row,output)
			setRoutingInstances(row,output)
			setProtocols(row,output)
			setStaticRout(row,output)

def setInterface(row,output):
	if (row['Interface'] != '' and row['ip address'] != '') and (row['Peer Interface'] == '' or row['Peer Interface'] == 'N/A'):
				output.write('set interface ' + row['Interface'] + ' unit ' + row['Unit'] + ' family ' + row['Family'] + ' address ' + row['ip address']+row['Mask'] +'\n')
	elif row['Interface'] != '' and row['ip address'] != '' and row['Peer Interface'] != '' and row['Peer Interface'] != 'N/A':
				output.write('set interface ' + row['Interface'] + ' unit ' + row['Unit'] + ' encapsulation ' + row['Encapsulation'] + ' peer-unit ' + row['Peer Unit'] + ' family ' + row['Family'] + ' address ' + row['ip address']+row['Mask'] +'\n')
	else:
		pass

def setRoutingInstances(row,output):
	if row['Routing-Instance'] != '' and row['Main Router Virtual Router'] != '':
		output.write('set routing-instances ' + row['Main Router Virtual Router'] + ' instance-type ' + row['Routing-Instance'] +'\n')
		if row['Routing-Instance'] == 'virtual-router':
			output.write('set routing-instances ' + row['Main Router Virtual Router'] + ' interface ' + row['Interface'] + '.' + row['Unit'] +'\n')
	else:
		pass

def setProtocols(row,output):
	if row['Routing Protocol'] != '' and  row['Routing Protocol'] != 'N/A' and row['Status'] == 'Passive':
		output.write('set routing-instances ' + row['Main Router Virtual Router'] + ' protocols ' + row['Routing Protocol'] + ' area ' + row['Area/AS/Level'] + ' interface ' + row['Interface'] + '.' + row['Unit'] + ' passive' +'\n')
	elif row['Routing Protocol'] != '' and  row['Routing Protocol'] != 'N/A' and row['Status'] != 'Passive':
		output.write('set routing-instances ' + row['Main Router Virtual Router'] + ' protocols ' + row['Routing Protocol'] + ' area ' + row['Area/AS/Level'] + ' interface ' + row['Interface'] + '.' + row['Unit'] +'\n')
	else:
		pass

def setStaticRout(row,output):
	if row['Static Network'] != '' and row['Static Network'] != 'N/A':
		output.write('set routing-options static route ' + row['Static Network'] + ' next-hop ' + row['Static Next-Hop'] +'\n')
	else:
		pass
main()