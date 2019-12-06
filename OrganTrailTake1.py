import random
def printResponse():
    attributes = []
    Input = input()
    print("You Chose: " + response[0][int(Input)-1])
    if Input == '1':
        health = 15
        strength = 90
        merit = 0
    elif Input == '2':
        health = 10
        strength = 75
        merit = 0
    elif Input == '3':
        health = 5
        strength = 50
        merit = 0
    attributes.append(health)
    attributes.append(strength)
    attributes.append(merit)
    print('Your attributes are: Health = ' + str(attributes[0]) + ' Strength = ' + str(attributes[1]))
    return attributes




currentScenario = 'Scenario1'

dialogue = {
    'Scenario1': ['Choose your character', ['Pharaoh (Easy)', 'Priest (Normal)', 'Farmer (Hard)'], ['Scenario2', 'Scenario2', 'Scenario2']],
    'Scenario2': ['Anubis asks you to follow him. What will you do?', ['follow him', 'stay where you are'], ['Scenario3', 'ScenarioEnd']],
    'Scenario3': ['You follow him into a crowd, but soon you lose sight of him... you look around, there is a traveler standing by themselves at the wall, what would you like to do',
                 ['Approach them and ask for directions', 'Fight them for food (or bragging rights)', 'make your way on your own'], ['Scenario4', 'ScenarioFight', 'ScenarioEnd']],
    'Scenario4': ['You approach the stranger. She turns around and you notice her appearance. She had the body of a leopard, but her head was that of a hippopotamus. She held a "Khopesh", a massive sword and sickle hybrid. When she spoke, her voice was powerful and intimidating."Hello weary traveler, I am Henet Requ, guardian of the portal of fire. You look lost, would you like my assistance?"',
                 ['Accept her offer', 'Make your way on your own', 'challenge her to a dance off'], ['Scenario5', 'Scenario6', 'ScenarioEnd']],
    'Scenario5': ['"Hello Henet, I was following Anubis but seem to have lost my way, do you know the way to the Hall of Maat?" Her brow furrowed. I do know the way, although it is very treacherous. You must follow me.', ['Follow her', 'come on seriously, follow her', 'why are you not trusting Henet'], ['ScenarioEnd', 'ScenarioEnd', 'ScenarioEnd']],
    'Scenario6': ['You try to make it through crowd on your own. Eventually after fighting the current of souls you see a gate . There appear to be two options, a water and land route. What do you do?', ['Approach the land route gate.','Approach the water route'], ['ScenarioEnd', 'ScenarioEnd']],
    'ScenarioEnd': ['Alas, you perish, never to set eyes on the Hall of Maat. Thanks for playing!', ['you lose', 'you lose (even more horribly)'], ['Scenario1', 'Scenario1']]
}




def fight(strength, health, currentScenario, lastScenario):
    outcome = random.randint(1,100)
    if outcome <= strength:
        health += 3
        currentScenario = lastScenario
        print('Congrats, you won!\n')
    else:
        currentScenario = 'ScenarioEnd'
        print('Sorry, you lost.\n')
    return health, currentScenario



def gameplay(currentScenario):
    print('What is your name?')
    name = input()
    print("Hello "+name)
    scenarioCount = 0
    while 1:

        if currentScenario == 'ScenarioFight':
            [health, currentScenario] = fight(attributes[1], attributes[0], currentScenario, lastScenario)

        print('\n' +dialogue[currentScenario][0])

        numOptions = len(dialogue[currentScenario][1])
        if numOptions == 3:
            responseString3 = 'Press 1 for ' + dialogue[currentScenario][1][0] + '. Press 2 for ' + dialogue[currentScenario][1][1] + '. Press 3 for ' + dialogue[currentScenario][1][2]+ '.\n'
            print(responseString3)
        elif numOptions == 2:
            responseString2 = 'Press 1 for ' + dialogue[currentScenario][1][0] + '. Press 2 for ' + dialogue[currentScenario][1][1] +'.\n'
            print(responseString2)

        Input = input()
        if currentScenario == 'Scenario1':
            attributes = []

            if Input == '1':
                health = 15
                strength = 90
                merit = 0
                characterFood = 3
            elif Input == '2':
                health = 10
                strength = 75
                merit = 0
                characterFood = 5
            elif Input == '3':
                health = 5
                strength = 50
                merit = 0
                characterFood = 7
            attributes.append(health)
            attributes.append(strength)
            attributes.append(merit)
            print('Your attributes are: Health = ' + str(attributes[0]) + ' Strength = ' + str(attributes[1])+'\n')

        lastScenario = currentScenario
        currentScenario = dialogue[currentScenario][2][int(Input) - 1]
        health -=1
        scenarioCount+=1
        if scenarioCount % characterFood == 0:
            health+=2
            print('Your tomb recieved an offering, your health has increased by 2')

    # try:
    #     printResponse()
    # except(IndexError):
    #     print("Please Choose a number 1-3")
    #     Input = input()
    #
    # except(IndexError):
    #     print("Please Choose a number 1-3")
    #     printResponse()
gameplay(currentScenario)

print('This concludes the Demo Verion of Organ Trail™ for more please stay tuned!!!')
