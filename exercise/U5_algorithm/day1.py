nums = [1,2,3,4,5,6,7,8,9,10]

chg_flag = True

while chg_flag == True:
    chg_flag = False
    for i in range(len(nums) - 1):
        numFst = nums[i]
        numSec = nums[i + 1]
        if numSec > numFst:
            numFst = nums[i + 1]
            numSec = nums[i]
            chg_flag = True
        nums[i] = numFst
        nums[i + 1] = numSec
    

print(nums)