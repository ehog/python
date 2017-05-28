# Battle Rules
num_knights = int(input('How many knights? '))
print('You entered: ' + str(num_knights))

day = input('What day is it? ')
#day = 'Sunday'
print('You entered: ' + day)

enemy = input('Enter the type of enemy: ')
#enemy = 'killer bunny'
print('You entered' + enemy)

if enemy == 'killer bunny':
    print('Holy Hand Grenade!')
else:
    if num_knights < 3 or day == 'Monday':
        print('Retreat!')
    elif num_knights >= 10 and day == 'Wednesday':
        print('Trojan Rabbit!')
    elif day == 'Tuesday':
        print('Taco Night')
    else:
        print('Truce?')
