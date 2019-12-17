import random

currentScenario = 'Scenario1'

dialogue = {
    'Scenario1': ['Choose your character', 
                 ['Pharaoh', 'Priest', 'Farmer'], ['Scenario2', 'Scenario2', 'Scenario2'], [[15,50,0,3], [10,60,1,5], [15,70,0,7]]],
    'Scenario2': ['We must make haste to the hall of two truths, so that your soul can be weighed against a feather and we can learn whether you may pass into the afterlife. Any questions? \n “W- w-” \n “Good! Let’s get on with it then.” Anubis rushes out of the room with no further words, what will you do?.', 
                 ['follow him', 'ignore him, and stay where you are'], ['Scenario3', 'ScenarioEnd'], [[-1,0,0,3], [-1,0,0,5], [-1,0,0,7]]],
    'Scenario3': ['You follow him into a crowd, but soon you lose sight of him... you look around, there is a traveler standing by themselves at the wall, what would you like to do?',
                 ['Approach them and ask for directions', 'Fight them for food (or bragging rights)', 'make your way on your own'], ['Scenario4', 'ScenarioFight', 'Scenario6'], [[-1,0,0,3], [-1,0,0,5], [-1,0,0,7]]],
    'Scenario4': ['You approach the stranger. She turns around and you notice her appearance. She had the body of a leopard, but her head was that of a hippopotamus. She held a "Khopesh", a massive sword and sickle hybrid. When she spoke, her voice was powerful and intimidating."Hello weary traveler, I am Henet Requ, guardian of the portal of fire. You look lost, would you like my assistance?"',
                 ['Accept her offer', 'Make your way on your own', 'challenge her to a dance off'], ['Scenario5', 'Scenario6', 'ScenarioEnd'], [[-1,0,0,3], [-1,0,0,5], [-1,0,0,7]]],
    'Scenario5': ['"Hello Henet, I was following Anubis but seem to have lost my way, do you know the way to the Hall of Maat?" Her brow furrowed. I do know the way, although it is very treacherous. You must follow me.', 
                 ['Follow her', 'come on seriously, follow her', 'why are you not trusting Henet'], ['ScenarioEnd', 'ScenarioEnd', 'ScenarioEnd'], [[-1,0,0,3], [-1,0,0,5], [-1,0,0,7]]],
    'Scenario6': ['You try to make it through crowd on your own. Eventually after fighting the current of souls you see a gate . There appear to be two options, a water and land route. What do you do?', 
                 ['Approach the land route gate.','Approach the water route'], ['ScenarioEnd', 'ScenarioEnd'], [[0,0,0,3], [0,0,0,5], [0,0,0,7]]], 
    #'Scenario7': ['',[],[]]
    #'Scenario8': ['',[],[]]
    #'Scenario9': ['',[],[]]
    #'Scenario10': ['',[],[]]
    #'Scenario11': ['',[],[]]
    'ScenarioEnd': ['Alas, you perish, never to set eyes on the Hall of Maat. Thanks for playing!', ['you lose', 'you lose (even more horribly)'], ['Scenario1', 'Scenario1']]
}




def fight(strength, health, currentScenario, lastScenario):
    outcome = random.randint(1,100)
    if outcome <= strength:
        health += 3
        currentScenario = lastScenario
        print('Congrats, you defeated a demon!\n')
        print('Health' + str(health))
    else:
        currentScenario = 'ScenarioEnd'
        print('Sorry, you lost.\n')
    return health, currentScenario



def gameplay(currentScenario):
    print('Your eyes open, or at least so it seems, but they’re met with a disconcerting sight. A coffin lies beneath you, with inscriptions that match your name. You notice a strange figure in the corner of the room. As they approach, you recognize it to be Anubis, the jackal headed god of the dead, son of Osiris. Anubis asks,“What is your name?” ')
    name = input()
    print("Hello " + name+", you must be very confused. I’m afraid to say that you’re dead, due to a terrible accident. Don’t panic, death gets a bad reputation but it’s alright. We should get going, but real quick, what was your occupation?")
    scenarioCount = 0
    attributes = {'Health': 0,
                  'Strength': 0,
                  'Merit': 0,
                  'TurnPerFood': 0 }
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

       
        attributes['Health'] += dialogue[currentScenario][3][int(Input) - 1][0]
        attributes['Strength'] += dialogue[currentScenario][3][int(Input) - 1][1]
        attributes['Merit'] += dialogue[currentScenario][3][int(Input) - 1][2]
        attributes['TurnPerFood'] += dialogue[currentScenario][3][int(Input) - 1][3]
        health = attributes['Health']
        TurnPerFood = attributes['TurnPerFood']
           
          
        #print('Your attributes are: Health = ' + str(attributes[0]-1) + ' Strength = ' + str(attributes[1])+'\n')
        

        lastScenario = currentScenario
        currentScenario = dialogue[currentScenario][2][int(Input) - 1]
        health -=1
        scenarioCount+=1
        if scenarioCount % TurnPerFood == 0:
            health+=2
            print('Your tomb recieved an offering, your health has increased by 2')
        print('Health:' + str(health))

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
