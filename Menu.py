import time
import random

Menu=str("(I)nstructions\n(P)lay\n(Q)uit")


menu=str("in")
game_status=str("in")




Instructions_page_1=str("This is a simple golf game in which each hole is 230m game away with par 5.")
Instructions_page_2=str("You are able to choose from 3 clubs, the Driver, Iron or Putter.")
Instructions_page_3=str("The Driver will hit around 100m, the Iron around 30m and the Putter around 10m.")
Instructions_page_4=str("The putter is best used very close to the hole.")

game_intro=str("You are 230 metres from the hole, the ball is infront of you. It is a straight line to the hole.")
game_menu_page_1=str("(D)river - around 100m")
game_menu_page_2=str("(I)ron - around 30m")
game_menu_page_3=str("(P)utter - around 10m")



PlayerName=str(input("what is your name? "))

print("Hello "+PlayerName+", Welcome to CommandGolf!")

time.sleep(1)
print(Menu)

def game_menu():
    time.sleep(3)
    print(game_menu_page_1)
    time.sleep(1)
    print(game_menu_page_2)
    time.sleep(1)
    print(game_menu_page_3)
    time.sleep(1)


def instructions():
    print(Instructions_page_1)
    time.sleep(3)
    print(Instructions_page_2)
    time.sleep(3)
    print(Instructions_page_3)
    time.sleep(3)
    print(Instructions_page_4)
    time.sleep(3)









def game():
    global swings_taken_int
    swings_taken_int=int(0)
    global swings_taken_str
    swings_taken_str=str(swings_taken_int)
    global distance_to_hole_int
    distance_to_hole_int=int(230)
    global distance_to_hole_str
    distance_to_hole_str=str(distance_to_hole_int)

    print(game_intro)
    time.sleep(1)

    while game_status=="in":
        game_menu()
        club_choice=str(input("choose your club: "))
        if club_choice=="D":
            swing_distance_int=random.randint(80,120)
            swing_distance_str=str(swing_distance_int)
            distance_to_hole_int=distance_to_hole_int-swing_distance_int
            distance_to_hole_str=str(distance_to_hole_int)
            print("You chose the Driver and hit "+swing_distance_str+" m!\nYou are now "+distance_to_hole_str+" away from the hole with "+swings_taken_str+" swings taken!")
            swings_taken_int=swings_taken_int+1
        elif club_choice=="I":
            swing_distance_int=random.randint(24,36)
            swing_distance_str=str(swing_distance_int)
            distance_to_hole_int=distance_to_hole_int-swing_distance_int
            distance_to_hole_str=str(distance_to_hole_int)
            print("You chose the Iron and hit "+swing_distance_str+" m!\nYou are now "+distance_to_hole_str+" away from the hole with "+swings_taken_str+" swings taken!")
            swings_taken_int=swings_taken_int+1
        elif club_choice=="P"and distance_to_hole_int<=10:
            swing_distance_int=random.randint(distance_to_hole_int*0.8,distance_to_hole_int*1.2)
            swing_distance_str=str(swing_distance_int)
            distance_to_hole_int=distance_to_hole_int-swing_distance_int
            distance_to_hole_str=str(distance_to_hole_int)
            print("You chose the Putter and hit "+swing_distance_str+" m!\nYou are now "+distance_to_hole_str+" away from the hole with "+swings_taken_str+" swings taken!")
            swings_taken_int=swings_taken_int+1
        elif club_choice=="P" and distance_to_hole_int>=10:
            swing_distance_int=random.randint(8,12)
            swing_distance_str=str(swing_distance_int)
            distance_to_hole_int=distance_to_hole_int-swing_distance_int
            distance_to_hole_str=str(distance_to_hole_int)
            print("You chose the Putter and hit "+swing_distance_str+" m!\nYou are now "+distance_to_hole_str+" away from the hole with "+swings_taken_str+" swings taken!")
            swings_taken_int=swings_taken_int+1
            
            












while menu=="in":
    time.sleep(1)
    MenuChoice=str(input("enter choice: "))
    instructions()
    if MenuChoice == "Q":
        print("Farewell and thanks for playing "+PlayerName)
        menu=str("out")
    elif MenuChoice=="I":
        print(Menu)
    elif MenuChoice=="P":
        game()
