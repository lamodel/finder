import webbrowser

var = 'google'
user = input("F-I-N-D-E-R :) ")
print('searching...')

if user == var:
    webbrowser.open_new(f'{var}')

else:
    webbrowser.open_new(f'{user}')


#created by lamodel