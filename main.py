# Apollos & Nathan
# Dec 10 2024
# Input Validation

# stage 2
run = True

while run == True:
    message = input('Enter a message with only numeric characters that is longer than 5 characters:')

    if message.isdigit() == True and len(message) >= 5:
        print(f'"{message}" is a valid message.')
        run = False
    else:
        print('Invalid input.')
        print('Try again,')
