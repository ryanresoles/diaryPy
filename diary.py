import os
import getpass
import time
from datetime import datetime


#functions
def ui():
	print("  ____   _   __   ___  _  _ ")
	print(" |  _ \ | | /  \ | _ || \/ |")
	print(" | (_) || || ^^ ||  _|\   / ")
	print(" |____/ |_||_/\_||_\_\ |_|  ")
	print("")


def login():
	current_user = {}
	print("Input credentials to continue: ")
	user = input("Enter your username: ")
	if user in user_accounts.keys():
		clear()
		ui()
		password = getpass.getpass("Enter password: ")
		if password == user_accounts[user][0]:
			current_user[user] = [user_accounts[user][0], user_accounts[user][1]]
			clear()
			user_ui(current_user, user)
			create_entries()
		else:
			print("Password incorrect. Please try again.")
			time.sleep(2)
			clear()
	else:
		print("User not found.")
		time.sleep(2)
		clear()


def user_ui(current_user, user):
	create_entries()
	load_entries()
	while True:
		ui()			
		print("Welcome, " + current_user[user][1] + "!")
		print()		
		print("M E N U")
		print("")
		print("[1] Create an entry")
		print("[2] View an entry")
		print("[3] Edit an entry")
		print("[4] Change password")
		print("[5] Logout")
		print("")
		choice = int(input("What do you want to do: "))
		clear()
		
		if choice == 1:
			while True:
				ui()
				print("CREATE AN ENTRY")
				entryTitle = input("Entry title: ")
				for e in entries.keys():
					if entryTitle == e[len(user):len(e)]:
						print("Invalid title. Title already taken.")
						time.sleep(2)
						clear()
						break
				else:
					entry = input("Write something: ")

					entries[user + entryTitle] = entry
					print("Entry saved.")
					time.sleep(2)
					clear()
					break


		elif choice == 2:
			while True:
				ui()
				print("Legend : (Username and Title)")
				for k in entries.keys():
					if user == k[:len(user)]:
						print(k)
					
				print()	
				print("REMINDER: Please print the exact title displayed on the screen.")
				choice = input("Which entry do you want to view: ")
				if choice in entries.keys():
					print(choice + " : " + entries[choice])
					choice2 = input("Enter 'B' to go back to the user menu: ")
					if choice2.upper() == "B":
						clear()
						break
					else:
						print("Invalid input.")
						time.sleep(2)
						clear()
				else:
					print("Entry not found.")
					time.sleep(2)
					clear()

				break

		elif choice == 3:
			while True:
				ui()
				print("Legend : (Username and Title)")
				for k in entries.keys():
					if user == k[:len(user)]:
						print(k)
					
				print()	
				choice = input("Which entry do you want to edit: ")
				if choice in entries.keys():
					entries[choice] = input("Enter modified entry: ")
					print()
					print("Entry successfully modified!")
					choice2 = input("Enter 'B' to go back to the user menu: ")
					if choice2.upper() == "B":
						clear()
						break
					else:
						print("Invalid input.")
						time.sleep(2)
						clear()
				else:
					print("Entry not found.")
					time.sleep(2)
					clear()

				break

		elif choice == 4:
			ui()
			print("CHANGE YOUR PASSWORD")
			pword = getpass.getpass("Enter current password: ")
			if pword == current_user[user][0]:
				user_accounts[user][0] = getpass.getpass("Enter new password: ")
				print("Password successfully changed!")
				user_update()
				time.sleep(2)
				clear()

		elif choice == 5:
			save_entries()
			break				
			

def save_entries():
	fileWriter = open("entries.txt", "w")
	if len(entries) > 0:
		for line in entries:
			fileWriter.write(encrypt(line) + "," + encrypt(entries[line]) + "\n")


	fileWriter.close()


def load_entries():
	loader = []
	fileReader = open("entries.txt", "r")
	for line in fileReader:
		ent = line[:-1]
		userEntry = ent.split(",")
		loader.append(userEntry)
	for u in loader:
		entries[decrypt(u[0])] = decrypt(u[1])

	fileReader.close()


def encrypt(string):
	output = ""
	for c in range(0, len(string)):
		output = output + chr(ord(string[c])-5)

	return output


def decrypt(string):
	output = ""
	for c in range(0, len(string)):
		output = output + chr(ord(string[c])+5)

	return output


def load_users():
	loader = []
	fileReader = open("user_accounts.txt", "r")
	for line in fileReader:
		unique_user = line[:-1]
		user_data = unique_user.split(",")
		loader.append(user_data)
	for u in loader:
		user_accounts[decrypt(u[0])] = [decrypt(u[1]), decrypt(u[2])]

	fileReader.close()


def signup(user):
	ui()
	passw = getpass.getpass("Enter your password : ")
	name = input("Enter your name [Firstname, Surname] : ")
	print("REMINDER : Please take note of your credentials to make sure you won't have trouble accessing your account.")
	print("You're all set! You can now log in to continue.")
	user_info = [passw, name]
	print("Signed up. You're all set!")
	clear()
	return user_info


def create_dir():
	fileWriter = open("user_accounts.txt", "a")

	fileWriter.close()

def create_entries():
	fileWriter = open("entries.txt", "a")

	fileWriter.close()


def user_update():
	fileWriter = open("user_accounts.txt", "w")
	if len(user_accounts) > 0:
		for line in user_accounts:
			fileWriter.write(encrypt(line) + "," + encrypt(user_accounts[line][0]) + "," + encrypt(user_accounts[line][1]) + "\n")


	fileWriter.close()


def clear():
	os.system('cls')



#main_code
user_pass = True
user_accounts = {}
entries = {}

clear()

while user_pass:
	print("  ____   _   __   ___  _  _ ")
	print(" |  _ \ | | /  \ | _ || \/ |")
	print(" | (_) || || ^^ ||  _|\   / ")
	print(" |____/ |_||_/\_||_\_\ |_|  ")
	print("")
	create_dir()
	load_users()
	print("Where all your personal secrets are hidden.")
	print("Log in to access your diary, or create an account if you are a new user.")
	print("")
	print("[1] Login")
	print("[2] Sign up")
	print("[3] EXIT")
	print("")
	choice = int(input("What do you want to do: "))
	clear()


	if choice == 1:
		ui()
		login()

	elif choice == 2:
		ui()
		print("Create an account now to make your very own diary!")
		while True:
			user = input("Enter your username: ")
			clear()
			if user in user_accounts:
				ui()
				print("That username is already taken. Please think of another one.")
				time.sleep(2)
				clear()

			else:
				user_info = signup(user)
				user_accounts[user] = user_info

			break

	elif choice == 3:
		user_update()
		ui()
		print("Thank you for using the program.")
		print("Program exits . . . ")
		time.sleep(2)
		clear()
		user_pass = False

	else:
		ui()
		print("Invalid choice.")
		time.sleep(2)
		clear()