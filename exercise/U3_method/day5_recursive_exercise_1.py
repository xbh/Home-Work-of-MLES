"""
def countDown(num):
	if num == 0:
		print(0)
	else:
		print(num,"",end="")
		return countDown(num-1)

countDown(6)
"""

def countUp(num,n=1):
	if n != num:
		print(n,"",end="")
		return countUp(num,n+1)
	else:
		print(num)

countUp(30)

"""

def palin(string,num):
	if string[num] != string[(-num-1)]:
		return False	
	
	elif num == -num-1:
		if string[num] == string[-num-1]:
			return True
	
	elif num == len(string)/2:
		return True

	else:
		return palin(string,num+1)

print(palin("2552",0))

"""

