



min_stones = 1
max_stones = 5
pile = 100



def valid_answer():
    while True:
        guess_text=input("enter your guess: ")
        try:
            guess = int(guess_text)
            if guess > max_stones or guess < min_stones:
                raise ValueError()
            return guess
        except:
            print("that's not a guess 🤨")






def play_nims(pile, max_stones):
    answer = valid_answer


    


    






#pile with 100 stones
#ask players if they want to play
#ask player one 
#subtrack from pile
#ask player two
#subtrack from pile
#

answer = input('do you want to play nims')

if answer == 'yes':
    print ("get ready to play NIMS")
    play_nims(pile, max_stones)



#while [pile is not empty]:
#   while [player 1's answer is not valid]:
#       [ask player 1]
#       [execute player 1's move]
# 
#   while [player 2's answer is not vali #           [ask player 2]
#            [execute player 2's move]
#
