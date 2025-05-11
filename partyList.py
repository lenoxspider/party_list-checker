#names of people invited to your party
guest_list = ['david', 'emma', 'gideon', 'suzzy', 'matthew', 'isaac']
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

#AI answer
guest_list = ['david', 'emma', 'gideon', 'suzzy', 'matthew', 'isaac']

def validate(name):
    if name in guest_list:
        print(f"Welcome to the party, {name.capitalize()}!")
    else:
        print(f"Sorry, {name.capitalize()}, you're not on the list.")

while True:
    user_input = input("Enter a name: ").lower()
    if user_input == 'exit':
        break
    validate(user_input)
