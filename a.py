import random as rand
while True:
    x=rand.randint(1,100)
    count=0
    win=False

    while count<5:
        print("Attempt",count+1,"of 5")
        print("Chances left:",5-count)

        guess=int(input("Guess a number between 1 and 100:"))

        if guess <1 or guess >100:
            print("Enter a number between 1 and 100")
            continue

        count= count+1

        if guess==x:
            print("You won!")

            if count==1:
                print("Excellent!")
            elif count==2:
                print("Very good!")
            elif count==3:
                print("Good!")
            elif count==4:
                print("Accepted!")
            else:
                print("You won with luck!")

            win=True
            break

        elif guess>x:
            print("Enter a smaller number")
        else:
            print("Enter a bigger number")

        if abs(guess-x)<=5:
            print("Very close!")
        elif abs(guess-x)<=15:
            print("Close!")
        else:
            print("You are far away!")

    if win==False:
        print("You lost!")
        print("Your number was",x)

    again=input("Play again? Yes/No")

    if again!="yes":
        break

print("Goodbye!")