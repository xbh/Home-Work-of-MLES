rows = int(input())
op_ele = []
op_count = []
op_counter =0

def RemoveRepeat(a):
    if(a == ''):
        return a
    b = ''
    for i in a:
        if (b == ''):
            b += i
        if(i == b[len(b)-1]):
            pass
        else:
            b = b+i
    return b


for i in range(rows):
    ip = str(input())
    # content = []
    counter = 1
    counter_list = []
    repTag = False
    simp_form = RemoveRepeat(ip)
    for x in range(len(ip) - 1):
        if ip[x] == ip[x + 1]:
            counter = counter + 1
            # content.append(ip[x])
        else:
            counter_list.append(int(counter))
            counter = 1
    if counter != 1:
        counter_list.append(int(counter))
    op_count.append(counter_list)
    op_ele.append(simp_form)

print(op_count)
print(op_ele)
