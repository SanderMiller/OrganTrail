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
                 ['Pharaoh', 'Priest', 'Farmer'], ['Scenario2', 'Scenario2', 'Scenario2'], [[10,50,0,3], [8,60,1,5], [6,70,0,5]], ['PyramidBackground.jpg', 'Anubis.png'] ],
    'Scenario2': ['We must make haste to the Hall of Two Truths, so that your soul can be weighed against \
                  \na feather and we can learn whether you may pass into the afterlife. Any questions? \
                  \n“W- w-” \
                  \n“Good! Let’s get on with it then.” Anubis rushes out of the room with no further words, \
                  \nwhat will you do?.',
                 ['Follow him', 'Ignore him, and stay where you are'], ['Scenario3', 'ScenarioEnd'], [[-1,0,0], [-1,0,0], [-1,0,0]], ['PyramidBackground.jpg', 'Anubis.png']],
    'Scenario3': ['You follow him into a crowd, but soon you lose sight of him... you look around, \
                  \nthere is a traveler standing by themselves at the wall, what would you like to do?',
                 ['Approach them and ask for directions', 'Fight them for food (or bragging rights)', 'Make your way on your own'], ['Scenario5', 'ScenarioFight', 'Scenario6', 'Scenario6'], [[-1,0,0], [-1,0,0], [-1,0,0]],['Cavern.jpg']],
    'Scenario4': ['You step through the portal and enter a room with fire blazing all around you. \
                  \nInstantly smoke fills your eyes and heat presses in from all directions.\
                  \n A figure approaches you, and although your vision is hazy, you pick out some details. \
                  \nHer body was an amalgam of different animals, with her legs and hands those of a lion,\
                  \ntail of a crocodile, but her head was that of a hippopotamus. She held a "Khopesh", \
                  \na massive sword and sickle hybrid. When she spoke, her voice was powerful and intimidating. \
                  \n"Hello weary traveler, I am the guardian of the portal of fire. You dare attempt to cross \
                  \nmy domain unimpeded?" There is no hope of passing by. I do not judge those who come to me \
                  \non their goodness or badness, only on their quick wit. Leave before I am forced to overpower\
                  \nyou" You seem to remember something about the guardian of the portal of fire from your\
                  \nlifetime. Something specifically about speaking their name...', ['Say "Dionysus"', 'Say "Isis"', 'Say "Henet Requ"'],['ScenarioEnd', 'ScenarioEnd', 'Scenario9'],[[-1,0,0], [-1,0,0], [-1,0,0]],['fire.jpg','Henet.jpg']],
    'Scenario5': ['As you approach the figure you recognize her as Taweret, the patron of childbirth\
                  \n"Hello Taweret, I was following Anubis but seem to have lost my way, do you know the way \
                  \nto the Hall of Maat?" Her brow furrowed. "I do know the way, although it is very treacherous. \
                  \nYou must follow me."',
                 ['Follow her', 'Suspecting a trap, run away'], ['Scenario7', 'Scenario6'], [[-1,10,0], [-1,0,0], [-1,0,0]],['Cavern.jpg', 'taweret.jpg']],
    'Scenario6': ['You try to make it through crowd on your own. Eventually after fighting the current of \
                  \nsouls you see a gate. There appear to be two options, a water and fire route. \
                  \nWhat do you do?',
                 ['Approach the fire route.','Approach the water route'], ['Scenario4', 'Scenario17'], [[-1,0,0], [-1,0,0], [-1,0,0]],['Cavern.jpg']],
    'Scenario7': ['Congrats, through apotropaism you have befriended Taweret, the goddess of childbirth \
                  \nand fertility. By converting this god to your side, your strength has increased by 10! \
                  \n\nYou follow Taweret, who seems to easily navigate through the crowd of souls. Not wanting \
                  \nto lose your guide again you hastily follow. Eventually she leads you to a set of gates,\
                  \none leads to a vast ocean, while the other leads to stretch of land, full of fire. \
                  \nWhich gate will you approach?',['Water Gate', 'Fire Gate'],['Scenario8','Scenario8'],[[-1,0,0], [-1,0,0], [-1,0,0]],['Cavern.jpg']],
    'Scenario8': ['Wait, before you go, remember that your journey to the Hall of Maat will be a dangerous one. \
                  \nNever trust anyone, and keep in mind that even if you make it to the Hall alive, your heart \
                  \nwill be weighed, and you must must be seen as worthy to enter Sekhet-A’Aru, the field of reeds', ['Thank Taweret and Approach the Water Gate', 'Thank Taweret and Approach the Fire Gate'],['Scenario17','Scenario4'],[[-1,0,0], [-1,0,0], [-1,0,0]],['Cavern.jpg', 'taweret.jpg']],
    'Scenario9': ['After you utter her name she weakens and huddles to the ground, brandishing her Khopesh \
                  \nfor you to take. "You are a wise one, traveler." She says as she allows you to pass. \
                  \nAs you wield the khopesh you feel strength rush through you.'
                  , ['Continue On', 'Continue On'],['Scenario10', 'Scenario10'],[[-1,10,0], [-1,10,0], [-1,10,0]],['fire.jpg','Henet.jpg']],
    'Scenario10': ['As you walk through the fiery cavern, you stumble upon a loaf of bread!- \
                  \n-Well, toast, as it has been burned pretty badly. The bread is on a ledge, but out of the\
                  \ncorner of your eye you spot a Medjed, a ghost-like demon, scrabbling \
                  \nagainst the rock, attempting and failing to reach the bread. What do you do?'
                  , ['Hand it the bread','Eat the bread to restore your health'],['Scenario11','Scenario11'],[[-1,0,1],[5,0,-1],[-1,0,0]],['fire.jpg', 'Medjed.jpg']],
    'Scenario11': ['After passing by the MedJed you follow the path for a while. You eventually come to a door. \
                  \nYou can hear some scrabbles and squeals and other curious noises coming from the other side. \
                  \nWhat do you do?'
                  , ['Listen at the keyhole', 'Run in and fight no matter what','Try and find a way around'],['Scenario12','ScenarioFight','Scenario14','Scenario13'],[[-1,0,-1],[-1,0,1],[-1,0,1]],['fire.jpg']],
    'Scenario12': ['You approach the keyhole, and put your eye down to it, listening the whole\
                  \ntime to try and make out any intelligible noises. As you peer through the\
                  \nsmall hole, the door opens from the other side and you are surrounded by sundisks.'
                  , ['Fight them off','Yell "Sundisks, servants of Ra, cease!"','Dance off (come on this time it might work)'],['ScenarioFight','ScenarioEnd','ScenarioEnd','Scenario13'],[[-1,0,0],[-1,0,0],[-1,0,0]],['fire.jpg', 'sundisk.jpg']],
    'Scenario13': ['The dust clears, and you stand over several piles of dazed sundisks. \
                  \n One of them appears to have dropped a bag of grain. What do you do?'
                  ,['Take the bag of grain','Ignore the grain and continue on your way'],['Scenario14','Scenario14',],[[3,0,-1],[-1,0,1],[-1,0,0]],['fire.jpg','sundisk.jpg']],
    'Scenario14': ['You stumble out into a new kind of light, it appears that you made it out of the cave.\
                  \n You approach a huge set of gates, guarded by a massive demon known as "Apep"'
                  ,['Fight it','Fight it','Fight it'],['ScenarioFight','ScenarioFight','ScenarioFight','Scenario16'],[[-1,0,0],[-1,0,0],[-1,0,0]],['HallOfOsiris.jpg','Apep.jpg']],
    'Scenario15': ['Apep appears unimpressed.'
                  ,['Fight it Again','Fight it Again','Fight it Again'],['ScenarioFight','ScenarioFight','ScenarioFight','Scenario16'],[[-1,0,0],[-1,0,0],[-1,0,0]],['HallOfOsiris.jpg','Apep.jpg']],
    'Scenario16': ['Apep is bewildered at your strength. One more time might do it!'
                  ,['Fight it Again','Fight it Again','Fight it Again'],['ScenarioFight','ScenarioFight','ScenarioFight','Scenario30'],[[-1,0,0],[-1,0,0],[-1,0,0]],['HallOfOsiris.jpg','Apep.jpg']],
    'Scenario17': ['Having made up your mind that water looked a lot less terrifying than water you \
                   \nmake your way to the water gate alone. You have prepared your whole life for this \
                   \njourney, but are this preparation only makes you more uneasy, you know what’s ahead. \
                   \nAs you walk through the gate it shuts behind you. No going back now. You are standing \
                   \non a dock, overlooking a seemingly endless ocean. Looking back you see a creature \
                   \nwith a human head, a feline body, and a forked tail. He is looking at you, so you \
                   \ndecide to approach the creature.',['Continue', 'Continue'],['Scenario18','Scenario18'],[[-1,0,0],[-1,0,0]],['water.jpg','GreatFace.jpg'] ],
    'Scenario18': ['“Looking for Sheket A’aru,” the creature asks. You nod your head. “Ah yes, just \
                   \nlike everyone else. Well Ra’s barque, the Meseket, won’t be here until dusk. \
                   \nYou may as well wait around here.', ['Ask who are you?', 'Decide to swim instead', 'Wait Patiently'], ['Scenario19', 'ScenarioEnd', 'Scenario20'],[[-1,0,0],[-1,0,0],[-1,0,0]],['water.jpg','GreatFace.jpg']],
    'Scenario19': ['I am known as “Great-Face, who opposes the aggressors”, the keeper of the waterway. \
                   \nI have been here a long time and seen a lot like you attempt to make it to Sheket A’aru, \
                   \nI don’t know if you have what it takes.', ['Shout "You\'re wrong!" and jump into the water', 'Challenge him to a battle', 'Wait patiently'], ['ScenarioEnd', 'ScenarioFight', 'Scenario20', 'Scenario20'], [[-1,0,0],[-1,0,0],[-1,0,0]],['water.jpg','GreatFace.jpg']],
    'Scenario20': ['After hours of waiting in the hot sun, you see a piece of bread, left by a passerby. \
                   \nYou wonder if anyone will notice if you took it. It would regenerate some health \
                   \nfor you, but you also think back to the Negative Confessions.', ['Take the bread', 'Leave the bread'], ['Scenario21', 'Scenario22'], [[-1,0,-1],[-1,0,1]], ['water.jpg']],
    'Scenario21': ['You look around, before quickly snatching the bread. You again scan your surroundings, \
                   \nbut nobody seems to have seen you, well done!', ['Continue', 'Continue'], ['Scenario23', 'Scenario23'],[[-1,0,0],[-1,0,0]], ['water.jpg']],
    'Scenario22': ['You leave the bread, and a few minutes later the soul of a young boy comes and \
                   \nretrieves the bread. Phew, you almost blew your chances of ever getting into Sheket A’aru.',['Continue', 'Continue'], ['Scenario23', 'Scenario23'],[[-1,0,0],[-1,0,0]], ['water.jpg']],
    'Scenario23': ['As evening sets in you see Ra’s ship enter the port and dock. You join the crowd \
                   \ndashing onto the Sheket, with hopes of reaching the Hall of Two Truth, and the field \
                   \nof reeds. You find a seat on the top deck, towards the bow. You look up at the square \
                   \nsails, full with wind, carrying the boat across smoothly across the sea. You wonder \
                   \nif this is how it would feel to fly.You begin to drift off to sleep when you \
                   \noverhear something that catches your attention. “She’ll eat your heart, stranding \
                   \nyou in Duat forever.” What will you do?', ['Keep Listening', 'Forget about it and go to sleep'], ['Scenario24', 'Scenario25'],[[-1,0,-1],[-1,0,1]], ['water.jpg']],
    'Scenario24': ['As you keep listening you hear that they are talking about the demon Ammit. \
                   \nThe demon with the head of a crocodile, upper torso of a leopard, and lower torso \
                   \nof a hippopotamus stays in the Hall of Two Truths, ready to devour any heart that weighs \
                   \nmore than the Maat’s feather. While you knew all of this, the thought of Ammit still \
                   \nmakes you uneasy.', ['Continue', 'Continue'], ['Scenario25', 'Scenario25'], [[-1,0,0],[-1,0,0]], ['water.jpg']],
    'Scenario25': ['You fall into a restless sleep, when you are woke by large waves slapping the sides \
                   \nof the boat. You see that the vast sea has been replaced by a lake of fire. Looking \
                   \nover the edge into the fiery mess below you see a number of fire demons, serpents and \
                   \na large baboon you recognize to be Babi. You see the blood thirst in his eyes and know \
                   \nthat if you don’t do anything you will surely perish.', ['Fight the demon', 'Hide Below Deck'], ['ScenarioFight', 'Scenario27', 'Scenario26'], [[-1,0,0],[-1,0,0]], ['fire.jpg','MonkeyThing.jpg']],
    'Scenario26': ['You lead the charge against Babi and are pleased to see that the rest of the souls on \
                   \nboard follow your lead. The mass of souls eventually is able to fight off the onslaught \
                   \nof demons, and the ship makes it through the lake of fire. You are relieved to see the \
                   \nshades of blue beneath the boat again, but without the light of the fire lake, you fall \
                   \ninto darkness. You feel gross, and wonder if it would be a good idea to dip your \
                   \nfeet in the water just to clean them.', ['Clean your feet', 'Remain with dirty feet'], ['Scenario28', 'Scenario28'], [[-1, 0, -1], [-1,0,1]], ['water.jpg','MonkeyThing.jpg']],
    'Scenario27': ['You hide under deck, but it seems the rest of the souls aboard had the same idea. \
                   \nWith Ra nowhere insight, there is nothing to defend you. The demons are easily able to tear \
                   \napart the boat, and you feel the heat as you fall into the lake of fire.', ['Continue','Continue'], ['ScenarioEnd', 'ScenarioEnd'], [[-1, 0, 0], [-1,0,0]], ['fire.jpg','MonkeyThing.jpg']],
    'Scenario28': ['Finally after a long night you spot land off in the distance. It is almost dawn. \
                   \nYou grow excited, you have made it through some of the most treacherous parts of the journey. \
                   \nAs soon as you land you rush off the boat, eager to get to the Hall of Two Truths as soon \
                   \nas possible, when you hear a voice behind you. "Not so fast!" you look back to see the God \
                   \nof the sun, Ra behind you. "You have made it through thus far, but remember you still have yet \
                   \nto have your heart weighed, take this." With that he hands you an amulet, in the shape of a scarab. \
                   \n"It is inscribed with a spell to ensure your heart will not speak out against you to Osiris."', ["Throw the Amulet at Ra", 'Take the amulet', 'Throw the amulet into the water'], ['ScenarioEnd', 'Scenario29', 'Scenario29'], [[-1,0,0],[-1,0,2],[-1,0,-20]],['water.jpg']],
    'Scenario29': ['You begin your trek up the steep mountain, before coming to a cave. You follow the crowd, \
                   \nmarching through the cave, on your way to The Hall of Two Truths.', ['Continue', 'Continue'], ['Scenario14', 'Scenario14'], [[-1,0,0],[-1,0,0]], ['Cavern.jpg']],
    'Scenario30': ['You enter into the huge doors of what is clearly the Hall of Two Truths. \
                  \nIn a throne sits Anubis, and at his feet sits Ammit the devourer. A single pair of\
                  \nscales lies ready to judge the heart of those brave enough to attempt. You see Anubis\
                  \npacing on one side of the hall, and he nods to you. Osiris beckons you towards the scales\
                  \nand you stand ready to act. What will you do?'
                  ,['Weigh your heart','Go out fighting'],['ScenarioWeigh','ScenarioEnd'],[[0,0,0],[0,0,0],[0,0,0]],['HallOfOsiris.jpg','Osiris.jpg']],
    'FinalScenario': ['Congratulations! You made it. You step out of the hall and onto a small \
                  \n boat, piloted by Hraf-Hef, the ferryman. He smiles at you, and offers you his congratulations.'
                  ,['Smile back','ignore him','say thank you'],['ScenarioWin','ScenarioEnd','ScenarioWin'],[[-1,0,0],[-1,0,0],[-1,0,0]],['FieldOfReeds.jpg']],

    'ScenarioWin': ['', ['Play Again', 'Play Again'], ['Scenario1', 'Scenario1'],[[0,0,0], [0,0,0], [0,0,0]],['SoulPassed.jpg']],
    'ScenarioEnd': ['', ['Play Again', 'Play Again'], ['Scenario1', 'Scenario1'],[[0,0,0], [0,0,0], [0,0,0]],['Youlost.jpg']]
    }

file_path1 = 'C:/Users/Casey May/OrganTrail/'

def resize(file_name, xDimension, yDimension):
    global file_path1
    file_path = file_path1 + file_name
    img = cv2.imread(file_path)
    imgResized = cv2.resize(img, (xDimension, yDimension), cv2.INTER_CUBIC) #INTER_AREA
    cv2.imwrite(file_path, imgResized)

# resize('HallOfOsiris.jpg',1440,1024)
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
        time.sleep(2)
        health += 3
        currentScenario = dialogue[lastScenario][2][-1]
        print('Congrats, you defeated a demon!\n')
        print('Health' + str(health))
    else:
        currentScenario = 'ScenarioEnd'
        print('Sorry, you lost.\n')
    return health, currentScenario

def merit_check(merit, currentScenario):
    if merit >= 0:
        currentScenario = 'FinalScenario'
    else:
        currentScenario = 'ScenarioEnd'
    return currentScenario


def multiline_render(text, x, y, font):
    lines = text.splitlines()
    for i,l in enumerate(lines):
        text = font.render(l, 0, black)
        if text.get_size()[0] > 1115:
            temp_surface = pygame.Surface((1115, 26))
        else:
            temp_surface = pygame.Surface(text.get_size())
        if text.get_size() != (1, 25):
            temp_surface.fill((255,255,255))
            temp_surface.blit(text, (0,0))
            screen.blit(temp_surface, (x, y  + font.get_linesize()*i))
        screen.blit(text, (x, y + font.get_linesize()*i))

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
    if len(option1) > 10:
        multiline_render(option1, 435 - len(option1)*10, 860, font)
    else:
        multiline_render(option1, 435 - len(option1), 860, font)
    multiline_render(option2, 900, 860, font)

    numOptions = len(dialogue[currentScenario][1])
    if numOptions == 3:
        option3 = dialogue[currentScenario][1][2]
        screen.blit(upKey, [670, 700])
        if len(option3) > 10:
            multiline_render(option3, 680-len(option3)*5, 660, font)
        else:
            multiline_render(option3, 680-len(option3)*5, 660, font)


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
            if currentScenario == 'ScenarioWeigh':
                currentScenario = merit_check(merit, currentScenario)


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
