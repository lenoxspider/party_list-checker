#names of people invited to your party
guest_list = ['david', 'charles', 'walter', 'steve', 'anonymous', 'kido']
user_name = input('Enter a name: ')
user_small = user_name.lower()
print()


def validat():
    if user_small in guest_list:
        print('Welcome to the party, {}' .format(user_name))
    else:
         print('Sorry, {}, you\'re not on the list.' .format(user_name))

while True:
    user_name = input('Enter a name: ')
    user_small = user_name.lower()
    if user_small == 'exit':
        break
    validat()
print()
