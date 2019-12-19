import pygame
import cv2
import os
import random
from time import sleep
import time

dialogue = {
    'Scenario1': ['You open your eyes, or at least so it seems, but they\'re met with a disconcerting sight. \
                  \nA coffin lies beneath you, with inscriptions that match your name. You notice a strange \
                  \nfigure in the corner of the room. As they approach, you recognize it to be Anubis, the \
                  \njackal headed god of the dead, son of Osiris. Hello, you must be very confused. \
                  \nI’m afraid to say that you’re dead, due to a terrible accident. Don’t panic, death gets a bad \
                  \nreputation but it’s alright. We should get going, but real quick, what was your occupation? \
                  \n\n\nChoose your character',
                 ['Pharaoh', 'Priest', 'Farmer'], ['Scenario2', 'Scenario2', 'Scenario2'], [[15,50,0,3], [10,60,1,5], [15,70,0,7]], ['PyramidBackground.jpg', 'Anubis.png'] ],
    'Scenario2': ['We must make haste to the hall of two truths, so that your soul can be weighed against \
                  \na feather and we can learn whether you may pass into the afterlife. Any questions? \
                  \n“W- w-” \
                  \n“Good! Let’s get on with it then.” Anubis rushes out of the room with no further words, \
                  \nwhat will you do?.',
                 ['Follow him', 'Ignore him, and stay where you are'], ['Scenario3', 'ScenarioEnd'], [[-1,0,0], [-1,0,0], [-1,0,0]], ['PyramidBackground.jpg', 'Anubis.png']],
    'Scenario3': ['You follow him into a crowd, but soon you lose sight of him... you look around, \
                  \nthere is a traveler standing by themselves at the wall, what would you like to do?',
                 ['Approach them and ask for directions', 'Fight them for food (or bragging rights)', 'Make your way on your own'], ['Scenario4', 'ScenarioFight', 'Scenario6', 'Scenario6'], [[-1,0,0], [-1,0,0], [-1,0,0]],['Cavern.jpg']],
    'Scenario4': ['You approach the stranger. She turns around and you notice her appearance. \
                  \nShe had the body of a leopard, but her head was that of a hippopotamus. She held a "Khopesh", \
                  \na massive sword and sickle hybrid. When she spoke, her voice was powerful and intimidating. \
                  \n"Hello weary traveler, I am Henet Requ, guardian of the portal of fire. You look lost, \
                  \nwould you like my assistance?"',
                 ['Accept her offer', 'Make your way on your own', 'Challenge her to a dance off'], ['Scenario5', 'Scenario6', 'ScenarioEnd'], [[-1,0,0], [-1,0,0], [-1,0,0]],['Cavern.jpg', 'Henet.jpg']],
    'Scenario5': ['"Hello Taweret, I was following Anubis but seem to have lost my way, do you know the way \
                  \nto the Hall of Maat?" Her brow furrowed. "I do know the way, although it is very treacherous. \
                  \nYou must follow me."',
                 ['Follow her', 'Suspecting a trap, runaway'], ['Scenario7', 'Scenario6'], [[-1,10,0], [-1,0,0], [-1,0,0]],['Cavern.jpg', 'Henet.jpg']],
    'Scenario6': ['You try to make it through crowd on your own. Eventually after fighting the current of \
                  \nsouls you see a gate. There appear to be two options, a water and land route. \
                  \nWhat do you do?',
                 ['Approach the land route gate.','Approach the water route'], ['ScenarioEnd', 'ScenarioEnd'], [[0,0,0], [0,0,0], [0,0,0]],['PyramidBackground.jpg']],
    'Scenario7': ['Congrats, through apotropaism you have befriended Taweret, the goddess of childbirth \
                  \nand fertility. By converting this god to your side, your strength has increased by 10! \
                  \n\nYou follow Taweret, who seems to easily navigate through the crowd of souls. Not wanting \
                  \nto lose your guide again you hastily follow. Eventually she leads you to a set of gates,\
                  \none leads to a vast ocean, while the other leads to stretch of land, full of fire.',['eat', 'eat'],['ScenarioEnd','ScenarioEnd'],[[-1,0,0], [-1,0,0], [-1,0,0]],['PyramidBackground.jpg']],
    #'Scenario8': ['',[],[]]
    #'Scenario9': ['',[],[]]
    #'Scenario10': ['',[],[]]
    #'Scenario11': ['',[],[]]
    'ScenarioEnd': ['k', ['Play Again', 'Play Again'], ['Scenario1', 'Scenario1'],[[0,0,0], [0,0,0], [0,0,0]],['Youlost.jpg']]
    }

file_path1 = '/home/cmay/Documents/OrganTrail/'

def resize(file_name, xDimension, yDimension):
    global file_path1
    file_path = file_path1 + file_name
    img = cv2.imread(file_path)
    imgResized = cv2.resize(img, (xDimension, yDimension), cv2.INTER_CUBIC) #INTER_AREA
    cv2.imwrite(file_path, imgResized)

# resize('FightVictory.jpg',1440,1024)
#resize('ArrowKeyRight.png',100,100)
#resize('ArrowKeyUp.png',100,100)



def fight(strength, health, currentScenario, lastScenario):
    global dialogue
    global screen
    outcome = random.randint(1,100)
    if outcome <= strength:
        FightVictory = pygame.image.load('FightVictory.jpg')
        screen.blit(FightVictory, [0, 0])
        pygame.display.flip()
        time.sleep(3)
        health += 3
        currentScenario = dialogue[lastScenario][2][3]
        print('Congrats, you defeated a demon!\n')
        print('Health' + str(health))
    else:
        currentScenario = 'ScenarioEnd'
        print('Sorry, you lost.\n')
    return health, currentScenario


def multiline_render(text, x, y, font):
    lines = text.splitlines()
    for i,l in enumerate(lines):
        screen.blit(font.render(l, 0, white), (x, y + font.get_linesize()*i))

def visualize(currentScenario, health, strength, additionalString):
    global dialogue
    avatar_status = True
    pygame.display.set_caption('Organ Trail')
    background_image = pygame.image.load(dialogue[currentScenario][4][0])

    try:
        avatar_image = pygame.image.load(dialogue[currentScenario][4][1])
    except IndexError:
        avatar_status = False

    leftKey = pygame.image.load('ArrowKeyLeft.png')
    rightKey = pygame.image.load('ArrowKeyRight.png')
    upKey = pygame.image.load('ArrowKeyUp.png')
    font = pygame.font.Font('freesansbold.ttf', 24)
    text = dialogue[currentScenario][0]
    option1 = dialogue[currentScenario][1][0]
    option2 = dialogue[currentScenario][1][1]
    healthText = 'Health: ' + str(health)
    strengthText = 'Strength: ' + str(strength)
    # textRect = text.get_rect()
    # textRect.center = (window_width // 2, window_height // 3)
    screen.blit(background_image, [0,0])
    multiline_render(text, 300, 150, font)
    if avatar_status:
        screen.blit(avatar_image, [100, 150])
    screen.blit(leftKey, [560, 820])
    screen.blit(rightKey, [780, 820])
    screen.blit(font.render(healthText, 0, white), [1200, 50])
    screen.blit(font.render(strengthText, 0, white), [1200, 100])
    multiline_render(additionalString, 300, 50, font)
    multiline_render(option1, 435, 860, font)
    multiline_render(option2, 900, 860, font)

    numOptions = len(dialogue[currentScenario][1])
    if numOptions == 3:
        option3 = dialogue[currentScenario][1][2]
        screen.blit(upKey, [670, 700])
        multiline_render(option3, 680, 660, font)


pygame.init()

window_width = 1440
window_height = 1024
clock_tick_rate=20

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)

currentScenario = 'Scenario1'
lastScenario = 'Scenario1'

scenarioCount = 0
attributes = {'Health': 0,
              'Strength': 0,
              'Merit': 0,
              'TurnPerFood': 0 }

size = (window_width, window_height)
screen = pygame.display.set_mode(size)
numOptions = len(dialogue[currentScenario][1])
#print('Your eyes open, or at least so it seems, but they\'re met with a disconcerting sight. A coffin lies beneath you, with inscriptions that match your name. You notice a strange figure in the corner of the room. As they approach, you recognize it to be Anubis, the jackal headed god of the dead, son of Osiris. Anubis asks,"What is your name?" ')
#name = input()

#print("Hello " + name+", you must be very confused. I’m afraid to say that you’re dead, due to a terrible accident. Don’t panic, death gets a bad reputation but it’s alright. We should get going, but real quick, what was your occupation?")
visualize(currentScenario, 0, 0, '')
pygame.display.flip()



dead=False


clock = pygame.time.Clock()
clock.tick(clock_tick_rate)

while dead == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

        numOptions = len(dialogue[currentScenario][1])

        if (event.type == pygame.KEYDOWN and numOptions == 3 and (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP)) or (event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT)):
            print(numOptions)
            if event.key == pygame.K_LEFT:
                Input = 1
            if event.key == pygame.K_RIGHT:
                Input = 2
            if event.key == pygame.K_UP and numOptions == 3:
                Input = 3



            if currentScenario == 'Scenario1':
                health = dialogue[currentScenario][3][int(Input) - 1][0]
                print(health)
                strength = dialogue[currentScenario][3][int(Input) - 1][1]
                merit = dialogue[currentScenario][3][int(Input) - 1][2]
                TurnPerFood = dialogue[currentScenario][3][int(Input) - 1][3]

            else:
                health += dialogue[currentScenario][3][int(Input) - 1][0]
                strength += dialogue[currentScenario][3][int(Input) - 1][1]
                merit += dialogue[currentScenario][3][int(Input) - 1][2]

            numOptions = len(dialogue[currentScenario][1])
            lastScenario = currentScenario
            currentScenario = dialogue[currentScenario][2][int(Input) - 1]
            if currentScenario == 'ScenarioFight':
                [health, currentScenario] = fight(strength, health, currentScenario, lastScenario)


            scenarioCount+=1
            if scenarioCount % TurnPerFood == 0 and currentScenario != 'ScenarioEnd':
                health+=2
                additionalString = 'Your tomb recieved an offering, your health has increased by 2!'
            else:
                additionalString = ''
            #print('Health:' + str(health))
            visualize(currentScenario, health, strength, additionalString)
            pygame.display.flip()

            clock.tick(clock_tick_rate)
