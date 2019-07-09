#simple loop
people =['Daniel', 'Denisse', 'Chispita','Chanchita','Chanquito']
print('**Simple Loop**')
for person in people:
	print('Current Person: {0}'.format(person))

#Break
print('**Break Loop**')
for person in people:
	if person == 'Chispita':
		break
	print('Current Person: {0}'.format(person))

#Continue
print('**Continue Loop**')
for person in people:
	if person =='Chanchita':
		continue
	print('Curreny Person: {0}'.format(person))
#Range
print('**Range Loop**')
for i in range(len(people)):
	print(people[i])

for i in range (0,20):
	print('Number: {0}'.format(i))
#Count
count = 0
while count <=10:
	print('Count {0}'.format(count))
	count+=1

