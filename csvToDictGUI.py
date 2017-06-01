import csv
import tkinter

class MainGui():
	def __init__(self):
		#Main window
		self.main_window = tkinter.Tk()

		#Set Window Title
		self.main_window.wm_title("CSV Creator")

		#Creating the three frames
		self.main_frame = tkinter.Frame(self.main_window)

		self.insert_button = tkinter.Button\
		(self.main_frame, text="Setup",\
			command=self.setupIntput)\
		.grid(row=0,column=0, pady=50)

		self.quit_button = tkinter.Button\
		(self.main_frame, text="Quit", \
			command=self.main_window.destroy)\
		.grid(row=0,column=5, pady=50)

		#Packing the frames
		self.main_frame.pack()

		#Enter the tkinter main loop.
		tkinter.mainloop()

	def setupIntput(self):
		self.deviceList=[]
		self.physRouterList=[]
		self.routerNameList=[]
		#Main window
		self.setup_window = tkinter.Tk()

		#Creating the three frames
		self.top_frame = tkinter.Frame(self.setup_window)

		self.bottom_frame = tkinter.Frame(self.setup_window)

		self.physRouter_label = tkinter.Label\
		(self.top_frame, text="Physical Router:")\
			.grid(row=0,column=0)

		self.physRouter_entry = tkinter.Entry\
		(self.top_frame, bd =5)
		self.physRouter_entry.grid(row=0,column=1)

		self.routerName_label = tkinter.Label\
		(self.top_frame, text="Router Name:")\
			.grid(row=1,column=0)

		self.routerName_entry = tkinter.Entry\
		(self.top_frame, bd =5)
		self.routerName_entry.grid(row=1,column=1)

		self.insert_button = tkinter.Button\
		(self.bottom_frame, text="Add",\
			command=self.add)\
		.grid(row=0,column=0, pady=50)

		self.insert_button = tkinter.Button\
		(self.bottom_frame, text="Done",\
			command=self.done)\
		.grid(row=0,column=1, pady=50)

		#Packing the frames
		self.top_frame.pack()
		self.bottom_frame.pack()

		#Enter the tkinter main loop.
		tkinter.mainloop()

	def add(self):
		self.physRouter = self.physRouter_entry.get()
		self.routerName = self.routerName_entry.get()

		if self.physRouter not in self.physRouterList and self.routerName not in self.routerNameList:

			self.physRouterList.append(self.physRouter)
			self.routerNameList.append(self.routerName)

		print(self.physRouterList)

		print(self.routerNameList)

	def done(self):
		self.deviceList.append(self.physRouterList)
		self.deviceList.append(self.routerNameList)

		self.setup_window.destroy()

		print(self.deviceList)

	def createHeader(self):
		with open('test.csv', 'w') as csvfile:
			fieldnames = ['Physical Router', 'Router Name', 'Routing-Instance', 'Routing-Instance', 'Interface', 'Unit', 'IP Address', 'Mask', 'Family', 'Encapsulation', 'Peer Interface', 'Peer Unit', 'To VR', 'Routing Dynamic Protocol', 'Routing Dynamic Area/AS', 'Routing Dynamic Status', 'Routing Static Network', 'Routing Static Next-Hop', 'Routing Static Qualified-Next-Hop','Policy Name', 'Policy Term', 'Policy Match Condition', 'Policy Match Value', 'Policy Match Address', 'Policy Match Mask', 'Policy Match Type', 'Policy Action']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

			writer.writeheader()



gui = MainGui()