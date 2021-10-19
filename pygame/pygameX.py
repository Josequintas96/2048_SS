import pygame
import sys
# from .2048_SS.logicT import *
# complete path => /Users/failop/Projects/p2048/2048_SS
#complete path => 2048_SS
sys.path.append('../')
from logicT import * 

pygame.init()


#title
pygame.display.set_caption("2048")
iconX = pygame.image.load("Play.ico")
pygame.display.set_icon(iconX)

#size of the window
screen = pygame.display.set_mode((800,800)) #height X:800  weight Y: 600
					#start at left up corner

#image:
playerImg = pygame.image.load("motorbike3.png")
playerImg2 = pygame.image.load("numbers/numb/one.png")

scoreImg = pygame.image.load("numbers/figures/score_64.png")
scoreValue = 0

#number values
numbI_one = pygame.image.load("numbers/numb/one_32.png")
numbII_two = pygame.image.load("numbers/numb/two_32.png")
numbIII_three = pygame.image.load("numbers/numb/three_32.png")
numbIV_four = pygame.image.load("numbers/numb/four_32.png")
numbV_five = pygame.image.load("numbers/numb/five_32.png")
numbVI_six = pygame.image.load("numbers/numb/six_32.png")
numbVII_seven = pygame.image.load("numbers/numb/seven_32.png")
numbVIII_eight = pygame.image.load("numbers/numb/eight_32.png")
numbVIV_nine = pygame.image.load("numbers/numb/nine_32.png")
numb_zero = pygame.image.load("numbers/numb/zero_32.png")

playerX = 370
playerY = 480
playerX_c = 0
playerY_c = 0

######################################################################################################
#here I am transfering the square
squareImg1 = pygame.image.load("numbers/figures/stop_128.png")
special_squareImg1 = pygame.image.load("numbers/figures/special_stop_128.png")
special_squareImg2 = pygame.image.load("numbers/figures/special2_stop_128.png")

def stopchain(pX, pY, special, ix):
	sudoku = 138
	i=0
	while i < 4:
		i2=0
		while i2 < 4:
			if special == False:
				stopI(pX+sudoku*i, pY+sudoku*i2)
			else:
				if ix[0] == i2 and ix[1] ==i:
					stopII(pX+sudoku*i, pY+sudoku*i2)
				else:
					stopI(pX+sudoku*i, pY+sudoku*i2)
			
			i2+=1
		i+=1
	
def stopI(pX, pY):
	screen.blit(squareImg1,(pX, pY))
	# screen.blit(special_squareImg1,(pX, pY))
def stopII(pX, pY):
	screen.blit(special_squareImg2,(pX, pY))

######################################################################################################
#Interactions ==> Comments
GameoverImg = pygame.image.load("numbers/figures/game_over_512.png")
Gameover_T = False

def gameOver(pX, pY):
	screen.blit(GameoverImg,(pX, pY))
	# screen.blit(special_squareImg1,(pX, pY))

CongratulationImg = pygame.image.load("numbers/figures/congratulation_512.png")
Congratulation_T = False

def Congratulation(pX, pY):
	screen.blit(CongratulationImg,(pX, pY))
	# screen.blit(special_squareImg1,(pX, pY))


def gameStage(pX, pY, arrX):
	# print("Array: ", arrX)
	sudoku = 138
	i=0
	j=0
	j2=0
	while i < 4:
		i2=0
		j=0
		while i2 < 4:
			if arrX[j][j2] !=0:
				if len(str(arrX[j][j2])) == 1:
					numb_stop( arrX[j][j2] , pX+sudoku*i, pY+sudoku*i2)
				elif len(str(arrX[j][j2])) > 1:
					ix = len(str(arrX[j][j2]))
					ix0 = 0
					pX2 = pX+sudoku*i - (ix-1)*10
					pY2 = pY+sudoku*i2
					while ix0 < ix:
						numb_stop( int(str(arrX[j][j2])[ix0]) ,pX2+ix0*22 , pY2)
						ix0+=1
			
			i2+=1
			j+=1
		i+=1
		j2+=1
	

def numb_stop(valX , pX, pY):
	strX = select_numb(valX)
	screen.blit(strX,(pX, pY))

def numb2(pX, pY):
	screen.blit(numbII_two,(pX, pY))
	
def scoreX(pX, pY):
	screen.blit(scoreImg,(pX, pY))


def select_numb(numb):
	if numb ==0:
		return numb_zero
	elif numb ==1:
		return numbI_one
	elif numb ==2:
		return numbII_two
	elif numb ==3:
		return numbIII_three
	elif numb ==4:
		return numbIV_four
	elif numb ==5:
		return numbV_five
	elif numb ==6:
		return numbVI_six
	elif numb ==7:
		return numbVII_seven
	elif numb ==8:
		return numbVIII_eight
	elif numb ==9:
		return numbVIV_nine

def scoreVX(pX, pY):
	val = len(str(scoreValue))
	i = 0
	pX2 = pX - 36*(len(str(scoreValue))-1)
	while i < val:
		ImgC = select_numb(int(str(scoreValue)[i]))
		screen.blit(ImgC,(pX2+36*i, pY))
		i+=1


def player():
	screen.blit(playerImg,(playerX, playerY))

def player2():
	screen.blit(playerImg2, (100, 200))

running = True
gameX = Arr_block()
gameX.new_round()
game_end = False
while running:
	# print("Super Array => ", gameX.array_illustration())
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		#if keystroke press
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				print("Left arrrow press")
				if gameX.new_move("left") == True:
					game_end = True
					scoreValue = gameX.ret_score()
				playerX_c =-0.5
			if event.key == pygame.K_RIGHT:
				print("Right key is press")
				if gameX.new_move("right") == True:
					game_end = True
					scoreValue = gameX.ret_score()
				playerX_c = 0.5

			if event.key == pygame.K_UP:
				playerY_c = -0.5
				print("Up key is press")
				if gameX.new_move("up") == True:
					game_end = True
					scoreValue = gameX.ret_score()

			if event.key == pygame.K_DOWN:
				print("Down key is press")
				if gameX.new_move("down") == True:
					game_end = True
					scoreValue = gameX.ret_score()
				playerY_c = 0.5

			if event.key == pygame.K_RETURN:
				scoreValue+=1
				# print("The value of enter: ", scoreValue)
				if Gameover_T ==False:
					Gameover_T = True
				else:
    					Gameover_T = False
			if event.key == pygame.K_r:
				print("Score is: ", gameX.ret_score())
				print("Restart has been pressed")
				gameX.restore_stage()
				scoreValue = gameX.ret_score()
				print("Previous score of game: ", gameX.ret_score())
				print()
				
			if event.key == pygame.K_a:
				print("New arouond start")
				# if gameX.new_round() == False:
				# 	print("Game Over")
				# else:
				# 	scoreValue = gameX.ret_score()
				if Congratulation_T == False:
					Congratulation_T = True
				else:
					Congratulation_T = False

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				print("Left arrrow release")
				playerX_c =0

			if event.key == pygame.K_RIGHT:
				print("Right arrrow release")
				playerX_c =0

			if event.key == pygame.K_UP:
				print("Up arrrow release")
				playerY_c =0

			if event.key == pygame.K_DOWN:
				print("Down arrow release")
				playerY_c =0

	screen.fill((204 , 204, 0))
	#if bellow screen.fill, then the image will be bellow the color
	player()

#	player2()
	
	# 1 column
	# stopI(160,120)




	

	gameStage(208,168, gameX.array_illustration())
	stopchain(160,120, gameX.ret_highspace_T() , gameX.ret_highspace() )
	# gameStage(208,168, [[2,0,0,4],[0,0,0,0],[0,0,0,0],[16,0,0,8]])
	# gameStage(208,168, [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
	

	if game_end == True:
		print("Thiis is suppose to happen")
		gameX.new_round()
		game_end = False
		scoreValue = gameX.ret_score()
	# else:
	# 	print("This is not suppose tto happen")

	#set thee value of the score
	scoreX(396, 680)
	scoreVX(680, 680)

	if Gameover_T == True:
		gameOver(200, 200)

	if gameX.ret_highspace_V() == 2048 and Congratulation_T == False:
		# print("Congratulatiion, end game")
		Congratulation(180, 140)
	# if Congratulation_T == True:
	# 	Congratulation(180, 140)

	pygame.display.update()
	playerX += playerX_c
	if playerX >= 680:
		playerX = 680
	elif playerX <= 0:
		playerX =0
	playerY += playerY_c
	if playerY > 480:
		playerY = 480
	elif playerY <= 0:
		playerY =0
#	playerY += playerY_c
	 
#	if playerX > 500:
#		playerY+=0.05
