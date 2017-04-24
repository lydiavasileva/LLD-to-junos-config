import csv
with open('lld.csv', 'r') as csvfile:
	reader = csv.DictReader(csvfile)
	deviceList=[]	
	for row in reader:
		if row['Main Router Virtual Router'] != '':
			typeList =[]
			Devices = {row['Main Router Virtual Router']:typeList}
			if row['Instance-Type'] != '':
				interfaceList =[]
				DeviceType = {row['Instance-Type']:interfaceList}
				typeList.append(DeviceType)
			else:
				interfaceList =[]
				DeviceType = {'Null':interfaceList}
				typeList.append(DeviceType)
			deviceList.append(Devices)

		#print(row['Main Router Virtual Router'],row['Instance-Type'], row['Interface'], row['Unit'], row['ip address'])

	print (deviceList)
