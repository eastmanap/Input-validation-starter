# Apollos & Nathan
# Dec 10 2024
# Input Validation

# isalpha()
run = True

while run == True:
    message = input('Enter a message with only alphabetic characters:')

    if message.isalpha() == True:
        print(message)
        print('Valid input')
        run = False
    else:
        print('Invalid input.')
        print('Try again,')
