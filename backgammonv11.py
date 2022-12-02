
## Import START###################################################
import pygame
from pygame.locals import *
import random
import os
from datetime import datetime
import json
## Import END###################################################

## Functions START################################################

# Adds the dice roll to the current position of the chips
def getGoToPOSPlusRoll(startingPOS1, startingPOS2, sortedDiceRoll):
    if startingPOS1 < startingPOS2:
        newPOS1 = sortedDiceRoll[0]+startingPOS1
        newPOS2 = sortedDiceRoll[1]+startingPOS2
    if startingPOS2 < startingPOS1:
        newPOS1 = sortedDiceRoll[1]+startingPOS1
        newPOS2 = sortedDiceRoll[0]+startingPOS2
    if startingPOS1 == startingPOS2:
        newPOS1 = sortedDiceRoll[0]+startingPOS1
        newPOS2 = sortedDiceRoll[1]+startingPOS2

    return newPOS1, newPOS2

#Function to resolve x and y position for chip.
def getXYPOS(Chipindex: int,boardPOS: int):
    #Chip position dictionary
    chipPosDict = '''
    {
        "Chips": [
            {"ChipIndex":0,"boardPOS":1,"x":5,"y":5},
            {"ChipIndex":1,"boardPOS":1,"x":5,"y":60},
            {"ChipIndex":0,"boardPOS":2,"x":65,"y":5},
            {"ChipIndex":1,"boardPOS":2,"x":65,"y":60},
            {"ChipIndex":0,"boardPOS":3,"x":120,"y":5},
            {"ChipIndex":1,"boardPOS":3,"x":120,"y":60},
            {"ChipIndex":0,"boardPOS":4,"x":178,"y":5},
            {"ChipIndex":1,"boardPOS":4,"x":178,"y":60},
            {"ChipIndex":0,"boardPOS":5,"x":235,"y":5},
            {"ChipIndex":1,"boardPOS":5,"x":235,"y":60},
            {"ChipIndex":0,"boardPOS":6,"x":291,"y":5},
            {"ChipIndex":1,"boardPOS":6,"x":291,"y":60},
            {"ChipIndex":0,"boardPOS":7,"x":371,"y":5},
            {"ChipIndex":1,"boardPOS":7,"x":371,"y":60},
            {"ChipIndex":0,"boardPOS":8,"x":429,"y":5},
            {"ChipIndex":1,"boardPOS":8,"x":429,"y":60},
            {"ChipIndex":0,"boardPOS":9,"x":484,"y":5},
            {"ChipIndex":1,"boardPOS":9,"x":484,"y":60},
            {"ChipIndex":0,"boardPOS":10,"x":542,"y":5},
            {"ChipIndex":1,"boardPOS":10,"x":542,"y":60},
            {"ChipIndex":0,"boardPOS":11,"x":597,"y":5},
            {"ChipIndex":1,"boardPOS":11,"x":597,"y":60},
            {"ChipIndex":0,"boardPOS":12,"x":657,"y":5},
            {"ChipIndex":1,"boardPOS":12,"x":657,"y":60},
            {"ChipIndex":0,"boardPOS":13,"x":728,"y":34},
            {"ChipIndex":1,"boardPOS":13,"x":728,"y":96},
            {"ChipIndex":0,"boardPOS":14,"x":728,"y":34},
            {"ChipIndex":1,"boardPOS":14,"x":728,"y":96},
            {"ChipIndex":0,"boardPOS":15,"x":728,"y":34},
            {"ChipIndex":1,"boardPOS":15,"x":728,"y":96},
            {"ChipIndex":0,"boardPOS":16,"x":728,"y":34},
            {"ChipIndex":1,"boardPOS":16,"x":728,"y":96},
            {"ChipIndex":0,"boardPOS":17,"x":728,"y":34},
            {"ChipIndex":1,"boardPOS":17,"x":728,"y":96},
            {"ChipIndex":0,"boardPOS":18,"x":728,"y":34},
            {"ChipIndex":1,"boardPOS":18,"x":728,"y":96},
            {"ChipIndex":0,"boardPOS":19,"x":728,"y":34},
            {"ChipIndex":1,"boardPOS":19,"x":728,"y":96}
        ]
    }
    '''
    #Convert String to JSON
    data = json.loads(chipPosDict)

    #Loop through all lines in dict
    for chip in data['Chips']:
        #If passed values match, return the x and y position
        if chip['ChipIndex'] == Chipindex and chip['boardPOS'] == boardPOS:
            return chip['x'],chip['y']



# This module defines payout
def payout(betAmount: float, startingPoint: int, bonus: bool, betType: str):

    # NO BONUS PAYOUT
    if startingPoint == 1 and betType == "JUMP" and bonus == False:
        payout = betAmount + (betAmount/5)*3
    if startingPoint == 1 and betType == "OUT" and bonus == False:
        payout = betAmount * 2

    if startingPoint == 2 and betType == "JUMP" and bonus == False:
        payout = betAmount * 3
    if startingPoint == 2 and betType == "OUT" and bonus == False:
        payout = betAmount * 2

    if startingPoint == 3 and betType == "JUMP" and bonus == False:
        payout = betAmount * 4
    if startingPoint == 3 and betType == "OUT" and bonus == False:
        payout = betAmount * 5

    if startingPoint == 4 and betType == "JUMP" and bonus == False:
        payout = betAmount * 11
    if startingPoint == 4 and betType == "OUT" and bonus == False:
        payout = betAmount * 6

    if startingPoint == 5 and betType == "JUMP" and bonus == False:
        payout = betAmount * 41
    if startingPoint == 5 and betType == "OUT" and bonus == False:
        payout = betAmount * 10

    # BONUS PAYOUT
    if startingPoint == 1 and betType == "JUMP" and bonus == True:
        payout = betAmount + (betAmount*5)*3 + (betAmount * 0.50)
    if startingPoint == 1 and betType == "OUT" and bonus == True:
        payout = betAmount * 2 + (betAmount * 0.50)

    if startingPoint == 2 and betType == "JUMP" and bonus == True:
        payout = betAmount * 3 + (betAmount * 0.50)
    if startingPoint == 2 and betType == "OUT" and bonus == True:
        payout = betAmount * 2 + (betAmount * 0.50)

    if startingPoint == 3 and betType == "JUMP" and bonus == True:
        payout = betAmount * 4 + (betAmount * 0.50)
    if startingPoint == 3 and betType == "OUT" and bonus == True:
        payout = betAmount * 5 + (betAmount * 0.50)

    if startingPoint == 4 and betType == "JUMP" and bonus == True:
        payout = betAmount * 11 + (betAmount * 0.50)
    if startingPoint == 4 and betType == "OUT" and bonus == True:
        payout = betAmount * 6 + (betAmount * 0.50)

    if startingPoint == 5 and betType == "JUMP" and bonus == True:
        payout = betAmount * 41 + (betAmount * 0.50)
    if startingPoint == 5 and betType == "OUT" and bonus == True:
        payout = betAmount * 10 + (betAmount * 0.50)

    return payout

# Standard Bubble Sort


def bubbleSort(inputArray):
    max_element = len(inputArray) - 1

    while max_element >= 0:
        
        index = 0
        
        while index <= max_element - 1:
        
            if inputArray[index] > inputArray[index+1]:
                temp = inputArray[index]
                inputArray[index] = inputArray[index+1]
                inputArray[index+1] = temp
        
            index = index + 1
        
        max_element = max_element - 1

    return inputArray

# Sort the dice rolles in decending order


def SortDiceRoll(dice1Roll, dice2Roll):
    # Add both dice rolls into an array
    diceRolles = []
    diceRolles.append(dice1Roll)
    diceRolles.append(dice2Roll)

    # Sort the array acscending
    sortedDiceRolles = bubbleSort(diceRolles)
    # Reverse sort to decending
    return sortedDiceRolles[::-1]

# Logs game activity


def writeLogs(level: str, message: str):
    # File Name
    fileName = os.path.basename(__file__)
    # Current Path
    runPath = (os.path.abspath(__file__)).replace(fileName, "")
    # Open log file
    logfile = open('{}{}'.format(runPath, 'logs.log'), 'a')
    # Append to logfile
    logfile.write('{},{},{} \n'.format(datetime.now(), level, message))
    # Close log file
    logfile.close()

## Functions END################################################


## Main Program START###########################################
# File Name
fileName = os.path.basename(__file__)

# Current Path
runPath = (os.path.abspath(__file__)).replace(fileName, "")

# Frames per second
FPS = 60

# Initialize various variables to control Main Window Size, and positions and sized of assets within the game.
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Arrays to store chips objects and their rectangle surface
blackChips = []
blackChipsRects = []

# Size of the chip
CHIPSIZE = 50

# Size of the dice
DICESIZE = 40

# Position of the dice when they appear
DICE1XPOS = 713
DICE1YPOS = 491
DICE2XPOS = 750
DICE2YPOS = 530

# Position of Roll Dice button
ROLLDICEBUTTONX = 713
ROLLDICEBUTTONY = 300

# Size and position of the most common buttons
BUTTONSIZEX = 86
BUTTONSIZEY = 30
POINT2BUTTONX = 713
POINT2BUTTONY = 340
POINT3BUTTONX = 713
POINT3BUTTONY = POINT2BUTTONY + 40
POINT4BUTTONX = 713
POINT4BUTTONY = POINT3BUTTONY + 40
POINT5BUTTONX = 713
POINT5BUTTONY = POINT4BUTTONY + 40

# Position of the Buy In Buttons and Display
BUYINDISPLAYX = 100
BUYINDISPLAYY = 470
BUYINMINUSX = BUYINDISPLAYX + 17
BUYINMINUSY = BUYINDISPLAYY + 70
BUYINPLUSX = BUYINDISPLAYX + 17
BUYINPLUSY = BUYINDISPLAYY - 40

# Set title of main game window
pygame.display.set_caption("Backgammon Casino")

# Assets
# Background
backGroundImage = pygame.transform.scale(pygame.image.load(
    "{}{}".format(runPath, "boardbackground.png")), (WIDTH, HEIGHT))

# Dice Images
one = pygame.transform.scale(pygame.image.load(
    "{}{}".format(runPath, "one.png")), (DICESIZE, DICESIZE))
two = pygame.transform.scale(pygame.image.load(
    "{}{}".format(runPath, "two.png")), (DICESIZE, DICESIZE))
three = pygame.transform.scale(pygame.image.load(
    "{}{}".format(runPath, "three.png")), (DICESIZE, DICESIZE))
four = pygame.transform.scale(pygame.image.load(
    "{}{}".format(runPath, "four.png")), (DICESIZE, DICESIZE))
five = pygame.transform.scale(pygame.image.load(
    "{}{}".format(runPath, "five.png")), (DICESIZE, DICESIZE))
six = pygame.transform.scale(pygame.image.load(
    "{}{}".format(runPath, "six.png")), (DICESIZE, DICESIZE))

# Roll dice button
buttonRollDice = pygame.transform.scale(pygame.image.load(
    "{}{}".format(runPath, "rollDiceEnabled.png")), (BUTTONSIZEX, BUTTONSIZEY))
rollDiceButtonRect = buttonRollDice.get_rect(
    topleft=(ROLLDICEBUTTONX, ROLLDICEBUTTONY))

# New Bet button
buttonNewBet = pygame.transform.scale(pygame.image.load(
    "{}{}".format(runPath, "newBet.png")), (BUTTONSIZEX, BUTTONSIZEY))
newBetButtonRect = buttonNewBet.get_rect(topleft=(713, 200))

# Points buttons
button2Point = pygame.transform.scale(pygame.image.load(
    "{}{}".format(runPath, "point2.png")), (BUTTONSIZEX, BUTTONSIZEY))
point2ButtonRect = button2Point.get_rect(
    topleft=(POINT2BUTTONX, POINT2BUTTONY))

button3Point = pygame.transform.scale(pygame.image.load(
    "{}{}".format(runPath, "point3.png")), (BUTTONSIZEX, BUTTONSIZEY))
point3ButtonRect = button3Point.get_rect(
    topleft=(POINT3BUTTONX, POINT3BUTTONY))

button4Point = pygame.transform.scale(pygame.image.load(
    "{}{}".format(runPath, "point4.png")), (BUTTONSIZEX, BUTTONSIZEY))
point4ButtonRect = button4Point.get_rect(
    topleft=(POINT4BUTTONX, POINT4BUTTONY))

button5Point = pygame.transform.scale(pygame.image.load(
    "{}{}".format(runPath, "point5.png")), (BUTTONSIZEX, BUTTONSIZEY))
point5ButtonRect = button5Point.get_rect(
    topleft=(POINT5BUTTONX, POINT5BUTTONY))

# Bet Amount and adjustment buttons
buttonBetMinus = pygame.transform.scale(pygame.image.load(
    "{}{}".format(runPath, "minus.png")), (29, 33))
minusButtonRect = buttonBetMinus.get_rect(topleft=(292, 490))

buttonBetPlus = pygame.transform.scale(pygame.image.load(
    "{}{}".format(runPath, "plus.png")), (29, 33))
plusButtonRect = buttonBetPlus.get_rect(topleft=(392, 490))

displayBetAmount = pygame.transform.scale(pygame.image.load(
    "{}{}".format(runPath, "betAmount.png")), (63, 63))
betAmountDisplayRect = displayBetAmount.get_rect(topleft=(0, 0))

# Buy in Amount and Adjustment buttons
buttonBuyInMinus = pygame.transform.scale(pygame.image.load(
    "{}{}".format(runPath, "buyInMinus.png")), (29, 33))
buyInMinusButtonRect = buttonBuyInMinus.get_rect(
    topleft=(BUYINMINUSX, BUYINMINUSY))

buttonBuyInPlus = pygame.transform.scale(pygame.image.load(
    "{}{}".format(runPath, "buyInPlus.png")), (29, 33))
buyInPlusButtonRect = buttonBuyInPlus.get_rect(
    topleft=(BUYINPLUSX, BUYINPLUSY))

displayBuyInAmount = pygame.transform.scale(pygame.image.load(
    "{}{}".format(runPath, "buyInAmount.png")), (63, 63))
buyInAmountDisplayRect = displayBuyInAmount.get_rect(topleft=(0, 0))

# Bonus Star
bonusStar = pygame.transform.scale(pygame.image.load(
    "{}{}".format(runPath, "bonusStar.png")), (50, 50))
bonusStarRect = bonusStar.get_rect(topleft=(0, 0))

# Intialize Chips
for r in range(2):
    newChip = None
    newChip = pygame.transform.scale(pygame.image.load(
        "{}{}".format(runPath, "blackChip.png")), (CHIPSIZE, CHIPSIZE))
    newChipRect = newChip.get_rect(topleft=(r*40, 200))
    blackChips.append(newChip)
    blackChipsRects.append(newChipRect)

# MAIN GAME VARIABLES
# Mandator Variable Related to Drawing Assets
clock = pygame.time.Clock()

# Stores the current Chip Index when user clicks on a chip asset
currentChipIndex = None

# Left button
leftButton = 0

# Identifies current player
player = 0

# Stores the randomized value of the dice roll
Dice1Rand = 0
Dice2Rand = 0

# Keeps track of the starting POINT position, should be 1,2,3,4, or 5.
startingPosition = 0

# Stores the number of rolls in the phase. Normally, you have 2 rolls. One for jump bet, and one for out bet.
# You could have a 3rd roll if user rolled a double and made the jump bet
currentRoll = 1

# Stores the accomulated Wins
accomWins = 0

# Stores the buy in amount
buyInAmount = 0

# Flag for identifying if the user managed to roll a double.
doubleRoll = False

# Lost flag to control ability to roll dice and other functions
lost = None

# Pay out amount
payoutAmount = 0

# Indicates that user trigger a bounus
bonusFlag = False

# Stores the bet amount
betAmount = 1

# Setup Bet Amount Display
pygame.font.init()
betAmountFont = pygame.font.SysFont('Arial', 35)

# Setup Buy In Amount Display
buyInAmountFont = pygame.font.SysFont('Arial', 15)

# Setup Info Display
infoDisplayFont = pygame.font.SysFont("Arial", 25)

# Custome Message Variable to update Info Display
custMessage = "Welcome to Backgammon Casino"

# MAIN GAME LOOP
run = True

while run:

    # Determines the refresh frame rate
    clock.tick(FPS)

    # Monitor various events within the game
    for event in pygame.event.get():

        # User is quitting the game. Exit game
        if event.type == pygame.QUIT:
            run = False

        # MOUSE IS PRESSED
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # Determine Which Chip is selected
            for i, c in enumerate(blackChipsRects):
                if c.collidepoint(event.pos):
                    currentChipIndex = i
                    player = 1
                    break
                else:
                    currentChipIndex = None
                    player = None

            # Roll dice by clicking on the Roll Dice button
            if rollDiceButtonRect.collidepoint(event.pos):

                # FIRST ROLL
                if currentRoll == 1:

                    Dice1Rand = random.randint(1, 6)
                    Dice2Rand = random.randint(1, 6)

                    if Dice1Rand == Dice2Rand:
                        doubleRoll = True

                    if (Dice1Rand == 6 and Dice2Rand == 6) or (Dice1Rand == 5 and Dice2Rand == 5):
                        bonusFlag = True
                        payoutAmount = payout(
                            betAmount, currentPoint, bonusFlag, "JUMP")
                        writeLogs("info", "BONUS: Player triggered bonus with {} and {} from point {}. their payout is {}".format(
                            Dice1Rand, Dice2Rand, currentPoint, payoutAmount))
                    else:
                        bonusFlag = False
                        payoutAmount = payout(
                            betAmount, currentPoint, bonusFlag, "JUMP")

                    # gotoPosition currentroll, chipnumber
                    gotoPosition11 = Dice1Rand + startingPosition
                    gotoPosition12 = Dice2Rand + startingPosition

                    blackChipsRects[0].x, blackChipsRects[0].y = getXYPOS(
                        0, gotoPosition11)
                    blackChipsRects[1].x, blackChipsRects[1].y = getXYPOS(
                        1, gotoPosition12)

                    if gotoPosition11 >= 7 and gotoPosition12 >= 7:
                        accomWins += payoutAmount
                        custMessage = "You won jump bet from POINT {}!".format(
                            currentPoint, payoutAmount)
                        writeLogs("info", "Player won the jump bet with {} and {} from point {}. They won {}".format(
                            Dice1Rand, Dice2Rand, currentPoint, payoutAmount))
                        lost = None
                    else:
                        custMessage = "You lost jump bet from POINT {}!".format(
                            currentPoint)
                        writeLogs("info", "Player lost the jump bet with {} and {} from point {}. They lost {}".format(
                            Dice1Rand, Dice2Rand, currentPoint, betAmount))
                        doubleRoll = False
                        lost = True
                        buyInAmount -= betAmount
                        accomWins = 0

                # SECOND ROLL
                if currentRoll == 2:

                    Dice1Rand = random.randint(1, 6)
                    Dice2Rand = random.randint(1, 6)

                    if Dice1Rand == Dice2Rand:
                        doubleRoll = True

                    if (Dice1Rand == 6 and Dice2Rand == 6) or (Dice1Rand == 5 and Dice2Rand == 5):
                        bonusFlag = True
                        payoutAmount = payout(
                            betAmount, currentPoint, bonusFlag, "OUT")
                        writeLogs("info", "BONUS: Player triggered bonus with {} and {} from point {}. their payout is {}".format(
                            Dice1Rand, Dice2Rand, currentPoint, payoutAmount))
                    else:
                        bonusFlag = False
                        payoutAmount = payout(
                            betAmount, currentPoint, bonusFlag, "OUT")

                    gotoPosition21, gotoPosition22 = getGoToPOSPlusRoll(
                        gotoPosition11, gotoPosition12, SortDiceRoll(Dice1Rand, Dice2Rand))

                    blackChipsRects[0].x, blackChipsRects[0].y = getXYPOS(
                        0, gotoPosition21)
                    blackChipsRects[1].x, blackChipsRects[1].y = getXYPOS(
                        1, gotoPosition22)

                    if gotoPosition21 >= 13 and gotoPosition22 >= 13:
                        payoutAmount = payout(
                            betAmount, currentPoint, False, "OUT")
                        accomWins += payoutAmount
                        custMessage = "You won the out bet from POINT {}. You won ${}".format(
                            currentPoint, payoutAmount)
                        writeLogs("info", "Player won the out bet with {} and {} from point {}. They won {}".format(
                            Dice1Rand, Dice2Rand, currentPoint, payoutAmount))
                        buyInAmount += accomWins
                        lost = None
                        doubleRoll = False
                    else:
                        if doubleRoll:
                            custMessage = "You rolled a double. You get another roll."
                            writeLogs("info", "Player rolled a double.{} and {} on point {}".format(
                                Dice1Rand, Dice2Rand, currentPoint))
                            lost = None
                        else:
                            custMessage = "You lost out bet from POINT {}.".format(
                                currentPoint)
                            writeLogs("info", "Player lost the out bet with {} and {} from point {}. They lost {}".format(
                                Dice1Rand, Dice2Rand, currentPoint, betAmount))
                            doubleRoll = False
                            lost = True
                            buyInAmount -= betAmount*2
                            accomWins = 0

                # THIRD ROLL IF ROLLED DOUBLE
                if currentRoll == 3 and doubleRoll:
                    Dice1Rand = random.randint(1, 6)
                    Dice2Rand = random.randint(1, 6)

                    if Dice1Rand == Dice2Rand:
                        doubleRoll = True

                    if (Dice1Rand == 6 and Dice2Rand == 6) or (Dice1Rand == 5 and Dice2Rand == 5):
                        bonusFlag = True
                        payoutAmount = payout(
                            betAmount, currentPoint, bonusFlag, "OUT")
                        writeLogs("info", "BONUS: Player triggered bonus with {} and {} from point {}. their payout is {}".format(
                            Dice1Rand, Dice2Rand, currentPoint, payoutAmount))
                    else:
                        bonusFlag = False
                        payoutAmount = payout(
                            betAmount, currentPoint, bonusFlag, "OUT")

                    gotoPosition31, gotoPosition32 = getGoToPOSPlusRoll(
                        gotoPosition21, gotoPosition22, SortDiceRoll(Dice1Rand, Dice2Rand))

                    blackChipsRects[0].x, blackChipsRects[0].y = getXYPOS(
                        0, gotoPosition31)
                    blackChipsRects[1].x, blackChipsRects[1].y = getXYPOS(
                        1, gotoPosition32)

                    if gotoPosition31 >= 13 and gotoPosition32 >= 13:
                        accomWins += payoutAmount
                        custMessage = "You won the out bet from POINT {}. You won ${}".format(
                            currentPoint, payoutAmount)
                        writeLogs("info", "Player won the out bet with {} and {} from point {}. They won {}".format(
                            Dice1Rand, Dice2Rand, currentPoint, payoutAmount))
                        buyInAmount += accomWins
                        lost = None
                        doubleRoll = False
                    else:
                        custMessage = "You lost out bet from POINT {}.".format(
                            currentPoint)
                        writeLogs("info", "Player lost the out bet with {} and {} from point {}. They lost {}".format(
                            Dice1Rand, Dice2Rand, currentPoint, betAmount))
                        doubleRoll = False
                        lost = True
                        accomWins = 0

                # increment current roll
                currentRoll += 1

            # New bet, reset everything, default to point 1 for chips
            if newBetButtonRect.collidepoint(event.pos):
                currentPoint = 1
                startingPosition = 5
                accomWins = 0
                custMessage = "Roll Dice"
                Dice1Rand = 0
                Dice2Rand = 0
                currentRoll = 1
                doubleRoll = False
                lost = None
                bonusFlag = False

                blackChipsRects[0].x, blackChipsRects[0].y = getXYPOS(
                    0, startingPosition)
                blackChipsRects[1].x, blackChipsRects[1].y = getXYPOS(
                    1, startingPosition)

            # User pressed + button for bet amount, increase bet amount by 1 dollar
            if plusButtonRect.collidepoint(event.pos) and betAmount < 100:
                betAmount += 1

            # User pressed - button for bet amount, decrease bet amount by 1 dollar
            if minusButtonRect.collidepoint(event.pos) and betAmount > 0:
                betAmount -= 1

            # User pressed + button for buy in amount, inrease by 20
            if buyInPlusButtonRect.collidepoint(event.pos) and buyInAmount < 10000:
                buyInAmount += 20

            # User pressed - button for buy in amount, decrease by 20
            if buyInMinusButtonRect.collidepoint(event.pos) and buyInAmount >= 20:
                buyInAmount -= 20

            # User set starting point to POINT 2
            if point2ButtonRect.collidepoint(event.pos):
                currentPoint = 2
                startingPosition = 4
                Dice1Rand = 0
                Dice2Rand = 0
                currentRoll = 1
                doubleRoll = False
                lost = None

                blackChipsRects[0].x, blackChipsRects[0].y = getXYPOS(
                    0, startingPosition)
                blackChipsRects[1].x, blackChipsRects[1].y = getXYPOS(
                    1, startingPosition)

            # User set starting point to POINT 3
            if point3ButtonRect.collidepoint(event.pos):
                currentPoint = 3
                startingPosition = 3
                Dice1Rand = 0
                Dice2Rand = 0
                currentRoll = 1
                doubleRoll = False
                lost = None
                bonusFlag = False

                blackChipsRects[0].x, blackChipsRects[0].y = getXYPOS(
                    0, startingPosition)
                blackChipsRects[1].x, blackChipsRects[1].y = getXYPOS(
                    1, startingPosition)

            # User set starting point to POINT 4
            if point4ButtonRect.collidepoint(event.pos):
                currentPoint = 4
                startingPosition = 2
                Dice1Rand = 0
                Dice2Rand = 0
                currentRoll = 1
                doubleRoll = False
                lost = None
                bonusFlag = False

                blackChipsRects[0].x, blackChipsRects[0].y = getXYPOS(
                    0, startingPosition)
                blackChipsRects[1].x, blackChipsRects[1].y = getXYPOS(
                    1, startingPosition)

            # User set starting point to POINT 5
            if point5ButtonRect.collidepoint(event.pos):
                currentPoint = 5
                startingPosition = 1
                Dice1Rand = 0
                Dice2Rand = 0
                currentRoll = 1
                doubleRoll = False
                lost = None
                bonusFlag = False

                blackChipsRects[0].x, blackChipsRects[0].y = getXYPOS(
                    0, startingPosition)
                blackChipsRects[1].x, blackChipsRects[1].y = getXYPOS(
                    1, startingPosition)

        # MOUSE IS MOVING
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[leftButton]:
                rel = event.rel

                for z, g in enumerate(blackChipsRects):

                    if z == currentChipIndex and player == 1:
                        g.x += rel[0]
                        g.y += rel[1]
      

    WIN.fill((255, 255, 255))
    WIN.blit(backGroundImage, (0, 0))

    for index, chip in enumerate(blackChips):
        WIN.blit(chip, blackChipsRects[index])

    if Dice1Rand == 1:
        WIN.blit(one, (DICE1XPOS, DICE1YPOS))
    elif Dice1Rand == 2:
        WIN.blit(two, (DICE1XPOS, DICE1YPOS))
    elif Dice1Rand == 3:
        WIN.blit(three, (DICE1XPOS, DICE1YPOS))
    elif Dice1Rand == 4:
        WIN.blit(four, (DICE1XPOS, DICE1YPOS))
    elif Dice1Rand == 5:
        WIN.blit(five, (DICE1XPOS, DICE1YPOS))
    elif Dice1Rand == 6:
        WIN.blit(six, (DICE1XPOS, DICE1YPOS))
    elif Dice1Rand == 0:
        pass

    if Dice2Rand == 1:
        WIN.blit(one, (DICE2XPOS, DICE2YPOS))
    elif Dice2Rand == 2:
        WIN.blit(two, (DICE2XPOS, DICE2YPOS))
    elif Dice2Rand == 3:
        WIN.blit(three, (DICE2XPOS, DICE2YPOS))
    elif Dice2Rand == 4:
        WIN.blit(four, (DICE2XPOS, DICE2YPOS))
    elif Dice2Rand == 5:
        WIN.blit(five, (DICE2XPOS, DICE2YPOS))
    elif Dice2Rand == 6:
        WIN.blit(six, (DICE2XPOS, DICE2YPOS))
    elif Dice2Rand == 0:
        pass

    # If lost, Disable Roll Dice Button
    if lost:
        ROLLDICEBUTTONX = 1000
        ROLLDICEBUTTONY = 1000
        rollDiceButtonRect.x, rollDiceButtonRect.y = ROLLDICEBUTTONX, ROLLDICEBUTTONY
        WIN.blit(buttonRollDice, (ROLLDICEBUTTONX, ROLLDICEBUTTONY))
    else:
        ROLLDICEBUTTONX = 713
        ROLLDICEBUTTONY = 300
        rollDiceButtonRect.x, rollDiceButtonRect.y = ROLLDICEBUTTONX, ROLLDICEBUTTONY
        WIN.blit(buttonRollDice, (ROLLDICEBUTTONX, ROLLDICEBUTTONY))

    # Display Bet Amount Assets on Screen
    WIN.blit(displayBetAmount, (325, 475))
    WIN.blit(buttonBetMinus, (292, 490))
    WIN.blit(buttonBetPlus, (392, 490))

    # Display Buy In Amount Assets on screen
    WIN.blit(displayBuyInAmount, (BUYINDISPLAYX, BUYINDISPLAYY))
    WIN.blit(buttonBuyInMinus, (BUYINMINUSX, BUYINMINUSY))
    WIN.blit(buttonBuyInPlus, (BUYINPLUSX, BUYINPLUSY))

    # Display New Bet, and POINT Buttons on screen
    WIN.blit(buttonNewBet, (713, 200))
    WIN.blit(button2Point, (POINT2BUTTONX, POINT2BUTTONY))
    WIN.blit(button3Point, (POINT3BUTTONX, POINT3BUTTONY))
    WIN.blit(button4Point, (POINT4BUTTONX, POINT4BUTTONY))
    WIN.blit(button5Point, (POINT5BUTTONX, POINT5BUTTONY))

    # Render the text displays
    betAmountDisplay = betAmountFont.render(
        '{}'.format(betAmount), False, (0, 0, 0))
    buyInAmountDisplay = buyInAmountFont.render(
        '{}'.format(round(buyInAmount, 2)), False, (0, 0, 0))
    infoDisplay = infoDisplayFont.render(
        '{}'.format(custMessage), False, (255, 255, 255))
    WIN.blit(betAmountDisplay, (340, 486))
    WIN.blit(buyInAmountDisplay, (BUYINDISPLAYX+15, BUYINDISPLAYY+20))
    WIN.blit(infoDisplay, (200, 430))

    # Show bonus star if user hit bonus
    if bonusFlag:
        WIN.blit(bonusStar, (30, 500))
    else:
        WIN.blit(bonusStar, (1000, 1000))

    # Redraw all assets
    pygame.display.update()

pygame.quit()
## Main Program END###########################################