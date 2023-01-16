# 5-4
# letter=['salutation','name','product','verbed','room','animals','amount','percent','spokesman','job_title']
#
# print(f'Dear {letter[0]} {letter[1]},')
#
# print(f'Thank you for your letter. We are sorry that our {letter[2]} {letter[3]} in your {letter[4]}. Please note that it should never be used in a {letter[4]}, esepecially near any {letter[5]}.' )
#
#
# print(f'Send us your receipt and {letter[6]} for shipping and handling. We will send you another {letter[2]} that, in our tests, is {letter[7]}% less likely to have {letter[3]}.')
#
# print(f'Thank you for your support')
# print(f'Sincerely,\n{letter[8]}\n{letter[9]}')


# 5-5

# letter=['salutation','name','product','verbed','room','animals','amount','percent','spokesman','job_title']
#
# salutation='Dear'
# name='Dean'
# product='shoes'
# verbed='delivered'
# room='room number 511'
# animals='cats'
# amount='every product'
# percent='80%'
# spokeman='John Smith'
# job_title='CEO'
#
# print('Dear {0} {1},'.letter.format(salutation,name))

# print('Thank you for your letter. We are sorry that our {product} {verbed} in your {room}. Please note that it should never be used in a {room}, esepecially near any {animals}.' )
#
#
# print('Send us your receipt and {amount} for shipping and handling. We will send you another {product} that, in our tests, is {verbed}% less likely to have {letter[3]}.')
#
# print('Thank you for your support')
# print('Sincerely,\n{spokeman}\n{job_title}')
#






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