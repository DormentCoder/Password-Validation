# Password Validation by Coda

print('Password Validation v1.10 by Coda')
print('Your password must be at least 10 characters long')
print('Numbers and symbols are reccomended, however these are not mandated.')
password = input('Input a password: ')
def length(password):
    if len(password) < 9:
        print('Error!')
        print('Password is not strong enough.')
        print('Try again.')
        exit()
length(password)
password_check = input('Type in your password again: ')
if password_check != password:
    print('Error!')
    print('The passwords do not match.')
    print('Try again.')
else:
    print('Registration is successful.')