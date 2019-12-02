'''
The art of violence in the programming.
Written by JerryX
'''
# ---------------Header-----------------

a_line = "{:*^30}".format("")
start_b = "{:*<1}".format("")
b_line = "{:^28}".format("Jerry's Simple Cashier")
c_line = "{:*^30}".format("")
end_b = "{:*>1}".format("")

print(a_line)
print(start_b, end="")
print(b_line, end="")
print(end_b)
print(c_line,"\n")

# --------------IPO Body 1--------------

# Ask for quantity
price_gold = float(input("How much of one gold block?\n"))
num_gold = float(input("How many gold blocks you will buy?\n"))

# Calculate the money that need to pay
num_need_pay = price_gold * num_gold
num_need_pay = round(num_need_pay, 2)

# Output how much need to pay
print("\nYou need to pay ${:.2f} to me.\n".format(num_need_pay))

# --------------IPO Body 2--------------

# Ask for how much have paid
num_paid = float(input("How much you paid?\n"))

# How much I need give back
num_paid = round(num_paid, 2)
num_remain = num_paid - num_need_pay
num_remain = round(num_remain, 2)


# Calculate how many of each bill & coin

# $50 bill
fifty_back = num_remain // 50
fifty_remain = num_remain % 50
fifty_remain = round(fifty_remain, 2)

# $20 bill
twenty_back = fifty_remain // 20
twenty_remain = fifty_remain % 20
twenty_remain = round(twenty_remain, 2)

# $10 bill
ten_back = twenty_remain // 10
ten_remain = twenty_remain % 10
ten_remain = round(ten_remain, 2)

# $5 bill
five_back = ten_remain // 5
five_remain = ten_remain % 5
five_remain = round(five_remain, 2)

# $2 bill
two_back = five_remain // 2
two_remain = five_remain % 2
two_remain = round(two_remain, 2)

# $1 bill
one_back = two_remain // 1
one_remain = two_remain % 1
one_remain = round(one_remain, 2)

# $0.25 bill
twentyfiveCent_back = one_remain // 0.25
twentyfiveCent_remain = one_remain % 0.25
twentyfiveCent_remain = round(twentyfiveCent_remain, 2)

# $0.1 bill
tenCent_back = twentyfiveCent_remain // 0.1
tenCent_remain = twentyfiveCent_remain % 0.1
tenCent_remain = round(tenCent_remain, 2)

# $0.05 bill
fiveCent_back = tenCent_remain // 0.05
fiveCent_remain = tenCent_remain % 0.05
fiveCent_remain = round(fiveCent_remain, 2)

# $0.01 bill
oneCent_back = fiveCent_remain / 0.01

# print out the answer
print("\nYou could get", num_remain, " doller back.\n")
print("You will get {:.0f} $50 bill(s)".format(fifty_back))
print("You will get {:.0f} $20 bill(s)".format(twenty_back))
print("You will get {:.0f} $10 bill(s)".format(ten_back))
print("You will get {:.0f} $5 bill(s)".format(five_back))
print("You will get {:.0f} $2 bill(s)".format(two_back))
print("You will get {:.0f} $1 bill(s)".format(one_back))
print("You will get {:.0f} 25 cents coin(s)".format(twentyfiveCent_back))
print("You will get {:.0f} 10 cents coin(s)".format(tenCent_back))
print("You will get {:.0f} 5 cents coin(s)".format(fiveCent_back))
print("You will get {:.0f} 1 cents coin(s)".format(oneCent_back))


# Halt
input("\nPress Enter button to exit\n")


# sometimes I believe compiler ignores all my comments


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
