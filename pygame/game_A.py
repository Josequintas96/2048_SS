import os
from tkinter.messagebox import showerror
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
# from .2048_SS.logicT import *
# complete path => /Users/failop/Projects/p2048/2048_SS
#complete path => 2048_SS
# sys.path.append('../')
from logicT import * 

pygame.init()


#title
pygame.display.set_caption("2048")
iconX = pygame.image.load("numbers/Play.ico")
pygame.display.set_icon(iconX)

#size of the window
screen = pygame.display.set_mode((800,800)) #height X:800  weight Y: 600
					#start at left up corner

#image:
scoreImg = pygame.image.load("numbers/figures/score_64.png")
Control_board = pygame.image.load("numbers/figures/Sboard.png")
SettingsImg = pygame.image.load("numbers/figures/settings.png")
SettingsImgB = pygame.image.load("numbers/figures/settings2.png")
scoreValue = 0


#letters valuese
letter_a = pygame.image.load("numbers/letters/a_32.png")
letter_c = pygame.image.load("numbers/letters/c_32.png")
letter_e = pygame.image.load("numbers/letters/e_32.png")
letter_o = pygame.image.load("numbers/letters/o_32.png")
letter_r = pygame.image.load("numbers/letters/r_32.png")
letter_s = pygame.image.load("numbers/letters/s_32.png")
letter_t = pygame.image.load("numbers/letters/t_32.png")

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
Shortcut_T = False

def gameOver(pX, pY):
	screen.blit(GameoverImg,(pX, pY))
	# screen.blit(special_squareImg1,(pX, pY))

CongratulationImg = pygame.image.load("numbers/figures/congratulation_512.png")
Congratulation_T = False

def Congratulation(pX, pY):
	screen.blit(CongratulationImg,(pX, pY))
	# screen.blit(special_squareImg1,(pX, pY))
 
def Dis_Settings(pX, pY):
    screen.blit(SettingsImg,(pX, pY))
    
def Dis_SettingsB(pX, pY):
    screen.blit(SettingsImgB,(pX, pY))


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
	#TTHE IMAGE SCORE IS DISPLAY
	screen.blit(scoreImg,(pX, pY))
 
def board_control(pX, pY):
    #this is the board of shorcuts conttrols
    screen.blit(Control_board, (pX, pY) )

def scoreX2(pX, pY):
	#the phrase score is display
	moveZ = 32
	screen.blit(letter_e,(pX, pY))
	screen.blit(letter_r,((pX-moveZ-2) , pY))
	screen.blit(letter_o,( (pX-moveZ*2-4), pY))
	screen.blit(letter_c,( (pX-moveZ*3-4) , pY))
	screen.blit(letter_s,( (pX-moveZ*4-2) , pY))


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


running = True
gameX = Arr_block()
gameX.new_round()
game_end = False
while running:
	# print("Super Array => ", gameX.array_illustration())
 
	mx, my = pygame.mouse.get_pos()
	loc = [mx , my]
    
    
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if loc[0] > 10 and loc[0] <74:
					if loc[1] > 726 and loc[1] < 790:
						if Shortcut_T == False:
							Shortcut_T = True
						# print("location is ", loc)
				elif Shortcut_T:
					Shortcut_T = False

		#if keystroke press
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT or event.key == pygame.K_a:
				# print("Left arrrow press")
				if gameX.new_move("left") == True:
					game_end = True
					scoreValue = gameX.ret_score()
				
			if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
				# print("Right key is press")
				if gameX.new_move("right") == True:
					game_end = True
					scoreValue = gameX.ret_score()
				

			if event.key == pygame.K_UP or event.key == pygame.K_w:
				# print("Up key is press")
				if gameX.new_move("up") == True:
					game_end = True
					scoreValue = gameX.ret_score()

			if event.key == pygame.K_DOWN or event.key == pygame.K_s:
				# print("Down key is press")
				if gameX.new_move("down") == True:
					game_end = True
					scoreValue = gameX.ret_score()
     
			if event.key == pygame.K_TAB:
				gameX.resetS_2048()
				gameX.new_round()
				scoreValue = gameX.ret_score()
				Gameover_T = False

			# 
			if event.key == pygame.K_r:
				# print("Score is: ", gameX.ret_score())
				# print("Restart has been pressed")
				gameX.restore_stage()
				scoreValue = gameX.ret_score()
				# print("Previous score of game: ", gameX.ret_score())
				# print()
				
			# if event.key == pygame.K_p:
			# 	#print("New arouond start")
			# 	if Congratulation_T == False:
			# 		Congratulation_T = True
			# 	else:
			# 		Congratulation_T = False

		# if event.type == pygame.KEYUP:
		# 	if event.key == pygame.K_LEFT:
		# 		print("Left arrrow release")

		# 	if event.key == pygame.K_RIGHT:
		# 		print("Right arrrow release")

		# 	if event.key == pygame.K_UP:
		# 		print("Up arrrow release")

		# 	if event.key == pygame.K_DOWN:
		# 		print("Down arrow release")

	screen.fill((204 , 204, 0))
	#if bellow screen.fill, then the image will be bellow the color

	
	# 1 column
	# stopI(160,120)




	

	gameStage(208,168, gameX.array_illustration())
	stopchain(160,120, gameX.ret_highspace_T() , gameX.ret_highspace() )
	# gameStage(208,168, [[2,0,0,4],[0,0,0,0],[0,0,0,0],[16,0,0,8]])
	# gameStage(208,168, [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
	

	if game_end == True:
		# print("Thiis is suppose to happen")
		gameX.new_round()
		game_end = False
		scoreValue = gameX.ret_score()
	# else:
	# 	print("This is not suppose tto happen")

	#set thee value of the score
	#scoreX(396, 680)
	scoreX2(396, 680)
	scoreVX(680, 680)

	if gameX.spaceX() == 16 and Gameover_T==False:
		# print("All spaces are filled")
		if gameX.all_poss() == True:
			gameOver(170, 170)
			Gameover_T=True
	if Gameover_T:
		gameOver(170, 170)
	if Shortcut_T == True:
		board_control(160,200)

	if (loc[0] > 10 and loc[0] <74) and (loc[1] > 726 and loc[1] < 790):
		Dis_Settings(10,726)
	else:
		Dis_SettingsB(10,726)

	if gameX.ret_highspace_V() == 2048:
    #  and Congratulation_T == False:
		# print("Congratulatiion, end game")
		Congratulation(180, 140)
	# if Congratulation_T == True:
	# 	Congratulation(180, 140)

	pygame.display.update()

