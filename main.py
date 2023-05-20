import pygame
import sys
from deck import Deck

def main():



    pygame.init()
    clock = pygame.time.Clock()
    cardCount = 30

    arguments = sys.argv

    ButtonP = arguments[1]
    ButtonK = arguments[2]
    buttonS = arguments[3]
    buttonsH = arguments[4]

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Asuka Trainer")
    #with open("./properties.txt", "r") as file:
    #    number = int(file.read())
    deck1 = Deck(1)
    deck1.init_deck()
    deck1.shuffle()

    deck2 = Deck(2)
    deck2.init_deck()
    deck2.shuffle()

    deck3 = Deck(3)
    deck3.init_deck()
    deck3.shuffle()

    activeCards = []

    decks = [deck1, deck2, deck3]
    currentDeck = 0

    card1 = decks[currentDeck].top_card()
    card1.name = "card1"
    card1.setX(0)
    card1.setY(100)
    activeCards.append(card1)
    card2 = decks[currentDeck].top_card()
    card2.name = "card2"
    card2.setX(200)
    card2.setY(100)
    activeCards.append(card2)
    card3 = decks[currentDeck].top_card()
    card3.name = "card3"
    card3.setX(400)
    card3.setY(100)
    activeCards.append(card3)
    card4 = decks[currentDeck].top_card()
    card4.name = "card4"
    card4.setX(600)
    card4.setY(100)
    activeCards.append(card4)
    running = True


    card1Present = True
    Card2Present = True
    Card3Present = True
    Card4Present = True
    reloadCurrent = False;
    cardCount -=4

    HAT_2 = (0, -1)
    HAT_3 = (1, -1)
    HAT_6 = (1, 0)

   

    input_sequence = []
    button_pressed = False
    action_performed_236 = False
    action_performed_22 = False





    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.JOYDEVICEADDED:
                joy = pygame.joystick.Joystick(event.device_index) 
            if event.type == pygame.JOYHATMOTION:
                if event.joy == 0:
                    if event.value == HAT_2:
                        input_sequence.append("2")
                    elif event.value == HAT_3:
                        input_sequence.append("3")
                    elif event.value == HAT_6:
                        input_sequence.append("6")
            if event.type == pygame.JOYBUTTONDOWN:
                print("down")
                if "".join(input_sequence) == "236":
                    print("yes")
                    if event.button == int(ButtonP) and cardCount >1:
                        button_pressed = True
                        if card1Present == True:
                            if reloadCurrent != True:
                                print("it happened")
                                for cards in activeCards:
                                    if cards.name == "card1":
                                        activeCards.remove(cards)
                            else:
                                reloadCurrent = False

                        # image_rect = card1.get_image().move(0,100)
                        # screen.fill((255,255,255), image_rect)
                            pygame.display.update()
                            card1Present = False

                            if card1.get_spell() == "quickBookmark":
                                if card1Present == False:
                                    print("THJLKSDHLAJKDHASLKJDH")
                                    card1 = decks[currentDeck].top_card()
                                    card1.name = "card1"
                                    card1.setX(0)
                                    card1.setY(100)
                                    activeCards.append(card1)
                                    cardCount-=1
                                    card1Present = True
                                if Card2Present == False:
                                    card2 = decks[currentDeck].top_card()
                                    card2.name = "card2"
                                    card2.setX(200)
                                    card2.setY(100)
                                    activeCards.append(card2)
                                    cardCount-=1
                                    Card2Present = True
                                if Card3Present == False:
                                    card3 = decks[currentDeck].top_card()
                                    card3.name = "card3"
                                    card3.setX(400)
                                    card3.setY(100)
                                    activeCards.append(card3)
                                    cardCount-=1
                                    Card3Present = True
                                if Card4Present == False:
                                    card4 = decks[currentDeck].top_card()
                                    card4.name = "card4"
                                    card4.setX(600)
                                    card4.setY(100)
                                    activeCards.append(card4)
                                    cardCount-=1
                                    Card4Present = True
                            if card1.get_spell() == "swap":
                                if card1Present == False:
                                    print("THJLKSDHLAJKDHASLKJDH")
                                    card1 = decks[currentDeck].top_card()
                                    card1.name = "card1"
                                    card1.setX(0)
                                    card1.setY(100)
                                    activeCards.append(card1)
                                    cardCount-=1
                                    card1Present = True
                                if Card2Present == False:
                                    card2 = decks[currentDeck].top_card()
                                    card2.name = "card2"
                                    card2.setX(200)
                                    card2.setY(100)
                                    activeCards.append(card2)
                                    cardCount-=1
                                    Card2Present = True
                                if Card3Present == False:
                                    card3 = decks[currentDeck].top_card()
                                    card3.name = "card3"
                                    card3.setX(400)
                                    card3.setY(100)
                                    activeCards.append(card3)
                                    cardCount-=1
                                    Card3Present = True
                                if Card4Present == False:
                                    card4 = decks[currentDeck].top_card()
                                    card4.name = "card4"
                                    card4.setX(600)
                                    card4.setY(100)
                                    activeCards.append(card4)
                                    cardCount-=1
                                    Card4Present = True
                            
                            elif card1.get_spell() == "randomCard":
                                    if card1Present == False:
                                        print("THJLKSDHLAJKDHASLKJDH")
                                        card1 = decks[currentDeck].top_card()
                                        card1.name = "card1"
                                        card1.setX(0)
                                        card1.setY(100)
                                        activeCards.append(card1)
                                        cardCount-=1
                                        card1Present = True
                            elif card1.get_spell() == "quickSwap":
                                    if card1Present == False:
                                        print("THJLKSDHLAJKDHASLKJDH")
                                        card1 = decks[currentDeck].top_card()
                                        card1.name = "card1"
                                        card1.setX(0)
                                        card1.setY(100)
                                        activeCards.append(card1)
                                        cardCount-=1
                                        card1Present = True
                            elif card1.get_spell() == "reload":
                                reloadCurrent = True
                                
                        elif card1Present == False:
                            print("THJLKSDHLAJKDHASLKJDH")
                            card1 = decks[currentDeck].top_card()
                            card1.name = "card1"
                            card1.setX(0)
                            card1.setY(100)
                            activeCards.append(card1)
                            cardCount-=1
                            card1Present = True
                        
                        
                    if event.button == int(ButtonK) and cardCount >1:
                        if Card2Present == True:
                            if reloadCurrent != True:
                                print("it happened")
                                for cards in activeCards:
                                    if cards.name == "card2":
                                        activeCards.remove(cards) 
                            # image_rect = card1.get_image().move(0,100)
                            # screen.fill((255,255,255), image_rect)
                                pygame.display.update()
                                Card2Present = False
                            else: 
                                reloadCurrent = False


                            if card2.get_spell() == "quickBookmark":
                                    if card1Present == False:
                                        print("THJLKSDHLAJKDHASLKJDH")
                                        card1 = decks[currentDeck].top_card()
                                        card1.name = "card1"
                                        card1.setX(0)
                                        card1.setY(100)
                                        activeCards.append(card1)
                                        cardCount-=1
                                        card1Present = True
                                    if Card2Present == False:
                                        card2 = decks[currentDeck].top_card()
                                        card2.name = "card2"
                                        card2.setX(200)
                                        card2.setY(100)
                                        activeCards.append(card2)
                                        cardCount-=1
                                        Card2Present = True
                                    if Card3Present == False:
                                        card3 = decks[currentDeck].top_card()
                                        card3.name = "card3"
                                        card3.setX(400)
                                        card3.setY(100)
                                        activeCards.append(card3)
                                        cardCount-=1
                                        Card3Present = True
                                    if Card4Present == False:
                                        card4 = decks[currentDeck].top_card()
                                        card4.name = "card4"
                                        card4.setX(600)
                                        card4.setY(100)
                                        activeCards.append(card4)
                                        cardCount-=1
                                        Card4Present = True
                            if card2.get_spell() == "swap":
                                    if card1Present == False:
                                        print("THJLKSDHLAJKDHASLKJDH")
                                        card1 = decks[currentDeck].top_card()
                                        card1.name = "card1"
                                        card1.setX(0)
                                        card1.setY(100)
                                        activeCards.append(card1)
                                        cardCount-=1
                                        card1Present = True
                                    if Card2Present == False:
                                        card2 = decks[currentDeck].top_card()
                                        card2.name = "card2"
                                        card2.setX(200)
                                        card2.setY(100)
                                        activeCards.append(card2)
                                        cardCount-=1
                                        Card2Present = True
                                    if Card3Present == False:
                                        card3 = decks[currentDeck].top_card()
                                        card3.name = "card3"
                                        card3.setX(400)
                                        card3.setY(100)
                                        activeCards.append(card3)
                                        cardCount-=1
                                        Card3Present = True
                                    if Card4Present == False:
                                        card4 = decks[currentDeck].top_card()
                                        card4.name = "card4"
                                        card4.setX(600)
                                        card4.setY(100)
                                        activeCards.append(card4)
                                        cardCount-=1
                                        Card4Present = True
                        
                            elif card2.get_spell() == "randomCard":
                                if Card2Present == False:
                                        card2 = decks[currentDeck].top_card()
                                        card2.name = "card2"
                                        card2.setX(200)
                                        card2.setY(100)
                                        activeCards.append(card2)
                                        cardCount-=1
                                        Card2Present = True
                            elif card2.get_spell() == "quickSwap":
                                if Card2Present == False:
                                        card2 = decks[currentDeck].top_card()
                                        card2.name = "card2"
                                        card2.setX(200)
                                        card2.setY(100)
                                        activeCards.append(card2)
                                        cardCount-=1
                                        Card2Present = True
                            elif card2.get_spell() == "reload":
                                reloadCurrent = True;


                        elif Card2Present == False:
                            print("THJLKSDHLAJKDHASLKJDH")
                            card2 = decks[currentDeck].top_card()
                            card2.name = "card2"
                            card2.setX(200)
                            card2.setY(100)
                            activeCards.append(card2)
                            cardCount-=1
                            Card2Present = True


                    if event.button == int(buttonS) and cardCount >1:
                        if Card3Present == True:
                            if reloadCurrent != True:
                                print("it happened")
                                for cards in activeCards:
                                    if cards.name == "card3":
                                        activeCards.remove(cards) 
                            # image_rect = card1.get_image().move(0,100)
                            # screen.fill((255,255,255), image_rect)
                                pygame.display.update()
                                Card3Present = False
                            else:
                                reloadCurrent = False
                            if card3.get_spell() == "quickBookmark" :
                                    if card1Present == False:
                                        print("THJLKSDHLAJKDHASLKJDH")
                                        card1 = decks[currentDeck].top_card()
                                        card1.name = "card1"
                                        card1.setX(0)
                                        card1.setY(100)
                                        activeCards.append(card1)
                                        cardCount-=1
                                        card1Present = True
                                    if Card2Present == False:
                                        card2 = decks[currentDeck].top_card()
                                        card2.name = "card2"
                                        card2.setX(200)
                                        card2.setY(100)
                                        activeCards.append(card2)
                                        cardCount-=1
                                        Card2Present = True
                                    if Card3Present == False:
                                        card3 = decks[currentDeck].top_card()
                                        card3.name = "card3"
                                        card3.setX(400)
                                        card3.setY(100)
                                        activeCards.append(card3)
                                        cardCount-=1
                                        Card3Present = True
                                    if Card4Present == False:
                                        card4 = decks[currentDeck].top_card()
                                        card4.name = "card4"
                                        card4.setX(600)
                                        card4.setY(100)
                                        activeCards.append(card4)
                                        cardCount-=1
                                        Card4Present = True
                            if card3.get_spell() == "swap" :
                                    if card1Present == False:
                                        print("THJLKSDHLAJKDHASLKJDH")
                                        card1 = decks[currentDeck].top_card()
                                        card1.name = "card1"
                                        card1.setX(0)
                                        card1.setY(100)
                                        activeCards.append(card1)
                                        cardCount-=1
                                        card1Present = True
                                    if Card2Present == False:
                                        card2 = decks[currentDeck].top_card()
                                        card2.name = "card2"
                                        card2.setX(200)
                                        card2.setY(100)
                                        activeCards.append(card2)
                                        cardCount-=1
                                        Card2Present = True
                                    if Card3Present == False:
                                        card3 = decks[currentDeck].top_card()
                                        card3.name = "card3"
                                        card3.setX(400)
                                        card3.setY(100)
                                        activeCards.append(card3)
                                        cardCount-=1
                                        Card3Present = True
                                    if Card4Present == False:
                                        card4 = decks[currentDeck].top_card()
                                        card4.name = "card4"
                                        card4.setX(600)
                                        card4.setY(100)
                                        activeCards.append(card4)
                                        cardCount-=1
                                        Card4Present = True
                            elif card3.get_spell() == "randomCard":
                                if Card3Present == False:
                                        card3 = decks[currentDeck].top_card()
                                        card3.name = "card3"
                                        card3.setX(400)
                                        card3.setY(100)
                                        activeCards.append(card3)
                                        cardCount-=1
                                        Card3Present = True
                            elif card3.get_spell() == "quickSwap":
                                if Card3Present == False:
                                        card3 = decks[currentDeck].top_card()
                                        card3.name = "card3"
                                        card3.setX(400)
                                        card3.setY(100)
                                        activeCards.append(card3)
                                        cardCount-=1
                                        Card3Present = True
                            elif card3.get_spell() == "reload":
                                reloadCurrent = True;
                    
                        elif Card3Present == False:
                            print("THJLKSDHLAJKDHASLKJDH")
                            card3 = decks[currentDeck].top_card()
                            card3.name = "card3"
                            card3.setX(400)
                            card3.setY(100)
                            activeCards.append(card3)
                            cardCount-=1
                            Card3Present = True

                    if event.button == int(buttonsH) and cardCount >1:
                        if Card4Present == True:
                            if reloadCurrent != True:
                                print("it happened")
                                for cards in activeCards:
                                    if cards.name == "card4":
                                        activeCards.remove(cards) 
                            # image_rect = card1.get_image().move(0,100)
                            # screen.fill((255,255,255), image_rect)
                                pygame.display.update()
                                Card4Present = False
                            else:
                                reloadCurrent = False
                            if card4.get_spell() == "quickBookmark":
                                    if card1Present == False:
                                        print("THJLKSDHLAJKDHASLKJDH")
                                        card1 = decks[currentDeck].top_card()
                                        card1.name = "card1"
                                        card1.setX(0)
                                        card1.setY(100)
                                        activeCards.append(card1)
                                        cardCount-=1
                                        card1Present = True
                                    if Card2Present == False:
                                        card2 = decks[currentDeck].top_card()
                                        card2.name = "card2"
                                        card2.setX(200)
                                        card2.setY(100)
                                        activeCards.append(card2)
                                        cardCount-=1
                                        Card2Present = True
                                    if Card3Present == False:
                                        card3 = decks[currentDeck].top_card()
                                        card3.name = "card3"
                                        card3.setX(400)
                                        card3.setY(100)
                                        activeCards.append(card3)
                                        cardCount-=1
                                        Card3Present = True
                                    if Card4Present == False:
                                        card4 = decks[currentDeck].top_card()
                                        card4.name = "card4"
                                        card4.setX(600)
                                        card4.setY(100)
                                        activeCards.append(card4)
                                        cardCount-=1
                                        Card4Present = True
                            if card4.get_spell() == "swap":
                                if card1Present == False:
                                    print("THJLKSDHLAJKDHASLKJDH")
                                    card1 = decks[currentDeck].top_card()
                                    card1.name = "card1"
                                    card1.setX(0)
                                    card1.setY(100)
                                    activeCards.append(card1)
                                    cardCount-=1
                                    card1Present = True
                                if Card2Present == False:
                                    card2 = decks[currentDeck].top_card()
                                    card2.name = "card2"
                                    card2.setX(200)
                                    card2.setY(100)
                                    activeCards.append(card2)
                                    cardCount-=1
                                    Card2Present = True
                                if Card3Present == False:
                                    card3 = decks[currentDeck].top_card()
                                    card3.name = "card3"
                                    card3.setX(400)
                                    card3.setY(100)
                                    activeCards.append(card3)
                                    cardCount-=1
                                    Card3Present = True
                                if Card4Present == False:
                                    card4 = decks[currentDeck].top_card()
                                    card4.name = "card4"
                                    card4.setX(600)
                                    card4.setY(100)
                                    activeCards.append(card4)
                                    cardCount-=1
                                    Card4Present = True                                       
                            elif card4.get_spell() == "randomCard":
                                print("TRIGGER")
                                print(card4.get_spell())
                                if Card4Present == False:
                                    card4 = decks[currentDeck].top_card()
                                    card4.name = "card4"
                                    card4.setX(600)
                                    card4.setY(100)
                                    activeCards.append(card4)
                                    cardCount-=1
                                    Card4Present = True
                            elif card4.get_spell() == "quickSwap":
                                print("TRIGGER")
                                print(card4.get_spell())
                                if Card4Present == False:
                                    card4 = decks[currentDeck].top_card()
                                    card4.name = "card4"
                                    card4.setX(600)
                                    card4.setY(100)
                                    activeCards.append(card4)
                                    cardCount-=1
                                    Card4Present = True
                            elif card4.get_spell() == "reload":
                                reloadCurrent = True;

                        elif Card4Present == False:
                            print("THJLKSDHLAJKDHASLKJDH")
                            card4 = decks[currentDeck].top_card()
                            card4.name = "card4"
                            card4.setX(600)
                            card4.setY(100)
                            activeCards.append(card4)
                            cardCount-=1
                            Card4Present = True
                    print("DONE")
                if "".join(input_sequence) == "22":
                    if event.button == 2:
                        currentDeck = 0
                    if event.button == 0:
                        print("RANDPOM")
                        print("before:",currentDeck)
                        currentDeck = 1
                        print("after:",currentDeck)
                    elif event.button == 3:
                        currentDeck = 2  
            if event.type == pygame.JOYBUTTONUP:
                
                input_sequence.clear()        
            print(input_sequence)
            
        
               
        
            

    
        screen.fill((0, 0, 0))
        
        for card in activeCards:
            card.draw(screen)
        font = pygame.font.Font(None, 36)
        text_count = "Current Deck: " + str(currentDeck) + "   Cards Left: " + str(decks[currentDeck].getCount())
      
        text_count = font.render(text_count, True, (255, 255, 255))
        
        screen.blit(text_count, (0, 0))
        
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()