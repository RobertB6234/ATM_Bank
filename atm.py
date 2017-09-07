'''
File atm.py
Case Study: 9.3 page 367
Author:RB
Date: 8/5/2017

This moduel defines the ATM class and its application
To test, launch from IDLE and run

>>>>createBank 95)
>>>>main()

Can be modified to run as a script fater a bank has been saved
'''
from bank import Bank, SavingsAccount
from tkinter import *

class ATM(Frame):
	'''This class handles terminal based ATM  transactions'''

	def __init__(self, bank):
		"""Intialize the fram, widgets, and the data model"""
		Frame.__init__(self)
		self.master.title("ATM")
		self.grid()
		self._bank = bank
		self._account = None
		
		# Create and add the widgest to the frame.
		# Data containers for the entry fields
		self._nameVar = StringVar()
		self._pinVar = StringVar()
		self._amountVar = DoubleVar()
		self._statusVar = StringVar()
		
		# Labels for entry fields
		self._nameLabel = Label(self, text = "Name")
		self._nameLabel.grid(row = 0, column = 0)
		self._pinlLabel = Label(self, text = "PIN")
		self._pinlLabel.grid(row = 1, column = 0)
		self._amountLabel = Label(self, text = "Amount")
		self._amountLabel.grid(row = 2, column = 0)
		self._statusLabel = Label(self, text = "Status")
		self._statusLabel.grid(row = 3, column = 0)
		
		# Entry fields
		self._nameEntry = Entry(self, textvariable = self._nameVar, justify = CENTER)
		self._nameEntry.grid(row = 0, column = 1)
		
		self._pinEntry = Entry(self, textvariable = self._pinVar, justify = CENTER)
		self._pinEntry.grid(row = 1, column = 1)
		
		self._amountEntry = Entry(self, textvariable = self._amountVar, justify = CENTER)
		self._amountEntry.grid(row = 2, column = 1)
		
		self._statusEntry = Entry(self, textvariable = self._statusVar, justify = CENTER)
		self._statusEntry.grid(row = 3, column = 1)
		
		#Command buttons
		self._balanceButton = Button(self, text = "Balance", command = self._getBalance)
		self._balanceButton["state"] = DISABLED
		self._balanceButton.grid(row = 0, column = 2)
		
		self._depositButton = Button(self, text = "Deposit", command = self._deposit)
		self._depositButton.grid(row = 1, column = 2)
		
		self._withdrawButton = Button(self, text = "Withdraw", command = self._withdraw)
		self._withdrawButton["state"] = DISABLED 
		self._withdrawButton.grid(row = 2, column = 2)
		
		self._loginButton = Button(self, text = "Login", command = self._login)
		self._loginButton.grid(row = 3, column = 2)
		
	def _getBalance(self):
		self._statusVar.set("You balance is $%0.2f" % (self._account.getBalance()))
		
	def _deposit(self):
		amount = self._amountVar.get()
		self._account.deposit(amount)
		self._statusVar.set("Deposit made")
		
	def _withdraw(self):
		amount = self._amountVar.get()
		message = self._account.withdraw(amount)
		if message:
			self._statusVar.set(message)
		else: 
			self._statusVar.set("Withdrawal made")
			
	def _login(self):
		pin = self._pinVar.get()
		name = self._nameVar.get()
		self._account = self._bank.get(pin)
		if self._account:
			if name == self._account.getName():
				self._statusVar.set("Welcome to the bank!")
				self._loginButton["text"] = "Logout"
				self._loginButton["command"] = self._logout
				self._balanceButton["state"] = NORMAL
				self._depositButton["state"] = NORMAL
				self._withdrawButton["state"] = NORMAL
			else:
				self._statusVar.set("Unrecognized name")
				self._account = None
		else:
			self._statusVar.set("Unrecognized pin")
			
	def _logout(self):
		self._account = None
		self._nameVar.set(" ")
		self._pinVar.set(" ")
		self._amountVar.set(0.0)
		self._loginButton["text"] = "Login"
		self._loginButton["command"] = self._login
		self._balanceButton["state"] = DISABLED
		self._depositButton["state"] =  DISABLED
		self._withdrawButton["state"] = DISABLED
		self._statusVar.set("Have a nice day!")
		
	# Top-level funtions
def main():
	"""Instantiate a bank and use it in an ATM. """
	bank = Bank("bank.dat")
	print ("The bank has been loaded")
		
	atm = ATM(bank)
	print("Running the GUI")
	atm.mainloop()
		
	bank.save()
	print("The bank has been updated")
		
def createBank(number = 0):
	"""Saves a bank with the specified number of accounts. Used during testing."""
	bank = Bank()
	for i in range(number):
		bank.add(SavingsAccount('Name' + str(i), str(1000 + i), 100.00))
			
	bank.save("bak.dat")

main()
			
			
			
		
		
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
		
		
		
		
		
		

# Top - level functions
def main():
	'''Instantiate a Bank and an ATM and run it.'''
	bank = Bank("bank.dat")
	atm = ATM(bank)
	atm.run()
	
def createBank(number = 0):
	'''Saves a bank with specified number of accounts.
	Used during testing'''
	bank = Bank()
	for i in range(number):
		bank.add(SavingsAccount('Name' + str(i + 1), str(1000 +1), 100.00))
		
	bank.save("bank.dat ")
			
main()
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
