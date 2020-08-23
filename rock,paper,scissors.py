#comp to player
import random

while True:

    print("\n--------------------------------------------------------------")
    print("This is a game of rock paper scissors aganist a bot")
    print("---------------------------------------------------------------- \n")
    t = 0
    win = 0
    lose = 0
    tie = 0

   
    ran = ["rock" ,"paper" , "scissors"]
    print( "win = %s  lose = %s  tie = %s" %(win , lose , tie))
    times = int(input("Enter the number of time  you want to play:  "))
    print("--------------------------------------------------------------\n")
    
    while t <times:
       
        player = input("player enter your choice(rock ,paper , scissors) : ")

        
        robo = random.choice(ran)
        if robo == player:
            tie+=1
            print("it is a tie")
        if player == ran[0]:
            if robo == ran[1]:
                lose+=1
                print("The computer wins")
        if player == ran[0]:
            if robo == ran[2]:
                win+=1
                print("The player wins")
        if player == ran[1]:
            if robo == ran[0]:
                win+=1
                print("The player wins")
        if player == ran[1]:
            if robo == ran[2]:
                lose+=1
                print("The computer wins")
        if player == ran[2]:
            if robo == ran[0]:
                lose+=1
                print("The computer wins")
        if player == ran[2]:
            if robo == ran[1]:
                 win+=1 
                 print("The player wins")
       
        t =t+1
    print("\n--------------------------------------------------------------\n")
    print( "win = %s  lose = %s  tie = %s" %(win , lose , tie))
    


    break









