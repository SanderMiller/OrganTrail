
def printResponse():
    Input = input()
    print("You Chose: " + response[0][int(Input)-1])



response = [['Pharaoh', 'Priest', 'Farmer'], ['follow Him', 'stay where you are']]
ScreenText= ['What is your name?',('Choose a character. Press 1 for ' + response[0][0] + '. Press 2 for ' + response[0][1]+ '. Press 3 for ' +response[0][2]+ '.'), 'Anubis asks you to follow him. What will you do?'+ ' Press 1 to ' + response[1][0] + '. Press 2 to ' + response[1][1], 'You follow him into a crowd, but soon you lose sight of him...', 'Anubis leaves you, you never make it to the Hall of Truth.']

print(ScreenText[0]) #'What is your name?'

name = input()
print("Hello "+name)
print(ScreenText[1]) #Choose a character. 
try:
    printResponse()

except(IndexError):
    print("Please Choose a number 1-3")
    printResponse()

print(ScreenText[2]) #Anubis asks you to follow him.
try:
    Input = input()
    if Input == '1':
        print(ScreenText[3])
    elif Input == '2':
        print(ScreenText[4])
except(IndexError):
    print("Please Choose a number 1-3")
    printResponse()

print('This concludes the Demo Verion of Organ Trail™ for more please stay tuned!!!')



