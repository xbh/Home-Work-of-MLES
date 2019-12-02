points = 20
total = 2
print('Correct answers: {:^30},{}'.format(float(points/total), total/points))


b_dict = {'name': 'chuhao', 'age': 20, 'province': 'shanxi'}
print('my name is {name}, age is {age},from {province}'.format(**b_dict))

a_list = ['chuhao', 20, 'china']
print('my name is {0[0]},from {0[2]},age is {0[1]}'.format(a_list))
