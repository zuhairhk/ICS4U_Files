def powerSet(a_set):
	''' powerSet() returns the a list of the power set of a set
	-- param
	a_set : set
	-- return
	list
	'''

	result = [set()]

	for i in a_set:
		result.append({i})

	i = 0
	while i < len(result):
		j = 0
		while j < len(result):
            print('why no wrk')
            #print('r i is:', result[i])
            #print('w i is', result[j])
			if result[i] | result[j] not in result:
				result.append(result[i] | result[j])
			j += 1
		else:
			i += 1

	return result

#a = powerSet({1,2,3,4,5,6})
a = powerSet({1,2,3})
a.sort()
print(a)
print(len(a))