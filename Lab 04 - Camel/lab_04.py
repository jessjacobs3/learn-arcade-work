import random

def main():
    print("Welcome to the Disaster!")
    print("You have stolen some some headphones from Walmart. The police are after you and wants them back.")
    print("Make your way back home to your place on foot as you no longer have access to your car.")
    print("Do not get caught by the police.")
    print("")
    # Variables:

    miles_traveled= 0
    thirst = 0
    fatigue = 0
    just_traveled = -20
    canteen = 5
    oasis = 0
    done = False

    # start main loop
    while not done:
        fullspeed = random.randrange(20, 25)
        moderatespeed = random.randrange(10, 15)
        print("")
        print("A. Yay, you found some water. Drink it.")
        print("B. Go ahead and jog at moderate speed.")
        print("C. Sprint at full speed.")
        print("D. Take a rest. You are tired.")
        print("E. Check my status.")
        print("Q. Quit.")

        user_choice = input("What's your choice? ").upper()
        print()

        if user_choice.lower() == "q":
            done = True
            print("Goodbye.")

        # drink water
        elif user_choice.lower() == "e":
            print("Miles traveled: ", miles_traveled)
            print("Drinks some water", canteen)
            print("Your energy level is: ", fatigue, " joules full.")
            print("The police are ", just_traveled, "miles behind you.")

        elif user_choice.lower() == "d":
            fatigue = 0
            print("You are refreshed and now your fatigue is now at ", fatigue)
            just_traveled += random.randrange(7, 14)

        elif user_choice.lower() == "c":
            print("You traveled ", fullspeed, "miles!")
            miles_traveled += random.randrange(10, 20)
            thirst += 3
            fatigue += random.randrange(2, 6)
            just_traveled += random.randrange(7, 14)
            oasis = random.randrange(1, 11)

        elif user_choice.lower() == "b":
            print("You are ", moderatespeed, "miles further along!")
            miles_traveled += random.randrange(10, 20)
            just_traveled += moderatespeed
            thirst += 2
            fatigue += 4
            just_traveled += random.randrange(7, 14)
            oasis = random.randrange(2, 22)


        elif user_choice.lower() == "a":
            if canteen == 0:
                print("You are out of water.")
            else:
                canteen -= 1
                thirst *= 0
                print("You have ", canteen, "drinks left. You are no longer thristy.")

        if oasis == 10:
            fatigue *= 0
            thirst *= 0
            canteen = 2
            print("You found an oasis! After taking several drinks, you filled your canteen and you are refreshed.")

        if just_traveled <= 15:
            print("The police are drawing closer and closer.")

        if miles_traveled >= 125 and not done:
            print("You made it across campus, you win!")
            done = True

        if just_traveled >= miles_traveled:
            print("You got caught by the cops.")
            print("You are dead!")
            done = True

        if thirst > 7:
            print("You died of hydration; you did not drink enough water.")
            done = True

        if fatigue > 6 and fatigue >= 9 and not done:
            print("You are getting very tired.")

        if fatigue > 14:
            print("You are dead.")
            done = True

main()