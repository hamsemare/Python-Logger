import sqlite3

connection=None
cursor= None
accountN= None




# Login 
def Login():
	global connection, cursor, accountN
	names=[]
	print("To quit enter Q at anytime!")

	# Check from the database
	cursor.execute('''
		select * 
		from user
		''')

	dataNames= cursor.fetchall()
	for n in dataNames:
		na= list(n)
		names.append(na)

	accounts=[]
	for i in names:
		accounts.append(i[0])

	while True:
		name= input("Enter Account Name: ")
		if(name=="q" or name=="Q"):
			exit(0)
		if(name in accounts):
			accountN= name
			return 
		else:
			print("Account Name does not exist!!!")
			con= input("If you want to Create an Account, Enter C or Anything else to Try Again: ")
			if(con=="q" or con=="Q"):
				exit(0)
			if (con=="c" or con=="C"):
				Create()
			print("\n"*10)
		




# Create an Account
def Create():
	global connection, cursor, accountN
	names=[]
	print("To quit enter Q at anytime!")

	i= input("Enter First and Last Name: ")

	if(i=="q" or i=="Q"):
			exit(0)

	# Check the database
	cursor.execute('''
		select * 
		from user
		''')
	dataNames= cursor.fetchall()
	for n in dataNames:
		na= list(n)
		names.append(na)
	accounts=[]
	for i in names:
		accounts.append(i[0])

	while True:
		name= input("Enter Account Name: ")
		if(name=="q" or name=="Q"):
			exit(0)
		if(name not in accounts):
			accountN= name
			cursor.execute('''insert into user values (?,?);''', (accountN,i))
			connection.commit()
			return 
		else:
			print("Account Name already exist!!!")
			con= input("If you want to Login, Enter L or Anything else to Try Again: ")
			if(con=="q" or con=="Q"):
				exit(0)
			if (con=="l" or con=="L"):
				Login()
			print("\n"*10)






# Show workout list of the user
def show():
	global accountN, cursor, connection
	print("\n"*20)
	print("Show Workouts")
	print("-"*10)
	print("To quit enter Q at anytime!")
	print("\n"*2)

	# Retrieve all workouts associated to the Account Name



	print("Do you want to continue?")
	q= input("Enter Q to Quit or Anything else to Continue: ")
	if(q=="q" or q=="q"):
		return
	else:
		print("\n"*5)
		home()




# Add a workout for the user
def add():
	global accountN, cursor, connection
	print("\n"*20)
	print("Add workout")
	print("-"*10)
	print("To quit enter Q at anytime!")
	print("\n"*2)

	# Workout needs name, reps,
	workoutN=input("Enter Workout name: ") 
	sets=input("Enter # of Sets: ")
	reps=input("Enter # of Reps: ")

	# add to database

	print("Do you want to continue?")
	q= input("Enter Q to Quit or Anything else to Continue: ")
	if(q=="q" or q=="q"):
		return
	else:
		print("\n"*5)
		home()



# HOME DASHBOARD
# Prompt the user to show workouts or add a workout
def home():
	global accountN, cursor, connection
	print("\n"*20)
	print("Welcome to the HOME DASHBOARD")
	print("--"*10)
	print("To quit enter Q at anytime!")
	print("\n"*2)
	
	while True:
		print("NUMBER\t\t| CHOICE")
		print("--"*20)
		print("1\t\t  Add a Workout")
		print("2\t\t  Show Workouts")
		print("--"*20)
		choice= input("Choice: ")
		if(choice=="q" or choice=="Q"):
			exit(0)

		if(choice=="1"):
			add()

		elif(choice=="2"):
			show()
		
		print("\n"*5)




# Main function for the program 
def main():
	global connection, cursor
	connection= sqlite3.connect("database.db")
	cursor=connection.cursor()
	print("\n"*100)
	print("Welcome to the Logger!!!")
	print("--"*10)
	print("\n"*10)
	while True:
		print("To quit enter Q at anytime!")
		print("What do you want to do? Login or Create an account")
		log=input("Enter L for Login or C for Create account: ")
		if(log=="q" or log=="Q"):
				exit(0)

		if(log=="L" or log=="l"):
			print("Welcome to Login")
			print("--"*10)
			print("\n"*20)
			Login()
			home()

		elif(log=="C" or log=="c"):
			print("Welcome to Create Account")
			print("--"*10)
			print("\n"*20)
			Create()
			home()

		else:
			print("\n"*20)

	print("\n" * 10)

main()




