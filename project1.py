def displayIntro():
  #put an Introduction message to the users
  pass 

def displayNonProfits():
  #print all the non-profits to the screen numerically. For Example:
#    1. World Central Kitchen
#    2. Crisis Text Line
#    3. Heart to Heart International
  pass 


def main():
	pass #remove me and everywhere else I appear

	#steps: 
	#1. welcome the user using a unique Intro Message (use a function for this)
	#2. create a variable for each nonprofit/charity that keeps track of how much total money has been donated
	#3. display all the non-profits to the user and ask which one they would like to donate to 
	#4. then ask the user how much money they would like to donate to that specific charity chosen in step 3
	#5. update the variable created in step 2 with whatever amount the user wanted to donated
			#for example: missionbit = 0 -> user wants to donate 100 so you would add 100 to missionbit. missionbit is now 100
	#6. now display all the nonprofits with their new total amounts donated
    #7. repeat this process until the user wants to stop donating (only do this if you cover while loops)
	#push to github after every single step

def displayIntro():
    print ("Welcome to the nonprofit donations!")
    print("1. MissionBit")
    print("2. RedCross")
    print("3. SalvationArmy")

def displayNonprofits():
    Missionbit_balance = 0
    RedCross_balance = 0
    SalvationArmy_balance = 0 
    
    
def main():
    displayIntro()
    displayNonprofits()
    choice1 = "MissionBit_balance"
    choice2 = "RedCross_balance"
    choice3 = "SalvationArmy_balance"
    int(input("Enter which organization you want to donate to:  "))
    if choice1:
        Missionbit_balance = int(input("Enter how much money you would like to donate:  "))
        print(f'Total MissionBit Balance', Missionbit_balance)
    elif choice2:
        RedCross_balance = int(input("Enter how much money you would like to donate:  "))
        print(f'Total RedCross Balance', RedCross_balance)
    elif choice3:
        SalvationArmy_balance = int(input("Enter how much money you would like to donate:  "))
        print(f'Total SalvationArmy', SalvationArmy_balance)
    
    
    
main()
