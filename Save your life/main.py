print("You were partying at your friend's place on the New Year's Eve! Completely drunk and in a sluggy condition, you fell asleep! You wake up in a jungle and find yourself lying on the ground. You feel like vomitting and somehow you control yourself. You have hardly managed your self when you see a glumpsy bear right some metres away from you growling with a ferrocious look!\nWhat would you do now?\n1.Run\n2.Lie down and wait to be crumpled under its feet\n3.Throw stones at it")
user_choice1 = int(input(">>>Enter the number of your choice: "))

if(user_choice1 == 1):
    print("\n\nYou run much more deeper into the jungle with more dense bushes. The sunlight could barely penetrate through the tall trees. But you can sense the bear running and growling in extreme anger. You need to think some of quickly.\n1. Hid behind a large stone\nClimb a tall tree\nContinue a running further into the jungle")
    user_choice2 = int(input(">>>Enter the number of your choice: "))
    if(user_choice2 == 1):
        print("You decide to crouch behind the large stone. The bear is now close to you and you try to control your breath. You see a beautiful flower beside your feet. The bear has now approached you and is standing you infront of him. What would you do now?\n1.Pick the flower and use it your protection\n2.Throw some stones at it\n3.Fight the fear with your full courage")
        user_choice3 = int(input(">>>Enter the number of your choice: "))
        if(user_choice3 == 1):
            print("The bear is now silent. That was a miracle the flower somehow managed to clam down the bear! Congratulations you survived!")
        elif(user_choice3 == 2):
            print("The stones did no harm to the bear. The bear pulls you up in its hand and tears you apart. You died!")
        else:
            print("Well fighting with bear was not a good option! You know the bear's a thousand times more stronger than you. You are defeated and are killed!")
    elif(user_choice2 == 2):
        print("You climbed up the large tree! But the bear was too tall, it easily got you down and crumpled you under its feet. You were killed.")
    else:
        print("You ran more deeper into the jungle and somehow managed to escape the bear! Congratulations you alive!")
elif(user_choice1 == 2):
    print("You were crushed under the bear's feet and died!")
else:
    print("The stones did no harm to the bear. The bear pulls you up in its hand and tears you apart. You died!")
    