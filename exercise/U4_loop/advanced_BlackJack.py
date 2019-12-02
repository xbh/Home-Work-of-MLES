'''
Powered by Jerry Xie
The advanced Black Jack game
Within the split and foolproof feature
Date: 4/29/2018
'''
# import the library
import random

# get the list of possiable cards
card_lst = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

# set total money & bet money
bet_total = 10000
bet_money = input("How much money you wanna bet?\n")


# the judgement module of bet money
def bet_judge(bet_num):
    num_bol = str.isdigit(bet_num)
    if num_bol != True:
        return False
    elif int(bet_num) <= bet_total:
        return True
    else:
        return False


# Wrong input lock
bet_flag = bet_judge(bet_money)
while bet_flag != True:
    bet_money = input("Wrong input, try again!\n")
    bet_flag = bet_judge(bet_money)


# the new card given module
def get_card(total_count):
    new_card = random.choice(card_lst)
    if new_card == "J" or new_card == "Q" or new_card == "K":
        new_card_value = 10
    elif new_card == "Ace":
        difference = 21 - total_count
        if difference >= 11:
            new_card_value = 11
        else:
            new_card_value = 1
    else:
        new_card_value = new_card
    return (new_card_value, new_card)


# initialization of both point count
dealer_count = 0
player_count = 0

# initialization of hit flag
print("Let's start!")
hit_flag = "hit"

# dealer #1 get card module
while dealer_count <= 17:
    dealer_count = dealer_count + get_card(dealer_count)[0]

# get two cards to player
player_card_a = get_card(player_count)
player_card_b = get_card(player_count)

# set the same card flag
if player_card_a == player_card_b:
    same_card_flag = True
else:
    same_card_flag = False

# count the point of player
player_count = player_card_a[0] + player_card_b[0]


print("Your card is", player_card_a[1], "and", player_card_b[1])

# check the money condiction & initializing
bet_flag = bet_judge(bet_money)
player_money = int(bet_money)
bet_total = bet_total - int(bet_money)

# looping main body
while hit_flag == "hit":
    # split check
    if same_card_flag == True:
        mod = str(input("You got two same card, do wanna split them?\n"))
        if mod == "yes":
            break
        elif mod == "no":
            same_card_flag = False
            pass
        else:
            print("Wrong Input, try again")
            hit_flag = "hit"
    else:
        # bet money flag check
        if bet_flag == True:
            pass
        else:
            print("Game over, pauper!")
            same_card_flag = False
            hit_flag = "stand"
            break
        # start of one role
        hit_flag = input("Do you want to hit or stand?\n")
        if hit_flag == "hit":
            # get a new card & count
            card_new = get_card(player_count)
            player_count = player_count + card_new[0]
            print("Your new card is", card_new[1],
                  ", The point is", player_count, "right now!")
            # end up if already over 21
            if player_count <= 21:
                pass
            else:
                hit_flag = "stand"
                print("\nYou got over than 21 already, the dealer have",
                      dealer_count, "point.\n")
                if dealer_count > 21:
                    player_money = player_money * 2
                    bet_total = bet_total + player_money
                    print("player WIN!, you have",
                          bet_total, "money right now")
                elif player_count > 21:
                    player_money = 0
                    bet_total = bet_total + player_money
                    print("player loses, you have",
                          bet_total, "money right now")
                countinue_flag = "yes"
                # countinue for next role
                while countinue_flag == "yes":
                    countinue_flag = input(
                        "Do you want to countinue? Yes or No?")
                    if countinue_flag == "yes" or countinue_flag == "Yes":
                        print("You have", bet_total, "doller now")
                        hit_flag = "hit"
                        # initialization
                        player_card_a = get_card(player_count)
                        player_card_b = get_card(player_count)
                        player_count = player_card_a[0] + player_card_b[0]
                        print("Your card is",
                              player_card_a[1], "and", player_card_b[1])
                        dealer_count = 0
                        while dealer_count <= 17:
                            dealer_count = dealer_count + \
                                get_card(dealer_count)[0]
                        countinue_flag = ""
                        bet_flag = bet_judge(bet_money)
                        player_money = int(bet_money)
                        bet_total = bet_total - int(bet_money)
                    # end up if player refuse to countinue
                    elif countinue_flag == "no" or countinue_flag == "No":
                        print("Thanks for playing, you have",
                              bet_total, "doller now, congratulation！")
                    else:
                        print("Wrong input. Try again")
                        countinue_flag = "yes"
        # calculate result
        elif hit_flag == "stand":
            print("OK, you have", player_count,
                  "point and the dealer have", dealer_count, "point.\n")
            if dealer_count > 21:
                player_money = player_money * 2
                bet_total = bet_total + player_money
                print("player WIN!, you have", bet_total, "money right now")
            elif player_count < dealer_count:
                player_money = 0
                bet_total = bet_total + player_money
                print("Player loses, you have", bet_total, "money right now")
            elif player_count == 21:
                player_money = player_money * 2
                bet_total = bet_total + player_money
                print("Player WIN! You have", bet_total, "money right now")
            elif player_count > dealer_count:
                player_money = player_money * 2
                bet_total = bet_total + player_money
                print("Player WIN! You have", bet_total, "money right now")
            elif player_count == dealer_count:
                bet_total = bet_total + player_money
                print("Draw! Play again")
            # set the flag for asking the countinue
            countinue_flag = "yes"
            player_money = 0
            # countinue for next role
            while countinue_flag == "yes":
                countinue_flag = input("Do you want to countinue? Yes or No?")
                if countinue_flag == "yes" or countinue_flag == "Yes":
                    print("You have", bet_total, "doller now")
                    hit_flag = "hit"
                    # initialization
                    player_count = 0
                    player_card_a = get_card(player_count)
                    player_card_b = get_card(player_count)
                    player_count = player_card_a[0] + player_card_b[0]
                    print("Your card is",
                          player_card_a[1], "and", player_card_b[1])
                    dealer_count = 0
                    while dealer_count <= 17:
                        dealer_count = dealer_count + get_card(dealer_count)[0]
                    countinue_flag = ""
                    bet_flag = bet_judge(bet_money)
                    player_money = int(bet_money)
                    bet_total = bet_total - int(bet_money)
                elif countinue_flag == "no" or countinue_flag == "No":
                    print("Thanks for playing, you have",
                          bet_total, "doller now, congratulation！")
                else:
                    print("Wrong input. Try again")
                    countinue_flag = "yes"
        else:
            print("wrong input, try again!")
            hit_flag = "hit"

# initialization
player_count = 0
result_lst = {"1": "", "2": ""}  # a dict to storage the result

# split module
while same_card_flag == True:
    # money check lock
    if bet_flag == True:
        pass
    else:
        print("Game over, pauper!")
        same_card_flag = False
        hit_flag = "stand"
        break
    # main looping body
    for i in range(1, 3):
        hit_flag = "hit"
        player_count = player_card_a[0]
        while hit_flag == "hit":
            print("For set " + str(i) + ", do you want to hit or stand?")
            hit_flag = input()
            # get new card
            if hit_flag == "hit":
                card_new = get_card(player_count)
                player_count = player_count + card_new[0]
                print("Your new card is", card_new[1],
                      ", The point is", player_count, "right now!")
                if player_count <= 21:
                    pass
                else:
                    # end up if already over than 21
                    print("\nYou got over than 21 already, the dealer have",
                          dealer_count, "point.\n")
                    hit_flag = "stand"
                    if dealer_count > 21:
                        result_lst[str(i)] = True
                        print("player WIN!")
                    elif player_count > 21:
                        result_lst[str(i)] = False
                        print("player lose")
            elif hit_flag == "stand":
                # calculate the result and storage into the dict
                print("OK, you have", player_count,
                      "point and the dealer have", dealer_count, "point.\n")
                if player_count > 21:
                    result_lst[str(i)] = True
                    print("player WIN!, you have")
                elif dealer_count > 21:
                    result_lst[str(i)] = True
                    print("player WIN!")
                elif player_count < dealer_count:
                    result_lst[str(i)] = False
                    print("Player loses")
                elif player_count == 21:
                    result_lst[str(i)] = True
                    print("player WIN!")
                elif player_count > dealer_count:
                    result_lst[str(i)] = True
                    print("player WIN!")
                elif player_count == dealer_count:
                    print("Draw! Play again")
            else:
                print("Wrong Input, try again")
                hit_flag = "hit"
    else:
        # judge the result
        if result_lst["1"] == False or result_lst["2"] == False:
            # cslculate the money
            player_money = 0
        else:
            player_money = player_money * 2
            bet_total = bet_total + player_money
        countinue_flag = "yes"
        while countinue_flag == "yes" or countinue_flag == "Yes":
            # ask for countinue
            print("You got", bet_total, "doller right now!")
            countinue_flag = input("Do you want to countinue? Yes or No?")
            if countinue_flag == "yes":
                print("You have", bet_total, "doller now")
                # initialization if player want next role
                same_card_flag = True
                hit_flag = "hit"
                count_lst = {"1": "", "2": ""}
                print("Your card is",
                      player_card_a[1], "and", player_card_b[1])
                bet_flag = bet_judge(bet_money)
                player_money = int(bet_money)
                bet_total = bet_total - int(bet_money)
                dealer_count = 0
                # dealer gets cards
                while dealer_count <= 17:
                    dealer_count = dealer_count + get_card(dealer_count)[0]
                # break the "while" looping body
                break
            elif countinue_flag == "no" or countinue_flag == "No":
                # end up the game
                print("Thanks for playing, you have",
                      bet_total, "doller now, congratulation！")
                countinue_flag = ""
                same_card_flag = False
            else:
                print("Wrong input. Try again.")
                countinue_flag = "yes"

# Halt
input("\nPress Enter button to exit\n")


'''
zoom it smaller
                      :;J7, :,                        ::;7:
                      ,ivYi, ,                       ;LLLFS:
                      :iv7Yi                       :7ri;j5PL
                     ,:ivYLvr                    ,ivrrirrY2X,
                     :;r@checkJ:                :ivu@ingramD.
                    :iL7::,:::iiirii:ii;::::,,irvF7rvvLujL7ur
                   ri::,:,::i:iiiiiii:i:irrv177JX7rYXqZEkvv17
                ;i:, , ::::iirrririi:i:::iiir@ZOEii;L8OGJr71i
              :,, ,,:   ,::ir@johnX.irii:i:::j1jri7ZBOS7ivv,
                 ,::,    ::rv77iiiriii:iii:i::,rvLq@nidghoog
             ,,      ,, ,:ir7ir::,:::i;ir:::i:i::rSGGYri712:
           :::  ,v7r:: ::rrv77:, ,, ,:i7rrii:::::, ir7ri7Lri
          ,     2OBBOi,iiir;r::        ,irriiii::,, ,iv7Luur:
        ,,     i78MBBi,:,:::,:,  :7FSL: ,iriii:::i::,,:rLqXv::
        :      iuMMP: :,:::,:ii;2GY7OBB0viiii:i:iii:i:::iJqL;::
       ,     ::::i   ,,,,, ::LuBBu BBBBBErii:i:i:i:i:i:i:r77ii
      ,       :       , ,,:::rruBZ1MBBqi, :,,,:::,::::::iiriri:
     ,               ,,,,::::i:  @jerry.x       ,:,, ,:::ii;i7:
    :,       rjujLYLi   ,,:::::,:::::::::,,   ,:i,:,,,,,::i:iii
    ::      BBBBBBBBB0,    ,,::: , ,:::::: ,      ,,,, ,,:::::::
    i,  ,  ,8BMMBBBBBBi     ,,:,,     ,,, , ,   , , , :,::ii::i::
    :      iZMOMOMBBM2::::::::::,,,,     ,,,,,,:,,,::::i:irr:i:::,
    i   ,,:;u0MBMOG1L:::i::::::  ,,,::,   ,,, ::::::i:i:iirii:i:i:
    :    ,iuUuuXUkFu7i:iii:i:::, :,:,: ::::::::i:i:::::iirr7iiri::
    :     :rkY@mr.lee:::::, ,:ii:::::::i:::::i::,::::iirrriiiri::,
     :      5BMBBBBBBSr:,::rv2kuii:::iii::,:i:,, , ,,:,:i@marcoY.,
          , :r50EZ8MBBBBGOBBBZP7::::i::,:::::,: :,:,::i;rrririiii::
              :jujYY7LS0ujJL7r::,::i::,::::::::::::::iirirrrrrrr:ii:
           ,:  :@charlieC.:,:,,,::::i:i:::::,,::::::iir;ii;7v77;ii;i,
           ,,,     ,,:,::::::i:iiiii:i::::,, ::::iiiir@alcatraz.r;7:i,
        , , ,,,:,,::::::::iiiiiiiiii:,:,:::::::::iiir;ri7vL77rrirri::
         :,, , ::::::::i:::i:::i:i::,,,,,:,::i:i:::iir;@aslanW.ii:::
'''
