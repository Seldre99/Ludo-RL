import pygame
import random

from numpy.core.multiarray import flagsobj
from pygame.locals import *
import sys
from pygame import font
import time

class gridObj:
    def __init__(self, bgColor, playerList, safe, coordinate):
        self.bgColor = bgColor
        self.playerList = playerList
        self.safe = safe
        self.coordinate = coordinate


class Token:
    def __init__(self, Id, color, state, coordinate,size):
        self.Id = Id
        self.color = color
        self.state = state
        self.coordinate = coordinate
        self.size=size
        self.original_coordinate = coordinate

cList = [(1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 5), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0), (7, 0), (8, 0), (8, 1),
          (8, 2), (8, 3), (8, 4), (8, 5), (9, 6), (10, 6), (11, 6), (12, 6), (13, 6), (14, 6), (14, 7),(14, 8), (13, 8),
          (12, 8), (11, 8), (10, 8), (9, 8), (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (7, 14),(6, 14), (6, 13),
          (6, 12), (6, 11), (6, 10), (6, 9), (5, 8), (4, 8), (3, 8), (2, 8), (1, 8), (0, 8), (0, 7),(0, 6)]
#RGBY
initPos=[[[1,1],[1,4],[4,1],[4,4]],[[10,1],[13,1],[10,4],[13,4]],[[1,10],[4,10],[1,13],[4,13]],[[10,10],[10,13],[13,10],[13,13]]]
pnames=['R','G','B','Y']

height = 1000
width = 800
initx = 0
inity = 0
currentPlayer = 'R'
compTokensLoc=[[1,1],[1,4],[4,1],[4,4]]
n=2
withComputer=False
dice_clicked = False
move_list = []
diceValue = 6
WHITE = (255, 255, 255)


Game_grid = [[-1 for _ in range(15)] for _ in range(15)]
colors=['white','red','green','yellow','blue','black']
colorMatrix = [[-1, -1, -1, -1, -1, -1, 0, 0, 0, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, 0, 2, 2, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, 2, 2, 0, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, 0, 2, 0, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, 0, 2, 0, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, 0, 2, 0, -1, -1, -1, -1, -1, -1],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0],
                [0, 1, 1, 1, 1, 1, 0, 5, 0, 4, 4, 4, 4, 4, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0],
                [-1, -1, -1, -1, -1, -1, 0, 3, 0, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, 0, 3, 0, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, 0, 3, 0, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, 0, 3, 3, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, 3, 3, 0, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, 0, 0, 0, -1, -1, -1, -1, -1, -1]]
coordinateMatrix = [[[initx + i * 50, inity + j * 50] for i in range(0, 15)] for j in range(0, 15)]
safeLocs=[[6,2],[8,1],[12,6],[13,8],[8,12],[6,13],[2,8],[1,6]]
safeMatrix = [[0 for i in range(15)] for j in range(15)]

for i in safeLocs:
    safeMatrix[i[0]][i[1]] = 1

diceFaces = {1: [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
           2: [[0, 1, 0], [0, 0, 0], [0, 1, 0]],
           3: [[0, 1, 0], [0, 1, 0], [0, 1, 0]],
           4: [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
           5: [[1, 0, 1], [0, 1, 0], [1, 0, 1]],
           6: [[1, 0, 1], [1, 0, 1], [1, 0, 1]],
               }

for i in range(15):
    for j in range(15):
        ob = gridObj(colors[colorMatrix[i][j]], [], safeMatrix[i][j], coordinateMatrix[i][j])
        Game_grid[i][j] = ob

for j in range(4):
    for i in range(1,5):
        p=initPos[j][i-1]
        R= Token(pnames[j]+str(i), colors[j+1], 0, (50 *p[0] , 50 * p[1]), 20)
        Game_grid[p[0]][p[1]].playerList.append(R)

def move(initPos, value, current):
    i = 0
    j = -1
    flag = 0
    while True:
        if cList[i] == initPos or j >= 0:
            if current == 'R' and i == 50:
                flag = 1
            if current == 'G' and i == 11:
                flag = 2
            if current == 'B' and i == 37:
                flag = 3
            if current == 'Y' and i == 24:
                flag = 4
            j += 1
            if j == value:
                break
        i = (i + 1) % len(cList)
    if flag == 1:
        return (cList[i][0] + 1, cList[i][1] + 1)
    elif flag == 2:
        return (cList[i][0] + 1, cList[i][1] + 1)
    elif flag == 3:
        return (cList[i][0] + 1, cList[i][1] - 1)
    elif flag == 4:
        return (cList[i][0] - 1, cList[i][1] - 1)
    else:
        return (cList[i][0], cList[i][1])


def relativeToken(pList, x, y):
    l = len(pList)
    relRad = int((2 / (l + 1)) * 20)
    relpt = []
    j = 0
    if l % 2 == 0:
        l1 = [i + 1 for i in range((l // 2))]
        l2 = [i - 1 for i in range((l // 2))]
        relpt = l2[::-1] + l1
    else:
        l1 = [i + 1 for i in range((l // 2))]
        l2 = [i - 1 for i in range((l // 2))]
        relpt = l2[::-1] + [0] + l1
    for p in pList:
        p.size = relRad
        p.coordinates = ((x) + (relpt[j] * (relRad // 2)), (y))
        j += 1

def drawGrid():
    global Game_grid
    newSurface = pygame.display.set_mode((height, width))
    newSurface.fill(WHITE)
    for i in range(15):
        for j in range(15):
            pygame.draw.rect(newSurface, Game_grid[i][j].bgColor, tuple(Game_grid[i][j].coordinate + [50, 50]))
            pygame.draw.rect(newSurface, (0, 0, 0), tuple(Game_grid[i][j].coordinate + [50, 50]), 1)

    # always constant
    pygame.draw.rect(newSurface, colors[1], (initx, inity, 300, 300))
    pygame.draw.rect(newSurface, colors[0], (initx + 50, inity + 50, 200, 200))
    pygame.draw.rect(newSurface, colors[2], (initx + 450, inity, 300, 300))
    pygame.draw.rect(newSurface, colors[0], (initx + 500, inity + 50, 200, 200))
    pygame.draw.rect(newSurface, colors[3], (initx, inity + 450, 300, 300))
    pygame.draw.rect(newSurface, colors[0], (initx + 50, inity + 500, 200, 200))
    pygame.draw.rect(newSurface, colors[4], (initx + 450, inity + 450, 300, 300))
    pygame.draw.rect(newSurface, colors[0], (initx + 500, inity + 500, 200, 200))

    for i in range(15):
        for j in range(15):
            relativeToken(Game_grid[i][j].playerList, i * 50, j * 50)
            for k in Game_grid[i][j].playerList:
                c = k.coordinates
                pygame.draw.circle(newSurface, k.color, (c[0] + 25, c[1] + 25), k.size)
                pygame.draw.circle(newSurface, colors[-1], (c[0] + 25, c[1] + 25), k.size, 1)
                # highlight
                if k.Id[0] == currentPlayer:
                    pygame.draw.circle(newSurface, colors[0], (c[0] + 25, c[1] + 25), k.size - 2, 2)
    # chess_faces

    face = diceFaces[diceValue]
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(newSurface, 'black', ((0 + 800) + (50 * j), (0 + 300) + (50 * i), 50, 50))
            if face[i][j] == 1:
                cIndex=pnames.index(currentPlayer)+1
                pygame.draw.circle(newSurface, colors[cIndex], ((0 + 800) + (50 * j) + 25, (0 + 300) + (50 * i) + 25),
                                   10)
    pygame.draw.rect(newSurface, colors[pnames.index(currentPlayer)+1], ((0 + 798), (0 + 298), 150, 150), 4)
    return newSurface

height = 1000
width = 800
pygame.init()
DISPLAYSURF = pygame.display.set_mode((height, width), flags=pygame.RESIZABLE)
pygame.display.set_caption('PythonGeeks Ludo Game')
font1 = pygame.font.SysFont("Calibri", 50)
label1 = font1.render(str(diceValue), 1, 'black')
DISPLAYSURF.blit(drawGrid(), (0, 0))
DISPLAYSURF.blit(label1, (850, 500))
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

