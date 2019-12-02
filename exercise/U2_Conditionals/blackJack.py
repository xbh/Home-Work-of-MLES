'''
Powered by JerryXie.
BlackJack Games
'''
# import
import random

# card database
card_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Card Initialization
card_a = random.choice(card_lst)
card_b = random.choice(card_lst)
card_c = random.choice(card_lst)
card_d = random.choice(card_lst)

# Return player's card
count_user = card_a + card_b
print("Your card is", card_a, card_b)

# Dealer's card
for count_dealer in range(12):
    count_dealer = count_dealer + random.choice(card_lst)

# FLag Initialization
hit_flag = "hit"

# Body
while hit_flag == "hit":
    hit_flag = input("Do you want to hit or stand?\n")
    if hit_flag == "hit":
        # Sending the card
        card_new = random.choice(card_lst)
        count_user = count_user + card_new
        print("Your new card is", card_new,
              "The point is", count_user, "right now!")
        if count_user <= 21:
            pass
        else:
            hit_flag = "stand"
            print("\nYou got over than 21 already, the dealer have",
                  count_dealer, "point.\n")
    elif hit_flag == "stand":
        # End of gambling
        print("OK, you have", count_user,
              "point and the dealer have", count_dealer, "point.\n")
    else:
        print("Wrong Input, try again")
        hit_flag = "hit"
else:
    # Judgement
    if count_user > 21:
        print("player loses")
    elif count_user < count_dealer and count_dealer <= 21:
        print("Player loses")
    elif count_user == 21:
        print("Player WIN!")
    elif count_user > count_dealer and count_user <= 21:
        print("Player WIN!")
    elif count_dealer == count_user:
        print("Draw! Play again")

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
