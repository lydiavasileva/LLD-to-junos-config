import csv
def main():
	output = open('setCommands','w')
	with open('simpleLLD.csv', 'r') as csvfile:
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
	try:
		if row['IP Address'] == 'dhcp':
			output.write('set interface ' + row['Interface'] + ' unit ' + row['Unit'] + ' family ' + row['Family'] + ' ' + row['IP Address'] +'\n')
		elif (row['Interface'] != '' and row['IP Address'] != '') and (row['Peer Interface'] == '' or row['Peer Interface'] == 'N/A'):
			output.write('set interface ' + row['Interface'] + ' unit ' + row['Unit'] + ' family ' + row['Family'] + ' address ' + row['IP Address']+'/'+row['Mask'] +'\n')
		elif row['Interface'] != '' and row['IP Address'] != '' and row['Peer Interface'] != '' and row['Peer Interface'] != 'N/A':
			output.write('set interface ' + row['Interface'] + ' unit ' + row['Unit'] + ' encapsulation ' + row['Encapsulation'] + ' peer-unit ' + row['Peer Unit'] + ' family ' + row['Family'] + ' address ' + row['IP Address']+'/'+row['Mask'] +'\n')
		else:
			pass
	except KeyError:
		pass
def setRoutingInstances(row,output):
	try:
		if row['Instance Type'] != '' and row['Virtual Router'] != '':
			output.write('set routing-instances ' + row['Virtual Router'] + ' instance-type ' + row['Instance Type'] +'\n')
			if row['Instance Type'] == 'virtual-router':
				output.write('set routing-instances ' + row['Virtual Router'] + ' interface ' + row['Interface'] + '.' + row['Unit'] +'\n')
		else:
			pass

	except KeyError:
		pass

def setProtocols(row,output):
	try:
		if row['Routing Dynamic Protocol'] != '' and  row['Routing Dynamic Protocol'] != 'N/A' and row['Status'] == 'Passive':
			output.write('set routing-instances ' + row['Virtual Router'] + ' protocols ' + row['Routing Dynamic Protocol'] + ' area ' + row['Area/AS/Level'] + ' interface ' + row['Interface'] + '.' + row['Unit'] + ' passive' +'\n')
		elif row['Routing Dynamic Protocol'] != '' and  row['Routing Dynamic Protocol'] != 'N/A' and row['Status'] != 'Passive':
			output.write('set routing-instances ' + row['Virtual Router'] + ' protocols ' + row['Routing Dynamic Protocol'] + ' area ' + row['Area/AS/Level'] + ' interface ' + row['Interface'] + '.' + row['Unit'] +'\n')
		else:
			pass

	except KeyError:
		pass

def setStaticRoute(row,output):
	try:
		if row['Routing Static Network'] != '' and row['Routing Static Network'] != 'N/A':
			output.write('set routing-instances '+ row['Virtual Router'] +' routing-options static route ' + row['Routing Static Network'] + ' next-hop ' + row['Routing Static Next-Hop'] +'\n')
		else:
			pass

	except KeyError:
		pass
def setRoutingPolicies(row,output):
	try:
		if (row['Routing Policy Name'] != '' and  ['Routing Policy Name'] != 'N/A') and (row['Policy Match Value'] != '' and row['Policy Match Value'] != 'N/A'):
			output.write('set policy-options policy-statement ' + row['Routing Policy Name'] + ' term ' + row['Policy Term'] + ' from ' + row['Policy Match Condition'] + ' ' + row['Policy Match Value'] + '\n')
			output.write('set policy-options policy-statement ' + row['Routing Policy Name'] + ' term ' + row['Policy Term'] + ' then ' + row['Policy Action'] +'\n')
			output.write('set routing-instances ' + row['Virtual Router'] + ' protocols ' + row['Policy Export'] + ' export ' + row['Routing Policy Name'] +'\n')
		elif (row['Routing Policy Name'] != '' and ['Routing Policy Name'] != 'N/A') and (row['Policy Match Address'] != '' and row['Policy Match Address'] != 'N/A'):
			output.write('set policy-options policy-statement ' + row['Routing Policy Name'] + ' term ' + row['Policy Term'] + ' from ' + row['Policy Match Condition'] + ' ' + row['Policy Match Address'] + ' ' + row['Policy Match Type'] + '\n')
			output.write('set policy-options policy-statement ' + row['Routing Policy Name'] + ' term ' + row['Policy Term'] + ' then ' + row['Policy Action'] +'\n')
			output.write('set routing-instances ' + row['Virtual Router'] + ' protocols ' + row['Policy Export'] + ' export ' + row['Routing Policy Name'] +'\n')
		else:
			pass

	except KeyError:
		pass
main()