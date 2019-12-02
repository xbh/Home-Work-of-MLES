int_a = int(input("Input a integer"))

if int_a % 3 == 0:
    print("Fizz!")
elif int_a % 5 == 0:
    print("Buzz!")
else:
    print(int_a,"\b!")

# ----------------------------------

num_small = int(input("How many small bars?"))
num_big = int(input("How many big bars?"))
num_target = int(input("How much you need in total?"))

num_small_use = 0

for num_small_use in range(num_small + 1):
    if (num_small_use + num_big * 5) == num_target:
        print(num_small_use)
        quit()
else:
    print("-1")
