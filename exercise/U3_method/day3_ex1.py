
def backAround(input_str):
    last_chr = input_str[-1]
    output_str = last_chr + input_str + last_chr
    return output_str

print(backAround("abc"))
'''

def loneTeen(age1, age2):
    if age1 >= 13 and age1 <= 19:
        if age2 >= 13 and age2 <= 19:
            return False
        else:
            return True
    elif age2 >= 13 and age2 <= 19:
        return True
    else:
        return False


def endUp(inputStr):
    if len(inputStr) <= 3:
        outputStr = str.upper(inputStr)
    else:
        last3Chr = inputStr[-3:]
        firstchr = inputStr[0:len(inputStr) - 3]
        outputStr = firstchr + str.upper(last3Chr)
    return outputStr


def close10(var_a, var_b):
    if abs(var_a - 10) < abs(var_b - 10):
        return var_a
    elif abs(var_a - 10) > abs(var_b - 10):
        return var_b
    else:
        return 0



def double(input_value):
    output_val = input_value * 2
    return output_val


print("The num is: ", double(56))



def triple(input_val):
    out_val = input_val * 3
    triple(out_val)
    return out_val

print(triple(34))
'''