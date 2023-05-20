import pygame
from card import Spell
import os
import random

class Deck:
    def __init__(self,test_case):
        self.folderPath = "./spells"
        self.images = {}
        self.deck = []
        self.test_case = test_case
        self.count = 30

        for file in os.listdir(self.folderPath):
            if file.endswith(".png"):
                image_path = os.path.join(self.folderPath, file)
                print(image_path)
                image_name = os.path.splitext(file)[0]
                self.images[image_name] = pygame.image.load(image_path)

    def get_image(self,image_name):
        return self.images.get(image_name)

    def init_deck(self): 
        match self.test_case:
            case 1:
                for i in range(2):
                    self.deck.append(Spell(self.get_image("manaDown"), "manaDown")) 
                for i in range(2):
                    self.deck.append(Spell(self.get_image("quickBookmark"),"quickBookmark"))
                for i in range(1):
                    self.deck.append(Spell(self.get_image("speedWand"),"speedWand"))
                for i in range(1):
                    self.deck.append(Spell(self.get_image("slowWand"),"slowWand"))
                for i in range(6):
                    self.deck.append(Spell(self.get_image("waterCube"),"waterCube")) 
                for i in range(5):
                    self.deck.append(Spell(self.get_image("lightningCube"),"lightningCube"))
                for i in range(5):
                    self.deck.append(Spell(self.get_image("threeCubes"),"threeCubes"))
                for i in range(5):
                    self.deck.append(Spell(self.get_image("fireball"),"fireball"))
                for i in range(1):
                    self.deck.append(Spell(self.get_image("bigLow"),"bigLow"))
                for i in range(1):
                    self.deck.append(Spell(self.get_image("overhead"),"overhead"))
                for i in range(1):
                    self.deck.append(Spell(self.get_image("dP"),"dP"))
            case 2:
                for i in range(2):
                    self.deck.append(Spell(self.get_image("manaRefill"),"manaRefill")) 
                for i in range(2):
                    self.deck.append(Spell(self.get_image("quickSwap"),"quickSwap"))
                for i in range(1):
                    self.deck.append(Spell(self.get_image("gravUp"),"gravUp"))
                for i in range(1):
                    self.deck.append(Spell(self.get_image("gravDown"),"gravDown"))
                for i in range(3):
                    self.deck.append(Spell(self.get_image("waterCube"),"waterCube")) 
                for i in range(3):
                    self.deck.append(Spell(self.get_image("lightningCube"),"lightningCube"))
                for i in range(3):
                    self.deck.append(Spell(self.get_image("threeCubes"),"threeCubes"))
                for i in range(3):
                    self.deck.append(Spell(self.get_image("fireball"),"fireball"))
                for i in range(2):
                    self.deck.append(Spell(self.get_image("lightCube"),"lightCube"))
                for i in range(3):
                    self.deck.append(Spell(self.get_image("bigLow"),"bigLow"))
                for i in range(3):
                    self.deck.append(Spell(self.get_image("overhead"),"overhead"))
                for i in range(2):
                    self.deck.append(Spell(self.get_image("waveCube"),"waveCube"))
                for i in range(1):
                    self.deck.append(Spell(self.get_image("reflector"),"reflector"))
                for i in range(1):
                    self.deck.append(Spell(self.get_image("randomCard"),"randomCard"))
            case 3:
                for i in range(2):
                    self.deck.append(Spell(self.get_image("manaPositive"),"manaPositive"))
                for i in range(1):
                    self.deck.append(Spell(self.get_image("swap"),"swap"))
                for i in range(1):
                    self.deck.append(Spell(self.get_image("cubeSpeedDown"),"cubeSpeedDown"))
                for i in range(1):
                    self.deck.append(Spell(self.get_image("cubeSpeedUp"),"cubeSpeedUp"))
                for i in range(2):
                    self.deck.append(Spell(self.get_image("waterCube"),"waterCube")) 
                for i in range(2):
                    self.deck.append(Spell(self.get_image("lightningCube"),"lightningCube"))
                for i in range(2):
                    self.deck.append(Spell(self.get_image("threeCubes"),"threeCubes")) 
                for i in range(3):
                    self.deck.append(Spell(self.get_image("waterCube"),"waterCube")) 
                for i in range(3):
                    self.deck.append(Spell(self.get_image("lightningCube"),"lightningCube"))
                for i in range(3):
                    self.deck.append(Spell(self.get_image("neutralEnder"),"neutralEnder"))
                for i in range(3):
                    self.deck.append(Spell(self.get_image("lightCube"),"lightCube"))
                for i in range(2):
                    self.deck.append(Spell(self.get_image("reflector"),"reflector"))
                for i in range(4):
                    self.deck.append(Spell(self.get_image("teleport"),"teleport"))
                for i in range(1):
                    self.deck.append(Spell(self.get_image("randomCard"),"randomCard"))
                for i in range(1):
                    self.deck.append(Spell(self.get_image("reload"),"reload"))
    def shuffle(self):
        random.shuffle(self.deck)
    def top_card(self):
        self.count -= 1
        return self.deck.pop()
    def getCount(self):
        return self.count

        

    
        
    



# Example usage
#pygame.init()

# Set up the display
#screen_width = 800
#screen_height = 600
#screen = pygame.display.set_mode((screen_width, screen_height))
#pygame.display.set_caption("Image Loader")


#image_loader =  Deck(1)

# Load images from the folder




#running = True
#while running:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False

    # Clear the screen
#    screen.fill((255, 255, 255))

    # Draw an image from the ImageLoader
 #   image = image_loader.get_image("speedWand")
 #   if image:
 #       screen.blit(image, (100, 100))

    # Update the display
  #  pygame.display.flip()

