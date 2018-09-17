from breezypythongui import EasyFrame
import random

class MainMenu(EasyFrame):

	def __init__(self):
		EasyFrame.__init__(self, title = "RPG Game", height = 320, width = 640)
		
		self.addLabel(text = "Main Menu", row = 0, column = 1)

		self.output = self.addLabel(text = "", row = 1, column = 0)


		self.buttonLeft = self.addButton(text = "QUIT", row = 3, column = 0, command = self.quit)

		self.buttonRight = self.addButton(text = "BEGIN", row = 3, column = 1, command = self.begin)
	
	def quit(self):
		self.output["text"] = "Goodbye!"
		#INSERT KILL COMMAND			
	
	def begin(self):
		self.output["text"] = "Greetings, tell me your name traveler..."
		self.InputField = self.addTextField(text = "", row = 2, column = 0)
		
		self.buttonLeft["text"] = "Go Back"
		self.buttonLeft["command"] = self.quit

		self.buttonRight["text"] = "Continue"
		self.buttonRight["command"] = self.name

	def name(self):
		name = self.InputField.getText()
		self.InputField.setText("")

		self.output["text"] = name + ", What is your class?"
		self.buttonRight["command"] = self.role

	def role(self):
		role = self.InputField.getText()
		self.InputField.setText("")

		self.output["text"] = role + ", Are you ready to get your stats?"
		self.buttonRight["command"] = self.stats

	def stats(self):
		Health = random.randint(1, 10)
		Armor = random.randint(1, 10)
		Magic = random.randint(1, 10)
		Attack = random.randint(1, 10)
		Speed = random.randint(1, 10)
		Exp = 0




def main():
	MainMenu().mainloop()

main()

