print ("Hey! Welcome to my new game. Made by Jack Wilson. Version 0.1.8, Published 10.28.16")
print ("""\     ____.__________  __      ____________    ________                              
    |    |\______   \/  \    /  \______   \  /  _____/_____    _____   ____   ______
    |    | |     ___/\   \/\/   /|     ___/ /   \  ___\__  \  /     \_/ __ \ /  ___/
/\__|    | |    |     \        / |    |     \    \_\  \/ __ \|  Y Y  \  ___/ \___ \ 
\________| |____|      \__/\  /  |____|      \______  (____  /__|_|  /\___  >____  >
                            \/                      \/     \/      \/     \/     \/""")
print ("Ready to play?")
input (" Press ENTER to continue")
print ("Ok! Lets get started!")
print ("What is your name?")
name = input()
input ("""Welcome,""" +name+""", to the quest of Tarquinius. A truly immersive, great, game. Created by Jack Wilson under JPWP Games, with help from Lucas Stocks, Andrew Shields, Griffin Reinhardt Hepler, and all of the players. Be prepared, to be immersed.~Jack
PRESS ENTER TO CONTINUE.""")
print (" First day. You wake up and meet Fred. Befriend fred?")
while True:
    d1a = input ("Do you want to: A) Befriend Fred. B) Be mean to Fred. [A/B]? : ")
    if d1a == "A":
        print ("You befriend fred. You now have a friend..")
        break
    elif d1a == "B":
        print ("You angered Fred. He kills you. RIP.")
        quit()
    else :
    	
    	print ("Incorrect input")
print ("Fred will now travel along side you.")
input ("You like fred. You decide to keep him as your friend. PRESS ENTER TO CONTINUE")
while True:
    d1a = input ("While you travel through town, you find some golden coins. Do you steal them or pass by and let it go?A - Steal. B - Let it go.")
    if d1a == "A":
        print ("You steal the coins. A gaurd sees you. \""+name+"!You have sinned! Give these pieces to me or SUFFFER!\" ""You give him the coins.")
        break
    elif d1a == "B":
        print ("A gaurd notices your good deed and decides to tell fellow gaurds to help you in times of trouble.")
        break
    else:
        print ("Incorrect input")
print ("After a long day, you go to sleep.")
input ("Press ENTER to continue.")
print (" Ahh, a fresh new day for " + name + ". Cant wait to see what happens!")
print (" DAY 2. Ready to go?")
input ("Press ENTER to continue")
while True:
	d1a = input ("As you step outside, Fred greets you. you can go out and adventure (A) or stay and meet more people from the town. (B). Please type your response")
	if d1a == "A":
		print ("You go out and adventure. While adventuring, you encounter a dragon. How will you fight it?")
		while True:
			d1b = input ("You can (A) play aggressive and go for a lunge or (B) play defensively and stay back.")
			if d1b == "A":
				print ("When you go for a lunge, you hit right in the heart and kill him. Congratulations!  Your quick wits saved you this time but maybe not next time. You now decide to go to the lounge and meet new people.")
			elif d1b == "B":
				("This dragon could breath fire your shield has been melted and you die.""\"Nooooo!""You hear fred shout")
				quit()
			else:
				print ("Incorrect input,"+name+".")
	elif d1a == "B":
		print ("At the town you discover other things. Meet new people, find some useless items. .")
		break
	else:
		print ("Incorrect input,"+name+".")
