'''STOCK INVESTMENT SIMULATOR GAME
Created on 11/23/2018
By: Thushen, Om, Max
'''

from iexfinance import get_historical_data
import pygame
import time
from datetime import datetime
import matplotlib.pyplot as plt
import random
from stockFunction import getPrice


#---------------DECLARE VARIABLES----------------

#Colors
BLACK    = ( 0, 0, 0)
WHITE    = ( 255, 255, 255)
GREEN    = ( 0, 255, 0)
RED      = ( 255, 0, 0)
LIGHTGREY = (200,200,200)
GREY = (180, 180, 180)
DARKGREY = (130,130,130)
LIGHTBLUE = (0, 191, 255)
BLUE = (0, 0, 255)
#Process variables
done = False
clock = pygame.time.Clock()

#Main variables:
AAPLSTOCKS = 0
TSLASTOCKS = 0
NFLXSTOCKS = 0
SBUXSTOCKS = 0
AMDSTOCKS = 0
NVDASTOCKS = 0
MSFTSTOCKS = 0
WMTSTOCKS = 0



timer1 = 6000
timer2 = 3000
timer3 = 2000
timer4 = 1000
timer5 = 1200
timer6 = 2600
timer7 = 4600
timer8 = 3800
timer9 = 0

splatoons = 10000
globalCount = 0
mouse = False
stocks = 0
status = 1
currentStock = ''
stockX = 550
stockY = 400


#---------------PROCESS CODE---------------------
pygame.init()
display_width=1500
display_length=900
size =(display_width,display_length)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Stock Simulator Game")


#sound
pygame.mixer.music.load('MiroPetals.mp3')
pygame.mixer.music.play(-1)


#Get lives prices: FIRST RUN
        #1/ AAPL
AAPL = getPrice("https://fr.finance.yahoo.com/quote/AAPL?p=AAPL")
         #2/ TSLA
TSLA = 1
         #3/ AMD
AMD = getPrice("https://fr.finance.yahoo.com/quote/AMD?p=AMD&.tsrc=fin-srch")
         #4/ WMT
WMT = getPrice("https://fr.finance.yahoo.com/quote/WMT?p=WMT&.tsrc=fin-srch")
         #5/ NVDA
NVDA = getPrice("https://fr.finance.yahoo.com/quote/NVDA?p=NVDA&.tsrc=fin-srch") 
         #6/ NFLX
NFLX = getPrice("https://fr.finance.yahoo.com/quote/NFLX?p=NFLX&.tsrc=fin-srch")
         #7/ SBUX
SBUX = getPrice("https://fr.finance.yahoo.com/quote/SBUX?p=SBUX&.tsrc=fin-srch") 
         #8/ MSFT
MSFT = getPrice("https://fr.finance.yahoo.com/quote/MSFT?p=MSFT")
      

#First run
player1Money = random.randrange(6000, 6500)
player2Money = random.randrange(6000, 6500)
player3Money = random.randrange(6000, 7000)
player4Money = random.randrange(6000, 7000)
player5Money = random.randrange(6000, 8000)
player6Money = random.randrange(7000, 9000)
player7Money = random.randrange(10000, 10500)
player8Money = random.randrange(10000, 11000)
player9Money = random.randrange(10000, 11000)
currentPlayer = splatoons


def drawGame():
   
   global globalCount, stocks, AAPL, TSLA, AMD, NVDA, NFLX, SBUX, MSFT, WMT, mouse, currentStock, AAPLSTOCKS, AMDSTOCKS, WMTSTOCKS, NVDASTOCKS, NFLXSTOCKS, TSLASTOCKS, SBUXSTOCKS, MSFTSTOCKS, splatoons, status, stockX,stockY
   

   def checkIfStock(stockNum, stock, stockPrice, substract, multiply, sellAmount):   #(TSLASTOCKS, 'TSLA', TSLA, 1, 1)
      global currentStock, splatoons, AAPLSTOCKS, AMDSTOCKS, WMTSTOCKS, NVDASTOCKS, NFLXSTOCKS, TSLASTOCKS, SBUXSTOCKS, MSFTSTOCKS
      mainFont = pygame.font.SysFont('Calibri', 150, True, False)
      stockText = mainFont.render("No Stocks To Sell! Buy More!",True,BLACK)
      if currentStock == stock:
         if stockNum < sellAmount:
             print('You dont have enough stocks')
         else:
            if currentStock == 'AAPL':
               AAPLSTOCKS -= substract
               splatoons += stockPrice * multiply
            if currentStock == 'NFLX':
               NFLXSTOCKS -= substract
               splatoons += stockPrice * multiply
            if currentStock == 'AMD':
               AMDSTOCKS -= substract
               splatoons += stockPrice * multiply
            if currentStock == 'SBUX':
               SBUXSTOCKS -= substract
               splatoons += stockPrice * multiply
            if currentStock == 'NVDA':
               NVDASTOCKS -= substract
               splatoons += stockPrice * multiply
            if currentStock == 'WMT':
               WMTSTOCKS -= substract
               splatoons += stockPrice * multiply
            if currentStock == 'TSLA':
               TSLASTOCKS -= substract
               splatoons += stockPrice * multiply
            if currentStock == 'MSFT':
               MSFTSTOCKS -= substract
               splatoons += stockPrice * multiply
      
      
   def checkBuy(stockNum, stock, stockPrice, add, multiply, sellAmount):   #(TSLASTOCKS, 'TSLA', TSLA, 1, 1)
      global currentStock, splatoons, AAPLSTOCKS, AMDSTOCKS, WMTSTOCKS, NVDASTOCKS, NFLXSTOCKS, TSLASTOCKS, SBUXSTOCKS, MSFTSTOCKS
      if currentStock == stock:
         if splatoons < stockPrice * multiply:
            print('Not enough money')
         else:
            if currentStock == 'AAPL':
               AAPLSTOCKS += add
               splatoons -= stockPrice * multiply
            if currentStock == 'NFLX':
               NFLXSTOCKS += add
               splatoons -= stockPrice * multiply
            if currentStock == 'AMD':
               AMDSTOCKS += add
               splatoons -= stockPrice * multiply
            if currentStock == 'SBUX':
               SBUXSTOCKS += add
               splatoons -= stockPrice * multiply
            if currentStock == 'NVDA':
               NVDASTOCKS += add
               splatoons -= stockPrice * multiply
            if currentStock == 'WMT':
               WMTSTOCKS += add
               splatoons -= stockPrice * multiply
            if currentStock == 'TSLA':
               TSLASTOCKS += add
               splatoons -= stockPrice * multiply
            if currentStock == 'MSFT':
               MSFTSTOCKS += add
               splatoons -= stockPrice * multiply
   #Game logic--------------------------
   pos = pygame.mouse.get_pos()
   mouseX = pos[0]
   mouseY = pos[1]
   
   globalCount += 1
   if globalCount >= 400:
      globalCount = 0
    #Get lives prices:
            #1/ AAPL
      AAPL = getPrice("https://fr.finance.yahoo.com/quote/AAPL?p=AAPL")
               #2/ TSLA
      TSLA = getPrice("https://fr.finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch")
               #3/ AMD
      AMD = getPrice("https://fr.finance.yahoo.com/quote/AMD?p=AMD&.tsrc=fin-srch")
               #4/ WMT
      WMT = getPrice("https://fr.finance.yahoo.com/quote/WMT?p=WMT&.tsrc=fin-srch")
               #5/ NVDA
      NVDA = getPrice("https://fr.finance.yahoo.com/quote/NVDA?p=NVDA&.tsrc=fin-srch") 
               #6/ NFLX
      NFLX = getPrice("https://fr.finance.yahoo.com/quote/NFLX?p=NFLX&.tsrc=fin-srch")
               #7/ SBUX
      SBUX = getPrice("https://fr.finance.yahoo.com/quote/SBUX?p=SBUX&.tsrc=fin-srch") 
               #8/ MSFT
      MSFT = getPrice("https://fr.finance.yahoo.com/quote/MSFT?p=MSFT")
         
         
   #Variables
   totalStocks = AAPLSTOCKS + AMDSTOCKS + WMTSTOCKS + NVDASTOCKS + NFLXSTOCKS + TSLASTOCKS + SBUXSTOCKS + MSFTSTOCKS


   #Check if player lost:
   if splatoons < 0 and totalStocks < 0:
      totalStocks = 0
      AAPLSTOCKS = 0
      TSLASTOCKS = 0
      NFLXSTOCKS = 0
      SBUXSTOCKS = 0
      AMDSTOCKS = 0
      NVDASTOCKS = 0
      MSFTSTOCKS = 0
      WMTSTOCKS = 0
      splatoons = 0
      status = 1

   #GRAPH DATA
   start = datetime(2018, 11, 1)
   end = datetime.now()
   end.isoformat()
  
   #'Sell stocks'
   mainFont = pygame.font.SysFont('Calibri', 50, True, False)
   sellText = mainFont.render("Sell Stocks",True,BLACK)
   
   
   #fontsize
   mainFont = pygame.font.SysFont('Calibri', 50, True, False)
   sideFont = pygame.font.SysFont("Calibri",40,True,False)
   xFont = pygame.font.SysFont("Calibri",25,True,False)
  
   #Render letters on main game
   buyText = mainFont.render("Buy Stocks",True,BLACK)
   stock_selected =xFont.render("Stock Selected:",True,BLACK)
   amount_money=xFont.render("Splatoons:",True,BLACK)
   amount_share=xFont.render("Amount of Shares:",True,BLACK)
   
   #'Total Splatoons And Stocks'
   mainFont = pygame.font.SysFont('Calibri', 50, True, False)
   stockText = mainFont.render(str(stocks),True,RED)


   
   #1
   num1 = sideFont.render('1', True, WHITE)
   num10 = sideFont.render('10', True, WHITE)
   num100 = sideFont.render('100', True, WHITE)
   num1000= sideFont.render('1000', True, WHITE)   
   #-1
   num1_n = sideFont.render('-1', True, WHITE)
   num10_n = sideFont.render('-10', True, WHITE)
   num100_n = sideFont.render('-100', True, WHITE)
   num1000_n= sideFont.render('-1000', True, WHITE)
   
   


   #STOCK PRICES BUTTON:
   stockFont = pygame.font.SysFont('Calibri', 28, True, False)
   #AAPL
   aaplT1 = stockFont.render('AAPL:', True, BLACK)
   aaplT = stockFont.render(str(AAPL),True, BLACK)
   aaplT2 = stockFont.render(str(AAPL),True,WHITE)
   aaplT3 = stockFont.render('AAPL:',True,WHITE)
   #TSLA
   tslaT1 = stockFont.render('TSLA:', True, BLACK)
   tslaT = stockFont.render(str(TSLA),True, BLACK)
   tslaT2 = stockFont.render(str(TSLA),True,WHITE)
   tslaT3 = stockFont.render('TSLA:',True,WHITE)
   #NFLX
   nflxT1 = stockFont.render('NFLX:', True, BLACK)
   nflxT = stockFont.render(str(NFLX),True, BLACK)
   nflxT2 = stockFont.render(str(NFLX),True,WHITE)
   nflxT3 = stockFont.render('NFLX:',True,WHITE)
   #AMD
   amdT1 = stockFont.render('AMD:', True, BLACK)
   amdT = stockFont.render(str(AMD),True, BLACK)
   amdT2 = stockFont.render(str(AMD),True,WHITE)
   amdT3 = stockFont.render('AMD:',True,WHITE)
   #NVDA
   nvdaT1 = stockFont.render('NVDA:', True, BLACK)
   nvdaT = stockFont.render(str(NVDA),True, BLACK)
   nvdaT2 = stockFont.render(str(NVDA),True,WHITE)
   nvdaT3 = stockFont.render('NVDA:',True,WHITE)
   #WMT
   wmtT1 = stockFont.render('WMT:', True, BLACK)
   wmtT = stockFont.render(str(WMT),True, BLACK)
   wmtT2 = stockFont.render(str(WMT),True,WHITE)
   wmtT3 = stockFont.render('WMT:',True,WHITE)
   #SBUX
   sbuxT1 = stockFont.render('SBUX:', True, BLACK)
   sbuxT = stockFont.render(str(SBUX),True, BLACK)
   sbuxT2 = stockFont.render(str(SBUX),True,WHITE)
   sbuxT3 = stockFont.render('SBUX:',True,WHITE)
   #MSFT
   msftT1 = stockFont.render('MSFT:', True, BLACK)
   msftT = stockFont.render(str(MSFT),True, BLACK)
   msftT2 = stockFont.render(str(MSFT),True,WHITE)
   msftT3 = stockFont.render('MSFT:',True,WHITE)
   
   
   #INFORMATION SCREEN TEXT
   currentStockPrint = stockFont.render(currentStock, True, BLACK)
   splatoonsPrint = stockFont.render(str(splatoons), True, BLACK)
   
   
   #Leaderbord text
   smallFont = pygame.font.SysFont('Calibri', 25, True, False)
   LDB = smallFont.render('LeaderBoard', True, BLACK)
   
   AAPLSTOCKSPRINT = stockFont.render(str(AAPLSTOCKS), True, BLACK)
   TSLASTOCKSPRINT = stockFont.render(str(TSLASTOCKS), True, BLACK)  
   NFLXSTOCKSPRINT = stockFont.render(str(NFLXSTOCKS), True, BLACK)
   SBUXSTOCKSPRINT = stockFont.render(str(SBUXSTOCKS), True, BLACK)
   AMDSTOCKSPRINT = stockFont.render(str(AMDSTOCKS), True, BLACK)
   NVDASTOCKSPRINT = stockFont.render(str(NVDASTOCKS), True, BLACK)
   MSFTSTOCKSPRINT = stockFont.render(str(MSFTSTOCKS), True, BLACK)
   WMTSTOCKSPRINT = stockFont.render(str(WMTSTOCKS), True, BLACK)
   
   
   #Back to min menu text
   smallFont = pygame.font.SysFont('Calibri', 25, True, False)
   BTMM = smallFont.render('Back to main menu', True, BLACK)

   
   #Drawing code-----------------------
   background_image4 = pygame.image.load("MainGameBackground.jpg").convert()
   screen.blit(background_image4, [0,0])




   #Buy Buttons-----------------
   #1
   if event.type == pygame.MOUSEBUTTONDOWN and mouseX > 100 and mouseX < 200 and mouseY > 90 and mouseY < 190:
      pygame.draw.rect(screen,GREEN,[100,90,100,100],0)
      screen.blit(num1, [138, 116])
      mouse = True
   else:
      pygame.draw.rect(screen,BLACK,[100,90,100,100],0)
      screen.blit(num1, [138, 116])
   if mouse and event.type == pygame.MOUSEBUTTONUP and  mouseX > 100 and mouseX < 200 and mouseY > 90 and mouseY < 190:
      checkBuy(AAPLSTOCKS, 'AAPL', AAPL, 1, 1, 1)
      checkBuy(TSLASTOCKS, 'TSLA',TSLA, 1, 1, 1)
      checkBuy(AMDSTOCKS, 'AMD', AMD, 1, 1, 1)
      checkBuy(NFLXSTOCKS, 'NFLX', NFLX, 1, 1, 1)
      checkBuy(NVDASTOCKS, 'NVDA', NVDA, 1, 1, 1)
      checkBuy(WMTSTOCKS, 'WMT', WMT, 1, 1, 1)
      checkBuy(SBUXSTOCKS, 'SBUX', SBUX, 1, 1, 1)
      checkBuy(MSFTSTOCKS, 'MSFT', MSFT, 1, 1, 1)
         
      mouse = False

   else:
      pygame.draw.rect(screen,BLACK,[250,90,100,100],0)
   if mouse and event.type == pygame.MOUSEBUTTONUP and  mouseX > 250 and mouseX < 350 and mouseY > 90 and mouseY < 190:
      checkBuy(AAPLSTOCKS, 'AAPL', AAPL, 10, 10, 10)
      checkBuy(TSLASTOCKS, 'TSLA',TSLA, 10, 10, 10)
      checkBuy(AMDSTOCKS, 'AMD', AMD, 10, 10, 10)
      checkBuy(NFLXSTOCKS, 'NFLX', NFLX, 10, 10, 10)
      checkBuy(NVDASTOCKS, 'NVDA', NVDA, 10, 10, 10)
      checkBuy(WMTSTOCKS, 'WMT', WMT, 10, 10, 10)
      checkBuy(SBUXSTOCKS, 'SBUX', SBUX, 10, 10, 10)
      checkBuy(MSFTSTOCKS, 'MSFT', MSFT, 10, 10, 10)
      mouse = False
   #100 
   if event.type == pygame.MOUSEBUTTONDOWN and mouseX > 400 and mouseX < 500 and mouseY > 90 and mouseY < 190:
      pygame.draw.rect(screen,GREEN,[400,90,100,100],0)
      mouse = True
   else:
      pygame.draw.rect(screen,BLACK,[400,90,100,100],0)
   if mouse and event.type == pygame.MOUSEBUTTONUP and mouseX > 400 and mouseX < 500 and mouseY > 90 and mouseY < 190:
      checkBuy(AAPLSTOCKS, 'AAPL', AAPL, 100, 100, 100)
      checkBuy(TSLASTOCKS, 'TSLA',TSLA, 100, 100, 100)
      checkBuy(AMDSTOCKS, 'AMD', AMD, 100, 100, 100)
      checkBuy(NFLXSTOCKS, 'NFLX', NFLX, 100, 100, 100)
      checkBuy(NVDASTOCKS, 'NVDA', NVDA, 100, 100, 100)
      checkBuy(WMTSTOCKS, 'WMT', WMT, 100, 100, 100)
      checkBuy(SBUXSTOCKS, 'SBUX', SBUX, 100, 100, 100)
      checkBuy(MSFTSTOCKS, 'MSFT', MSFT, 100, 100, 100)
      mouse = False
    #1000  
   if event.type == pygame.MOUSEBUTTONDOWN and mouseX > 550 and mouseX < 650 and mouseY > 90 and mouseY < 190:
      pygame.draw.rect(screen,GREEN,[550,90,100,100],0)
      mouse = True
   else:
      pygame.draw.rect(screen,BLACK,[550,90,100,100],0)
   if mouse and event.type == pygame.MOUSEBUTTONUP and mouseX > 550 and mouseX < 650 and mouseY > 90 and mouseY < 190:
      checkBuy(AAPLSTOCKS, 'AAPL', AAPL, 1000, 1000, 1000)
      checkBuy(TSLASTOCKS, 'TSLA',TSLA, 1000, 1000, 1000)
      checkBuy(AMDSTOCKS, 'AMD', AMD, 1000, 1000, 1000)
      checkBuy(NFLXSTOCKS, 'NFLX', NFLX, 1000, 1000, 1000)
      checkBuy(NVDASTOCKS, 'NVDA', NVDA, 1000, 1000, 1000)
      checkBuy(WMTSTOCKS, 'WMT', WMT, 1000, 1000, 1000)
      checkBuy(SBUXSTOCKS, 'SBUX', SBUX, 1000, 1000, 1000)
      checkBuy(MSFTSTOCKS, 'MSFT', MSFT, 1000, 1000, 1000)
      mouse = False


   #Sell Buttons
   #1
   if event.type == pygame.MOUSEBUTTONDOWN and mouseX > 800 and mouseX < 900 and mouseY > 90 and mouseY < 190:
      pygame.draw.rect(screen,GREEN,[800,90,100,100],0)
      mouse = True
   else: 
      pygame.draw.rect(screen,BLACK,[800,90,100,100],0)
   if mouse and event.type == pygame.MOUSEBUTTONUP and  mouseX > 800 and mouseX < 900 and mouseY > 90 and mouseY < 190:
      checkIfStock(AAPLSTOCKS, 'AAPL', AAPL, 1, 1, 1)
      checkIfStock(TSLASTOCKS, 'TSLA',TSLA, 1, 1, 1)
      checkIfStock(AMDSTOCKS, 'AMD', AMD, 1, 1, 1)
      checkIfStock(NFLXSTOCKS, 'NFLX', NFLX, 1, 1, 1)
      checkIfStock(NVDASTOCKS, 'NVDA', NVDA, 1, 1, 1)
      checkIfStock(WMTSTOCKS, 'WMT', WMT, 1, 1, 1)
      checkIfStock(SBUXSTOCKS, 'SBUX', SBUX, 1, 1, 1)
      checkIfStock(MSFTSTOCKS, 'MSFT', MSFT, 1, 1, 1)
      mouse = False
   #10
   if event.type == pygame.MOUSEBUTTONDOWN and mouseX > 950 and mouseX < 1050 and mouseY > 90 and mouseY < 190:
      pygame.draw.rect(screen,GREEN,[950,90,100,100],0)
      mouse = True
   else: 
      pygame.draw.rect(screen,BLACK,[950,90,100,100],0)
   if mouse and event.type == pygame.MOUSEBUTTONUP and mouseX > 950 and mouseX < 1050 and mouseY > 90 and mouseY < 190:
      checkIfStock(AAPLSTOCKS, 'AAPL', AAPL, 10, 10, 10)
      checkIfStock(TSLASTOCKS, 'TSLA',TSLA, 10, 10, 10)
      checkIfStock(AMDSTOCKS, 'AMD', AMD, 10, 10, 10)
      checkIfStock(NFLXSTOCKS, 'NFLX', NFLX, 10, 10, 10)
      checkIfStock(NVDASTOCKS, 'NVDA', NVDA, 10, 10, 10)
      checkIfStock(WMTSTOCKS, 'WMT', WMT, 10, 10, 10)
      checkIfStock(SBUXSTOCKS, 'SBUX', SBUX, 10, 10, 10)
      checkIfStock(MSFTSTOCKS, 'MSFT', MSFT, 10, 10, 10)
      mouse = False
   #100
   if event.type == pygame.MOUSEBUTTONDOWN and mouseX > 1100 and mouseX < 1200 and mouseY > 90 and mouseY < 190:
      pygame.draw.rect(screen,GREEN,[1100,90,100,100],0)
      mouse = True
   else:
      pygame.draw.rect(screen,BLACK,[1100,90,100,100],0)
   if mouse and event.type == pygame.MOUSEBUTTONUP and mouseX > 1100 and mouseX < 1200 and mouseY > 90 and mouseY < 190:
      checkIfStock(AAPLSTOCKS, 'AAPL', AAPL, 100, 100, 100)
      checkIfStock(TSLASTOCKS, 'TSLA',TSLA, 100, 100, 100)
      checkIfStock(AMDSTOCKS, 'AMD', AMD, 100, 100, 100)
      checkIfStock(NFLXSTOCKS, 'NFLX', NFLX, 100, 100, 100)
      checkIfStock(NVDASTOCKS, 'NVDA', NVDA, 100, 100, 100)
      checkIfStock(WMTSTOCKS, 'WMT', WMT, 10, 100, 100)
      checkIfStock(SBUXSTOCKS, 'SBUX', SBUX, 100, 100, 100)
      checkIfStock(MSFTSTOCKS, 'MSFT', MSFT, 100, 100, 100)
      mouse = False
   #1000
   if event.type == pygame.MOUSEBUTTONDOWN and mouseX > 1250 and mouseX < 1350 and mouseY > 90 and mouseY < 190:
      pygame.draw.rect(screen,GREEN,[1250,90,100,100],0)
      mouse = True
   else:
      pygame.draw.rect(screen,BLACK,[1250,90,100,100],0)
   if mouse and event.type == pygame.MOUSEBUTTONUP and mouseX > 1250 and mouseX < 1350 and mouseY > 90 and mouseY < 190:
      checkIfStock(AAPLSTOCKS, 'AAPL', AAPL, 1000, 1000, 1000)
      checkIfStock(TSLASTOCKS, 'TSLA',TSLA, 1000, 1000, 1000)
      checkIfStock(AMDSTOCKS, 'AMD', AMD, 1000, 1000, 1000)
      checkIfStock(NFLXSTOCKS, 'NFLX', NFLX, 1000, 1000, 1000)
      checkIfStock(NVDASTOCKS, 'NVDA', NVDA, 1000, 1000, 1000)
      checkIfStock(WMTSTOCKS, 'WMT', WMT, 1000, 1000, 1000)
      checkIfStock(SBUXSTOCKS, 'SBUX', SBUX, 1000, 1000, 1000)
      checkIfStock(MSFTSTOCKS, 'MSFT', MSFT, 1000, 1000, 1000)
      mouse = False
   
   #Button Buy (Color change)-----------------
   #+1----------------------------------------
   if event.type == pygame.MOUSEBUTTONDOWN and mouseX > 100 and mouseX < 200 and mouseY > 90 and mouseY < 190:
      pygame.draw.rect(screen,GREEN,[100,90,100,100],0)
      screen.blit(num1, [143, 120])
      mouse = True
   else:
      pygame.draw.rect(screen,BLACK,[100,90,100,100],0)
      screen.blit(num1, [143, 120])
   #+10-------------------------------------------
   if event.type == pygame.MOUSEBUTTONDOWN and mouseX > 250 and mouseX < 350 and mouseY > 90 and mouseY < 190:
      pygame.draw.rect(screen,GREEN,[250,90,100,100],0)
      screen.blit(num10, [280, 120])
      mouse = True
   else:
      pygame.draw.rect(screen,BLACK,[250,90,100,100],0)
      screen.blit(num10, [280, 120])
   #+100----------------------------------
   if event.type == pygame.MOUSEBUTTONDOWN and mouseX > 400 and mouseX < 500 and mouseY > 90 and mouseY < 190:
      pygame.draw.rect(screen,GREEN,[400,90,100,100],0)
      screen.blit(num100, [419, 120])
      mouse = True
   else:
      pygame.draw.rect(screen,BLACK,[400,90,100,100],0)
      screen.blit(num100, [419, 120])

   #+1000----------------------------------
   if event.type == pygame.MOUSEBUTTONDOWN and mouseX > 550 and mouseX < 650 and mouseY > 90 and mouseY < 190:
      pygame.draw.rect(screen,GREEN,[550,90,100,100],0)
      screen.blit(num1000, [560, 120])
      mouse = True
   else:
      pygame.draw.rect(screen,BLACK,[550,90,100,100],0)
      screen.blit(num1000, [560, 120])
  
  
    #Button Sell (Color change)-----------------
    #-1-------------------------------------
   if event.type == pygame.MOUSEBUTTONDOWN and mouseX > 800 and mouseX < 900 and mouseY > 90 and mouseY < 190:
      pygame.draw.rect(screen,RED,[800,90,100,100],0)
      screen.blit(num1_n, [831, 120])
      mouse = True
   else:
      pygame.draw.rect(screen,BLACK,[800,90,100,100],0)
      screen.blit(num1_n, [831, 120])
   #-10-----------------------------    
   if event.type == pygame.MOUSEBUTTONDOWN and mouseX > 950 and mouseX < 1050 and mouseY > 90 and mouseY < 190:
      pygame.draw.rect(screen,RED,[950,90,100,100],0)
      screen.blit(num10_n, [973, 120])
      mouse = True
   else:
      pygame.draw.rect(screen,BLACK,[950,90,100,100],0)
      screen.blit(num10_n, [973, 120])
   #-100-----------------------------    
   if event.type == pygame.MOUSEBUTTONDOWN and mouseX > 1100 and mouseX < 1200 and mouseY > 90 and mouseY < 190:
      pygame.draw.rect(screen,RED,[1100,90,100,100],0)
      screen.blit(num100_n, [1114, 120])
      mouse = True
   else:
      pygame.draw.rect(screen,BLACK,[1100,90,100,100],0)
      screen.blit(num100_n, [1114, 120])
   #-1000-----------------------------    
   if event.type == pygame.MOUSEBUTTONDOWN and mouseX > 1250 and mouseX < 1350 and mouseY > 90 and mouseY < 190:
      pygame.draw.rect(screen,RED,[1250,90,100,100],0)
      screen.blit(num1000_n, [1254, 120])
      mouse = True
   else:
      pygame.draw.rect(screen,BLACK,[1250,90,100,100],0)
      screen.blit(num1000_n, [1254, 120])
  
  
   #Companies
   #AAPL Button
   if event.type == pygame.MOUSEBUTTONDOWN and mouseX > 30 and mouseX < 210 and mouseY > 400 and mouseY < 490:
      pygame.draw.rect(screen, BLACK, [30, 400, 180, 90], 0)
      screen.blit(aaplT2,[120, 436])
      screen.blit(aaplT3, [40, 436])
      currentStock = 'AAPL'
      mouse = True
   else:
      pygame.draw.rect(screen, WHITE, [30, 400, 180, 90], 0)
      screen.blit(aaplT,[120, 436])
      screen.blit(aaplT1, [40, 436])
      
   ''' 
   if mouse and event.type == pygame.MOUSEBUTTONUP and mouseX > 30 and mouseX < 210 and mouseY > 400 and mouseY < 490:
      currentStock = 'AAPL'
      AAPLgraph = get_historical_data("AAPL", start, end, output_format='pandas')
      plt.plot(AAPLgraph["close"])
      plt.title('Time series chart for AAPL')
      plt.show()
      mouse = False
    '''  
   #TSLA Button
   if event.type == pygame.MOUSEBUTTONDOWN  and mouseX > 240 and mouseX < 420 and mouseY > 400 and mouseY < 490:
      pygame.draw.rect(screen, BLACK, [240, 400, 180, 90], 0)
      screen.blit(tslaT2,[320, 436])
      screen.blit(tslaT3, [250, 436])
      currentStock = 'TSLA'
      mouse = True
   else:
      pygame.draw.rect(screen, WHITE, [240, 400, 180, 90], 0)
      screen.blit(tslaT,[320, 436])
      screen.blit(tslaT1, [250, 436])
   ''' 
   if mouse and event.type == pygame.MOUSEBUTTONUP and mouseX > 240 and mouseX < 420 and mouseY > 400 and mouseY < 490:
      currentStock = 'TSLA'
      TSLAgraph = get_historical_data("TSLA", start, end, output_format='pandas')
      plt.plot(TSLAgraph["close"])
      plt.title('Time series chart for TSLA')
      plt.show()
      mouse = False
   '''  
      
   #NFLX Button   
   if event.type == pygame.MOUSEBUTTONDOWN  and mouseX > 450 and mouseX < 630 and mouseY > 400 and mouseY < 490:
      pygame.draw.rect(screen, BLACK, [450, 400, 180, 90], 0)
      screen.blit(nflxT2,[530, 436])
      screen.blit(nflxT3, [460, 436])
      currentStock = 'NFLX'
      mouse = True
   else: 
      pygame.draw.rect(screen, WHITE, [450, 400, 180, 90], 0) 
      screen.blit(nflxT,[530, 436])
      screen.blit(nflxT1, [460, 436])
      '''
      if mouse and event.type == pygame.MOUSEBUTTONUP  and mouseX > 450 and mouseX < 630 and mouseY > 400 and mouseY < 490:
         currentStock = 'NFLX'
         NFLXgraph = get_historical_data("NFLX", start, end, output_format='pandas')
         plt.plot(NFLXgraph["close"])
         plt.title('Time series chart for NFLX')
         plt.show()
         mouse = False
      '''
   #SBUX Button   
   if event.type == pygame.MOUSEBUTTONDOWN and mouseX > 660 and mouseX <  840 and mouseY > 400 and mouseY < 490:
      pygame.draw.rect(screen, BLACK, [660, 400, 180, 90], 0)
      screen.blit(sbuxT2,[750, 436])
      screen.blit(sbuxT3, [670, 436])
      currentStock = 'SBUX'
      mouse = True
   else:
      pygame.draw.rect(screen, WHITE, [660, 400, 180, 90], 0)
      screen.blit(sbuxT,[750, 436])
      screen.blit(sbuxT1, [670, 436])
   '''
   if mouse and event.type == pygame.MOUSEBUTTONUP and mouseX > 660 and mouseX <  840 and mouseY > 400 and mouseY < 490:
      currentStock = 'SBUX'
      SBUXgraph = get_historical_data("SBUX", start, end, output_format='pandas')
      plt.plot(SBUXgraph["close"])
      plt.title('Time series chart for SBUX')
      plt.show()
      mouse = False
   '''     
      
      
   #AMD Button
   if event.type == pygame.MOUSEBUTTONDOWN and mouseX > 30 and mouseX < 210 and mouseY > 600 and mouseY < 690:
      pygame.draw.rect(screen, BLACK, [30, 600, 180, 90], 0)
      screen.blit(amdT2,[120, 636])
      screen.blit(amdT3, [40, 636])
      currentStock = 'AMD'
      mouse = True
   else:
      pygame.draw.rect(screen, WHITE, [30, 600, 180, 90], 0)
      screen.blit(amdT,[120, 636])
      screen.blit(amdT1, [40, 636])
   '''      
   if mouse and event.type == pygame.MOUSEBUTTONUP and mouseX > 30 and mouseX < 210 and mouseY > 600 and mouseY < 690:
      currentStock = 'AMD'      
      AMDgraph = get_historical_data("AMD", start, end, output_format='pandas')
      plt.plot(AMDgraph["close"])
      plt.title('Time series chart for AMD')
      plt.show()
      mouse = False
   '''      
   #WMT Button
   if event.type == pygame.MOUSEBUTTONDOWN  and mouseX > 240 and mouseX < 420 and mouseY > 600 and mouseY < 690:
      pygame.draw.rect(screen, BLACK, [240, 600, 180, 90], 0)
      screen.blit(wmtT2,[330, 636])
      screen.blit(wmtT3, [250, 636])
      currentStock = 'WMT'
      mouse = True
   else:
      pygame.draw.rect(screen, WHITE, [240, 600, 180, 90], 0)
      screen.blit(wmtT,[330, 636])
      screen.blit(wmtT1, [250, 636])
   '''
   if mouse and event.type == pygame.MOUSEBUTTONUP and mouseX > 240 and mouseX < 420 and mouseY > 600 and mouseY < 690:
      currentStock = 'WMT'
      WMTgraph = get_historical_data("WMT", start, end, output_format='pandas')
      plt.plot(WMTgraph["close"])
      plt.title('Time series chart for WMT')
      plt.show()
      mouse = False
   '''      
            
      
   #NVDA Button   
   if event.type == pygame.MOUSEBUTTONDOWN  and mouseX > 450 and mouseX < 630 and mouseY > 600 and mouseY < 690:
      pygame.draw.rect(screen, BLACK, [450, 600, 180, 90], 0)
      screen.blit(nvdaT2,[540, 636])
      screen.blit(nvdaT3, [460, 636])
      currentStock = 'NVDA'
      mouse = True
   else: 
      pygame.draw.rect(screen, WHITE, [450, 600, 180, 90], 0) 
      screen.blit(nvdaT,[540, 636])
      screen.blit(nvdaT1, [460, 636])
   '''
   if mouse and event.type == pygame.MOUSEBUTTONUP  and mouseX > 450 and mouseX < 630 and mouseY > 600 and mouseY < 690:
      currentStock = 'NVDA'
      NVDAgraph = get_historical_data("NVDA", start, end, output_format='pandas')
      plt.plot(NVDAgraph["close"])
      plt.title('Time series chart for NVDA')
      plt.show()
      mouse = False
   '''      
   #MSFT Button   
   if event.type == pygame.MOUSEBUTTONDOWN and mouseX > 660 and mouseX <  840 and mouseY > 600 and mouseY < 690:
      pygame.draw.rect(screen, BLACK, [660, 600, 180, 90], 0)
      screen.blit(msftT2,[750, 636])
      screen.blit(msftT3, [670, 636])
      currentStock = 'MSFT'
      mouse = True
   else:
      pygame.draw.rect(screen, WHITE, [660, 600, 180, 90], 0)
      screen.blit(msftT,[750, 636])
      screen.blit(msftT1, [670, 636])
   '''
   if mouse and event.type == pygame.MOUSEBUTTONUP and mouseX > 660 and mouseX <  840 and mouseY > 600 and mouseY < 690:
      currentStock = 'MSFT'
      MSFTgraph = get_historical_data("MSFT", start, end, output_format='pandas')
      plt.plot(MSFTgraph["close"])
      plt.title('Time series chart for MSFT')
      plt.show()
      mouse = False
   '''
   #Putting texts onscreen:
   screen.blit(buyText,[280, 20])
   screen.blit(sellText,[990,20])
   screen.blit(stock_selected,[1130,650])
   screen.blit(amount_money,[1190,601])
   screen.blit(amount_share,[1000,700])
   
   #Print Information Screen
   screen.blit(currentStockPrint, [1300, 650])
   screen.blit(splatoonsPrint, [1300, 600])
   
   
   if currentStock == 'AAPL':
      screen.blit(AAPLSTOCKSPRINT, [1200, 700])
   elif currentStock == 'TSLA':
      screen.blit(TSLASTOCKSPRINT, [1200, 700])
   elif currentStock == 'AMD':
      screen.blit(AMDSTOCKSPRINT, [1200, 700])
   elif currentStock == 'NVDA':
      screen.blit(NVDASTOCKSPRINT, [1200, 700])
   elif currentStock == 'SBUX':
      screen.blit(SBUXSTOCKSPRINT, [1200, 700])
   elif currentStock == 'WMT':
      screen.blit(WMTSTOCKSPRINT, [1200, 700])
   elif currentStock == 'MSFT':
      screen.blit(MSFTSTOCKSPRINT, [1200, 700])
   elif currentStock == 'NFLX':
      screen.blit(NFLXSTOCKSPRINT, [1200, 700])
   splatoons = round(splatoons, 2)
   
   
   
   
   
   #Back to main menu Button

   if event.type == pygame.MOUSEBUTTONDOWN and mouseX > 60 and mouseX  < 310 and mouseY > 300 and mouseY < 348:
      mouse = True
      pygame.draw.rect(screen, BLUE, [60, 300, 250, 48])
      screen.blit(BTMM, [85, 317])
   else:
      pygame.draw.rect(screen, LIGHTBLUE, [60, 300, 250, 48])
      screen.blit(BTMM, [85, 317])
   if mouse and event.type == pygame.MOUSEBUTTONUP and mouseX > 60 and mouseX  < 310 and mouseY > 300 and mouseY < 348:
      status = 1
      mouse = False
      
    #LeaderBoard  
   if event.type == pygame.MOUSEBUTTONDOWN and mouseX > 380 and mouseX  < 630 and mouseY > 300 and mouseY < 348:
      mouse = True
      pygame.draw.rect(screen, BLUE, [380, 300, 250, 48])
      screen.blit(LDB, [438, 317])
   else:
      pygame.draw.rect(screen, LIGHTBLUE, [380, 300, 250, 48])
      screen.blit(LDB, [438, 317])
   if mouse and event.type == pygame.MOUSEBUTTONUP and mouseX > 60 and mouseX  < 630 and mouseY > 300 and mouseY < 348:
      status = 5
      mouse = False
   
   
def drawMenu ():
   global DARKGREY, LIGHTGREY, mouse, status
   pos = pygame.mouse.get_pos()
   mouseX = pos[0]
   mouseY = pos[1]

   # 'STARTING SCREEN BACKGROUND VARIABLES'
   background_image = pygame.image.load("StockBackgroundNEW.jpg").convert() # ORIGINAL STARTING SCREEN
   background_image2 = pygame.image.load("StockBackgroundBLUE_NEW.jpg").convert() #START BUTTON CHANGE
   background_image3 = pygame.image.load("StockBackgroundNEW_PURPLE.jpg").convert() # INSTRUCTIONS BUTTON
   background_image4 = pygame.image.load("StockBackgroundRED_NEW.jpg").convert() #QUIT GAME
   # Colour Of Buttons Change
      #START BUTTON
   if event.type == pygame.MOUSEBUTTONDOWN and mouseX > 550 and mouseX  <  850 and mouseY > 400 and mouseY < 600:
      mouse = True
      screen.blit(background_image2,[0,0])
   else:
      screen.blit(background_image, [0, 0])
   
   if mouse and event.type == pygame.MOUSEBUTTONUP and mouseX > 550 and mouseX  <  850 and mouseY > 400 and mouseY < 600:
      status = 2
      mouse = False
      
      #INSTRUCTIONS BUTTON
 #INSTRUCTIONS BUTTON
   if event.type == pygame.MOUSEBUTTONDOWN and mouseX > 200 and mouseX < 400 and mouseY > 100 and mouseY< 300:
      screen.blit(background_image3, [0,0])
      mouse = True
      
   if event.type == pygame.MOUSEBUTTONUP and mouseX > 200 and mouseX < 400 and mouseY > 100 and mouseY< 300:
      status = 3
      mouse = False
      
      #QUIT GAME:
   if event.type == pygame.MOUSEBUTTONDOWN and mouseX > 1100 and mouseX  < 1400 and mouseY > 550 and mouseY < 700:
      screen.blit(background_image4,[0,0])
      mouse = True
   
   
   if mouse and event.type == pygame.MOUSEBUTTONUP and mouseX > 1100 and mouseX  <  1400 and mouseY > 550 and mouseY < 700:
      quit_game()
      mouse = False
      
   #StockBars Background
   #rando = random.randrange(400,801)
   #pygame.draw.line(screen,BLACK,[100,910],[100,rando],10)
   
   
def quit_game():
   pygame.quit
   quit()
   
def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()
    
def do_not_leave():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.quit()
                quit()
                
                       
        screen.fill(LIGHTGREY)
        largeText = pygame.font.Font('freesansbold.ttf',60)
        TextSurf, TextRect = text_objects("Thank you for playing, Click on screen to exit", largeText)
        TextRect.center = ((1500/2),(900/2))
        screen.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)


def drawInstructions():
   global mouse, status
   pos = pygame.mouse.get_pos()
   mouseX = pos[0]
   mouseY = pos[1]
   instruBack = pygame.image.load("InstructionsBackground.jpg").convert() 
   screen.blit(instruBack,[0,0])
   smallFont = pygame.font.SysFont('Calibri', 25, True, False)
   BTMM = smallFont.render('Back to main menu', True, BLACK)
   if event.type == pygame.MOUSEBUTTONDOWN and mouseX > 1250 and mouseX  < 1500 and mouseY > 0 and mouseY < 48:
      mouse = True
      pygame.draw.rect(screen, BLUE, [1250, 0, 250, 48])
      screen.blit(BTMM, [1280, 14])
   else:
      pygame.draw.rect(screen, LIGHTBLUE, [1250, 0, 250, 48])
      screen.blit(BTMM, [1280, 14])
   if mouse and event.type == pygame.MOUSEBUTTONUP and mouseX > 1250 and mouseX  < 1500 and mouseY > 0 and mouseY < 48:
      status = 1
      mouse = False
   
   bgame = smallFont.render("Let's play now!", True, BLACK)
   if event.type == pygame.MOUSEBUTTONDOWN and mouseX > 0 and mouseX  < 210 and mouseY > 0 and mouseY < 48:
      mouse = True
      pygame.draw.rect(screen, BLUE, [0, 0, 210, 48])
      screen.blit(bgame, [15, 14])
   else:
      pygame.draw.rect(screen, LIGHTBLUE, [0, 0, 210, 48])
      screen.blit(bgame, [15, 14])
   if mouse and event.type == pygame.MOUSEBUTTONUP and mouseX > 0 and mouseX  < 210 and mouseY > 0 and mouseY < 48:
      status = 2
      mouse = False
   
   
   mainFont = pygame.font.SysFont('Calibri', 100, True, False)
   instruText = mainFont.render("How To Play",True,BLACK)
   screen.blit(instruText,[500,30])
   
   otherText = pygame.font.SysFont('Algreyea', 50, True,False)
   instruText2 = otherText.render('This game is to build a fundamental understanding of investing while  ',True,WHITE)
   screen.blit(instruText2,[20,150])
   instruText3 = otherText.render('providing players with real-world skills and practice in math, economics,', True, WHITE)
   screen.blit(instruText3,[20,190])
   instruText4 = otherText.render('and other subjects. We are using real life data from NYSC and NASDAQ!',True, WHITE)
   screen.blit(instruText4,[20,230])
   
   instruText5 = otherText.render('1. Invest In Stock Companies. You will be given $5000 to start with and',True,WHITE)
   screen.blit(instruText5,[20,290])
   instruText6 = otherText.render('you will need to earn money investing in the LIVE stocks given and make',True,WHITE)
   instruText7 = otherText.render('your way to the top of the leaderboards.',True,WHITE)
   screen.blit(instruText6,[20,320])
   screen.blit(instruText7,[20,350])
   instruText8 = otherText.render('2. In order to purchase stocks you will need to click on the company that',True,WHITE)
   instruText9 = otherText.render('you wish to invest in. After that on the top of the screen you will see',True,WHITE)
   instruText10 = otherText.render('Buy and Sell buttons which will allow you to invest. Once you feel that',True,WHITE)
   instruText11 = otherText.render('you wish to sell your stocks click on the company then press the sell',True,WHITE)
   instruText12 = otherText.render("buttons.(PS: Don't Forget To Close The Chart If You Wish To Buy/Sell)",True,WHITE)
   instruText13 = otherText.render("*stocks update approximately every 10 seconds when the stock market is",True,WHITE)
   instruText14 = otherText.render(" open",True,WHITE)
   screen.blit(instruText8,[20,400])
   screen.blit(instruText9,[20,430])
   screen.blit(instruText10,[20,460])
   screen.blit(instruText11,[20,490])
   screen.blit(instruText12,[20,520])
   screen.blit(instruText13,[20,785])
   screen.blit(instruText14,[20,820])
   
def drawLeaderboard():
   global splatoons, timer1, player1Money, player2Money, player3Money, player4Money, player5Money, player6Money, player7Money, player8Money, player8Money, player9Money, currentPlayer, otherText, timer2, RED, timer2, timer3, timer4, timer5, timer6, timer7, timer8, timer9, mouse, status,mouseX,mouseY
   
   leaderBack = pygame.image.load("LeaderBackground.jpg").convert() 
   screen.blit(leaderBack,[0,0])
   pos = pygame.mouse.get_pos()
   mouseX = pos[0]
   mouseY = pos[1]
   
   
   #Update player money
   
   pygame.draw.rect(screen, BLACK, [230, 80, 1000, 700], 2)
   pygame.draw.line(screen, BLACK, [230, 150], [1230, 150], 3)
   pygame.draw.line(screen, BLACK, [230, 220], [1230, 220], 3)
   pygame.draw.line(screen, BLACK, [230, 290], [1230, 290], 3)
   pygame.draw.line(screen, BLACK, [230, 360], [1230, 360], 3)
   pygame.draw.line(screen, BLACK, [230, 430], [1230, 430], 3)
   pygame.draw.line(screen, BLACK, [230, 500], [1230, 500], 3)
   pygame.draw.line(screen, BLACK, [230, 570], [1230, 570], 3)
   pygame.draw.line(screen, BLACK, [230, 640], [1230, 640], 3)
   pygame.draw.line(screen, BLACK, [230, 710], [1230, 710], 3)   
   
   #Random AI
   
   timer1 += 1
   timer2 += 1
   timer3 += 1
   timer4 += 1
   timer5 += 1
   timer6 += 1
   timer7 += 1
   timer8 += 1
   timer9 += 1
   
   if timer1 > 3600:
      player1Money = random.randrange(6000, 6500)
      timer1 = 0
   if timer2 >3600:
      player2Money = random.randrange(6000, 6500)
      timer2 = 0
   if timer3 >3600:
      player3Money = random.randrange(6000, 7000)
      timer3 = 0
   if timer4 >3600:
      player4Money = random.randrange(6000, 7000)
      timer4 = 0
   if timer5 >3600:
      player5Money = random.randrange(6000, 8000)
      timer5 = 0
   if timer6 >3600:
      player6Money = random.randrange(7000, 9000)
      timer6 = 0
   if timer7> 3600:
      player7Money = random.randrange(10000, 10500)
      timer7 = 0
   if timer8>3600:
      player8Money = random.randrange(10000, 11000)
      timer8 = 0
   if timer9>3600:
      player9Money = random.randrange(10000, 11000)
      timer9 = 0
      
      currentPlayer = splatoons
      
   
   rank = [player1Money, player2Money, player3Money, player4Money, player5Money, player6Money, player7Money, player8Money, player9Money, currentPlayer]
   rank.sort()
   
   otherText = pygame.font.SysFont('Algreyea', 50, True,False)
   playerrank1 = otherText.render(str(rank[9]),True,BLACK)
   playerrank2 = otherText.render(str(rank[8]),True,BLACK)
   playerrank3 = otherText.render(str(rank[7]),True,BLACK)
   playerrank4 = otherText.render(str(rank[6]),True,BLACK)
   playerrank5 = otherText.render(str(rank[5]),True,BLACK)
   playerrank6 = otherText.render(str(rank[4]),True,BLACK)
   playerrank7 = otherText.render(str(rank[3]),True,BLACK)
   playerrank8 = otherText.render(str(rank[2]),True,BLACK)
   playerrank9 = otherText.render(str(rank[1]),True,BLACK)
   playerrank10 = otherText.render(str(rank[0]),True,BLACK)
   
   #Names declared
   playerName1 = otherText.render('Player 1', True, BLACK)
   playerName2 = otherText.render('Player2', True, BLACK)
   playerName3 = otherText.render('Player3', True, BLACK)   
   playerName4 = otherText.render('Player4', True, BLACK) 
   playerName5 = otherText.render('Player5', True, BLACK) 
   playerName6 = otherText.render('Player6', True, BLACK)
   playerName7 = otherText.render('Player7', True, BLACK)
   playerName8 = otherText.render('Player8', True, BLACK)
   playerName9 = otherText.render('Player9', True, BLACK)
   playerName10 = otherText.render('You', True, RED)

   
   #Rank numbers
   p1 = otherText.render('1', True, BLACK)
   p2 = otherText.render('2', True, BLACK)
   p3 = otherText.render('3', True, BLACK)
   p4 = otherText.render('4', True, BLACK)
   p5 = otherText.render('5', True, BLACK)
   p6 = otherText.render('6', True, BLACK)
   p7 = otherText.render('7', True, BLACK)
   p8 = otherText.render('8', True, BLACK)
   p9 = otherText.render('9', True, BLACK)
   p10 = otherText.render('10', True, BLACK)
   
   #Back to game button
   smallFont = pygame.font.SysFont('Calibri',25,True, False)
   BTMM = smallFont.render('Back to main menu', True, BLACK)
   if event.type == pygame.MOUSEBUTTONDOWN and mouseX > 1250 and mouseX < 1500 and mouseY > 0 and mouseY < 48:
      mouse = True
      pygame.draw.rect(screen,BLUE,[1250,0,250,48])
      screen.blit(BTMM,[1280,14])
   else:
      pygame.draw.rect(screen,LIGHTBLUE,[1250,0,250,48])
      screen.blit(BTMM,[1280,14])
   if mouse and event.type == pygame.MOUSEBUTTONUP and mouseX > 1250 and mouseX < 1500 and mouseY > 0 and mouseY < 48:
      status = 2 
      mouse = False
   
    
   def nameRank(name, player):
      if player == rank[9]:
         screen.blit(name, [600, 100])
      if player == rank[8]:
         screen.blit(name, [600, 170])
      if player == rank[7]:
         screen.blit(name, [600, 240])
      if player == rank[6]:
         screen.blit(name, [600, 310])
      if player == rank[5]:
         screen.blit(name, [600, 380])
      if player == rank[4]:
         screen.blit(name, [600, 450])
      if player == rank[3]:
         screen.blit(name, [600, 520])
      if player == rank[2]:
         screen.blit(name, [600, 590])
      if player == rank[1]:
         screen.blit(name, [600, 660])
      if player == rank[0]:
         screen.blit(name, [600, 730])

   #Names      
   nameRank(playerName1, player1Money)
   nameRank(playerName2, player2Money)
   nameRank(playerName3, player3Money)         
   nameRank(playerName4, player4Money)
   nameRank(playerName5, player5Money)
   nameRank(playerName6, player6Money)
   nameRank(playerName7, player7Money)
   nameRank(playerName8, player8Money)
   nameRank(playerName9, player9Money)
   nameRank(playerName10, currentPlayer)
   
   
   #Money 
   screen.blit(playerrank1, [1000, 100])
   screen.blit(playerrank2, [1000, 170])
   screen.blit(playerrank3, [1000, 240])   
   screen.blit(playerrank4, [1000, 310])
   screen.blit(playerrank5, [1000, 380])   
   screen.blit(playerrank6, [1000, 450])  
   screen.blit(playerrank7, [1000, 520])
   screen.blit(playerrank8, [1000, 590])   
   screen.blit(playerrank9, [1000, 660])   
   screen.blit(playerrank10, [1000, 730])
   
   
   #Rank
   screen.blit(p1, [300, 100])
   screen.blit(p2, [300, 170])
   screen.blit(p3, [300, 240])   
   screen.blit(p4, [300, 310])
   screen.blit(p5, [300, 380])   
   screen.blit(p6, [300, 450])  
   screen.blit(p7, [300, 520])
   screen.blit(p8, [300, 590])   
   screen.blit(p9, [300, 660])   
   screen.blit(p10, [290, 730])
   
#----------------------MAIN GAME LOOP-------------------     

while not done:
   #Close window
   for event in pygame.event.get():  
       if event.type == pygame.QUIT:
           print("User asked to quit.")
           done = True

   #status = 1 = Menu
   #status = 2 = Game
   #status = 3 = Instructions
   #status = 4 = Quit
   if status == 2:
      drawGame()
   elif status == 1:
      drawMenu()
   elif status == 3:
      drawInstructions()
   elif status == 4:
      do_not_leave()
   elif status == 5:
      drawLeaderboard()
      

   
   pygame.display.flip()
   clock.tick(60)


do_not_leave()
pygame.quit()

