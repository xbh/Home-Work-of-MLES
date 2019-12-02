def pali(input_str,start,end):
    if start >= end:
        return True
    if input_str[start] == input_str[end]:
        return pali(input_str,start + 1,end - 1)
    else:
        return False


def string_times(str, n):
    if n == 1:
        return str
    else:
        return str + string_times(str, n - 1)



print(string_times("abc",4))