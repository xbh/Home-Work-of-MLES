myAnimal = ["cat", "dog", "lizard", "pig", "wtf", "wahh"]
leng = len(myAnimal)

for i in range(0,123):
    for num in range(0,leng):
        lasrt_chr = ord(myAnimal[num][-1])
        if lasrt_chr == i:
            print(myAnimal[num])

# ---------------------------

num_lst = [1,2,3,4,5]

for i in range(0,len(num_lst)):
    temp = num_lst[i]