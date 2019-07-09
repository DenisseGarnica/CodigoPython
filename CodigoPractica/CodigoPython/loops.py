#simple loop
people =['Daniel', 'Denisse', 'Chispita']
print('**Simple Loop**')
for person in people:
	print('Current Person: {0}'.format(person))

#Break
print('**Break Loop**')
for person in people:
	if person == 'Chispita':
		break
	print('Current Person: {0}'.format(person))

