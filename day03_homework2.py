#5.5

letter=('Dear {salutation} {name}\nThank you for your letter. We are sorry that out {product} {verbed} in your {room}.Please note that it should never be used in a {room},especially near any {animals}.')

print(letter.format(salutation='Dear',name='Dean',product='shoes',verbed='delivered',room=511,animals='cats'))
#이하 생략


# 5.6

an_English_submarine='McBoatface'
an_Australian_racehores='McHorseface'
a_Swedish_train='McTrainface'

print('Ducky %s' %an_English_submarine)
print('Gourdy %s' %an_Australian_racehores)
print('Spitzy %s'%a_Swedish_train)


# 5.7

print('Ducky {0}\nGourdy {1}\nSpitzy {2}'.format(an_English_submarine,an_Australian_racehores,a_Swedish_train))

# 5.8

print(f'Ducky {an_English_submarine}\nGourdy {an_Australian_racehores}\nSpitzy {a_Swedish_train}')



# 6.2

guess_me=7
number=1

while True:
    if guess_me>number:
        print('too low')
    elif number==guess_me:
        print('found it')
        break
    else:
        print('oops')
        break
    number+=1


# 6.3
guess_me=5

for number in range(10):
    if number<guess_me:
        print('too low')
    elif number==guess_me:
        print('found it')
    else:
        print('oops')