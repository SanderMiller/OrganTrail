import pygame, sys
from pygame import font

scenarios = ['hi', 'bye']

pygame.init() 

#Create Window
windowSize = (800,600)
screen = pygame.display.set_mode(windowSize) 
pygame.display.set_caption('Organ Trail')


class Display():

    def __init__(initScenarioText, initOptionUp, initOptionRight, initOptionLeft, initOptionDown):
        self.initScenarioText = initScenarioText 
        self.ScenarioText = self.initScenarioText

        self.initOptionUp  = initOptionUp
        self.initOptionLeft  = initOptionLeft
        self.initOptionRight  = initOptionRight
        self.initOptionDown  = initOptionDown


        self.OptionUp  = self.initOptionUp
        self.OptionLeft  = self.initOptionLeft
        self.OptionRight  = self.initOptionRight
        self.OptionDown  = self.initOptionDown

    def search_font(name):
        found_font = font.match_font(name)
        return found_font

    def font_renderer(font,size): 
        font_object = pygame.font.Font(font, size)
        return font_object

    def createScenario(scenarioArray, scenarioIndex):
        font = search_font('ubuntu')
        scenarioText = font_renderer(font, 10)
        message = scenarioArray[scenarioIndex]
        font_object = pygame.font.Font(used_font, size)
        return Scenario

    def message_display(used_font, size, color,xy,message): 
        font_object = pygame.font.Font(used_font, size)
        rendered_text = font_object.render(message, True, (color))
        screen.blit(rendered_text,(xy))
        pygame.display.update()
    #rendering the message
    ubuntu = search_font('ubuntu')
    normal_message = [search_font('ubuntu'),30,(255,255,255),(5,400)]
    #message_display(*normal_message ,"That is a super short line!")
    def main():
        while True:
            message_display(*normal_message ,"Not much to see here.")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
main()