import pygame

class Spell:
    def __init__(self,image, spell):
        self.spell = spell
        self.name = ""
        self.x = 0
        self.y = 0
        self.image = image
        self.rect = self.image.get_rect()
    def set_name(self, name):
        self.name = name;
    def draw(self, surface):
        surface.blit(self.image, (self.x,self.y))
    def setX(self, value):
        self.x = value;
    def setY(self,value):
        self.y = value
    def get_image(self):
        return self.rect
    def get_spell(self):
        return self.spell
    