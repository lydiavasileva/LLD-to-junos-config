import csv
def main():
	output = open('setCommands','w')
	with open('IJOS-Alternative-Virtual-SRX-A1.csv', 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		output.write('delete security policies' + '\n')
		output.write('set security forwarding-options family mpls mode packet-based' + '\n')
		for row in reader:
			setInterface(row,output)
			setRoutingInstances(row,output)
			setProtocols(row,output)
			setStaticRoute(row,output)
			setRoutingPolicies(row,output)
		output.write('\n')

def setInterface(row,output):
	if row['ip address'] == 'dhcp':
		output.write('set interface ' + row['Interface'] + ' unit ' + row['Unit'] + ' family ' + row['Family'] + ' ' + row['ip address'] +'\n')
	elif (row['Interface'] != '' and row['ip address'] != '') and (row['Peer Interface'] == '' or row['Peer Interface'] == 'N/A'):
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

def setStaticRoute(row,output):
	if row['Static Network'] != '' and row['Static Network'] != 'N/A':
		output.write('set routing-instances '+ row['Main Router Virtual Router'] +' routing-options static route ' + row['Static Network'] + ' next-hop ' + row['Static Next-Hop'] +'\n')
	else:
		pass
def setRoutingPolicies(row,output):
	if row['Policy'] != '' and row['Value'] != '':
		output.write('set policy-options policy-statement ' + row['Policy'] + ' term ' + row['Term'] + ' from ' + row['Condition'] + ' ' + row['Value'] + '\n')
		output.write('set policy-options policy-statement ' + row['Policy'] + ' term ' + row['Term'] + ' then ' + row['Action'] +'\n')
		output.write('set routing-instances ' + row['Main Router Virtual Router'] + ' protocols ' + row[' Policy-export'] + ' export ' + row['Policy'] +'\n')
	elif row['Policy'] != '' and row['Match-Address'] != '':

		pass
main()