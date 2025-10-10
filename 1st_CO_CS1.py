#Choose your own adventure story

#Asking for users name
#class User:
    #def __init__(self, name):

userName = input("What is your name traveler?: ")

#Starting of the story
def storyGame():
    usersResponse = input(f"Hello {userName}, would you like to play game? ")
#Story ideas:
    #Your main character is a person in their late twenties, who is very rebellious. The story begins at a luxury island resort.
    #A family get-together is arranged. It's a story about terror. Your character attempts to keep a low profile.

    if usersResponse == 'yes' or \
        usersResponse == 'Yes':
        print("Amazing lets begin: ")
    elif usersResponse == 'no' or \
            usersResponse == 'No':
        exit("Okay goodbye")
    else:
        exit("Sorry, I don't understand your input goodbye.")

    print("You and your family have decided to go to a luxury island resort for a family get-together. It's the perfect resort, it's near the beach, top tier food, everything.")
    print("You are quite the rebellious person and divide from the group as you enter the resort. Your family doesn't notice, and honestly doesn't seem to care.")

    user1stDoor = int(input("As you explore you come across a crossroads. You can either go through a grey and yellow industrial door (1), or glass doors that lead outdoors (2) "))

    if user1stDoor == 1:
        greyYellowDoor()
    elif user1stDoor == 2:
        outside()
    else:
            exit("Sorry, I don't understand your input goodbye.")

def greyYellowDoor():
        print("You go to the grey and yellow door and it reads 'employees only'. You enter anyway as you are rebellious and don't care. The door slams shut behind you and you are now in the dark.")
        darkness = int(input("Do you feel the wall for a light switch (1), or try to leave the room (2)"))

        if darkness  == 1:
            lightSwitch()
        elif darkness  == 2:
            coward()
        else:
            exit("Sorry, I don't understand your input goodbye.")

def lightSwitch():
        print("You feel the wall for a light switch. The walls feel almost sticky and vibrate slightly. You finally find a switch and flick it on. Suddenly it's as if the sun was spawned within the room.")
        print("You go blind for a few seconds, and fall to the ground holding your eyes. The pain subsides and you stand back up and uncover your eyes. You look around and realize...You are in a laboratory type place.")
        print("There is a massive tank in the middle of the room surrounded by wires and computers. You can't see inside as it is too murky. You look around at some of the papers on the desk, there are numbers and symbols you do not understand.")

        redButton = int(input("There is a big red button next to the tank. Do you press it (1), or leave the room (2)"))

        if redButton == 1:
            pressButton()
        elif redButton == 2:
            leaveRoom()
        else:
            exit("Sorry, I don't understand your input goodbye.")

def pressButton():
    print("You pressed the button next to the tank, and the water starts to drain. You take a couple steps back, but you are too intrigued to leave. As the water drains, the tank's glass starts to clear.")
    print("As the glass clears, you notice a paleish-green blob in the tank but you cant really see what it actually is. Suddenly...what seems to be an octopus tentacle slams on the side of the tank. The ground shakes and you are knocked off your feet.")
    print("You look around quickly and notice the door, you turn back and...the tank is empty. You stand up and turn around to run out the door, but yell out as a massive, one-eye, pale green octopus is covering the door.")

    octopusDoor = int(input("Do you try to fight the octopus (1), or try to look around to attempt to escape (2) "))

    if octopusDoor == 1:
        firstOctopusFight()
    elif octopusDoor == 2:
        firstOctopusEscape()
    else:
        exit("Sorry, I don't understand your input goodbye.")

def firstOctopusFight():
    print("You choose to fight. You stand firm and hold your ground, at least you try to. The octopus wraps one of it's tentacles around you. You try to wiggle free but it is useless, you are trapped.")
    exit("Your light fades out.")

def firstOctopusEscape():
    print("You choose to try and escape...but around you cannot see any way out. The octopus wraps one of it's tentacles around you. You try to wiggle free but it is useless, you are trapped.")
    exit("Your light fades out.")

def beatGame():
    print("You beat the game...")
    print("Congrats...") #add confetti and start undertale song "Home"
    print("Do you feel accomplished?")
    input("Or do you feel something different? ")
    print("Yes I let you input whatever you wanted with no consequences.")
    print("It is time for you to leave...")

def outside():
    print("You decide to go outside. You think that maybe going outside the sunshine and fresh air will help your nerves. Afterall, your family is a lot. You get outside and the sun blinds you for a second.")
    print("As your eyes adjust and you really look, the resort is on the beach. You step off the patio of the resort and you are standing on sand. 'Wow...' you think to yourself, this place is amazing.")
    print("You walk down near the water and look down at your shoes. Your sneakers are slightly damp and covered in sand, but it's strangely...peaceful. You look around you but...no one is there...As you look out into the ocean")
    print("a woman appears from the water and walks to you. She is very beautiful with long black hair, seafoam green eyes, and a long dark purple dress. She reaches her hand out to you to take...You feel called to take her hand...")

    seaNypmh = input("Do you? ")

    if seaNypmh == 'yes' or seaNypmh == 'Yes':
        bossFight()
    elif seaNypmh == 'no' or seaNypmh == 'No':
        exit("Your mind is closed, open it.")
    elif
        beatGame()
    elif

    else:
        exit("Sorry, you didn't open your mind. Goodbye.")

def bossFight():

def leaveRoom():
    print("You decide to leave as soon as you enter the room. So you walk out and head outside.")
    outside()

    def coward():
        print("")

storyGame()