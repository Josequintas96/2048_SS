import cv2
import matplotlib.pyplot as plt
import keyboard

from random import seed
from random import randint


def preTest(val):
	val += val*val
	return val

class Block:
	num = 0
	def __init__(self):
		self.num=0
	def incr(self, plus):
		self.num += plus
	def reset(self, val):
		self.num = val
	def val(self):
		return self.num

class Arr_block:
	arr = []
	score = 0
	space =0 #number of square filled
	lengthX = 4
	highspace_T = True #is there a higher number
	high_space = [0,0] #location of higher number
	high_spaceV = 0 #value of higher number
	prev_st = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] #store thee values of actual run => previous one
	prev_sc = 0 #previous score shoould bee
	prev_sp = 0 #previous number of scares shoould be

	def __init__(self):
		#print("Initialize happen")
		i=0
		if len(self.arr) < 4:
			while i < self.lengthX:
				arr2 = []
				i2 = 0
				while i2 < self.lengthX:
					x = Block()
					arr2.append(x)
					i2 += 1
				i+=1
				self.arr.append(arr2)
		#print("Block has initialize: " , len(self.arr) )

	def length(self):
		print("This is lenght of object: ", len(self.arr))
		print("\t This is lenght of object P2: ", len(self.arr[0]))

	def return_length(self):
		arrX = []
		arrX.append(len(self.arr))
		arrX.append(len(self.arr[0]))
		return arrX

	def spaceX(self):
		#return number of square filled
		return self.space
	def spaceI(self):
		self.space+=1
	def spaceD(self):
		self.space-=1
	def fake_space(self, fs):
		self.space = fs

	def ret_highspace(self):
		#return location wheere it is suppose too locate the higher numbeer of equation
		return self.high_space

	def ret_highspace_T(self):
		#return if there is a higher number of equation
		return self.highspace_T

	def ret_highspace_V(self):
		#return value of higher number of equation
		return self.high_spaceV

	def scoreX(self):
		print("Score: ", self.score)
	def ret_score(self):
		return self.score
	def new_score(self, val):
		self.score+=val
	def false_score(self, val):
			self.score = val

	def illustrate(self):
		#print the square by square of values
		i=0
		# print("\t", end='')
		while i < 4:
			i2=0
			while i2 < 4:
				# print(self.arr[i][i2].val(), "\t", end='')
				i2+=1
			i+=1
			# print("\n\t", end='')
		self.scoreX()

	def set_current_stage(self):
		#save the stage using at the moment
		ix = len(self.arr)
		i = 0
		while i < ix:
			ix2 = len(self.arr[i])
			i2 = 0
			while i2 < ix2:
				self.prev_st[i][i2] = self.arr[i][i2].val()
				i2+=1	
			i+=1
		self.prev_sc = self.ret_score()
		self.prev_sp = self.spaceX()

	def restore_stage(self):
		#restore the previous stage
		self.cheap_2048(self.prev_st)
		self.false_score(self.prev_sc)
		self.fake_space(self.prev_sp)


	def array_illustration(self):
		# set up the highest values and return and array of current values 
		arr2048 = []
		ix = len(self.arr)
		#print("ix: ", ix)
		i = 0
		maxnumb = 0
		while i < ix:
			ix2 = len(self.arr[i])
			#print("\tix2: ", ix2)
			i2 = 0
			arr_2048_0 = []
			while i2 < ix2:
				if self.arr[i][i2].val() > maxnumb:
					# print("This is a maximun number: ", maxnumb)
					maxnumb = self.arr[i][i2].val()
					self.high_space[0] = i
					self.high_space[1] = i2
				arr_2048_0.append(self.arr[i][i2].val())
				i2+=1
			arr2048.append(arr_2048_0)	
			i+=1
		if maxnumb !=0 and maxnumb > self.high_spaceV:
			self.high_spaceV = maxnumb
		
		if maxnumb ==0:
			self.highspace_T = False
			self.highspace = [0,0]
		else:
			self.highspace_T = True
		return arr2048

	def cheap_2048(self, arrX):
		ix = len(self.arr)
		i = 0
		while i < ix:
			ix2 = len(self.arr[i])
			i2 = 0
			while i2 < ix2:
				self.arr[i][i2].reset(arrX[i][i2])
				i2+=1	
			i+=1

	def reset_2048(self):
		ix = len(self.arr)
		i = 0
		while i < ix:
			ix2 = len(self.arr[i])
			i2 = 0
			while i2 < ix2:
				self.arr[i][i2].reset(0)
				i2+=1	
			i+=1
		self.false_score(0)
		self.fake_space(0)

	def new_round(self):
		# start neew round by adding a number 2 on a random location
		#  if spcae is full reetun False else return True
		if self.spaceX() == 16:
			return False
		valX = randint(0,15)
		loc1 =0
		loc2 =0
		if valX!=0:
			loc1 = int(valX/4)
			loc2 = int(valX%4)
		# print(valX, " => ", end='')
		# print("Location are: ", loc1, " ", loc2)
		while self.arr[loc1][loc2].val() != 0:
			valX = randint(0,15)
			loc1 =0
			loc2 =0
			if valX!=0:
				loc1 = int(valX/4)
				loc2 = int(valX%4)
			#print(valX, " => ", end='')
			#print("Location are: ", loc1, " ", loc2)
		self.arr[loc1][loc2].reset(2)
		self.new_score(2)
		self.spaceI()
		
		return True
	

	def new_action(self):
		while True:
			xa = keyboard.read_key()      
			if xa == "down":
				#print("\tSpecial key => down")
				self.new_move(xa)
				xa = keyboard.read_key()
				break
			elif xa == "right":
				#print("\tSpecial Key =>  right")
				self.new_move(xa)
				xa = keyboard.read_key()
				break
			elif xa == "left":
				#print("\tSpecial Key =>left")
				self.new_move(xa)
				xa = keyboard.read_key()
				break
			elif xa == "up":
				#print("\tSpecial Key => up")
				self.new_move(xa)
				xa = keyboard.read_key()
				break
			# else:
			# 	print("\tKey pressed: ", xa)



	def new_move(self, val):
		#print("\tDouble Special key is ", val)
		occurence = False
		if val == "up":
			#print("Running right")
			i=1
			limitX = 0
			i2 = 0
				#this is the last square can be compare, in case oof fusion, this sqaurre most be take out of equation
			while i2 < 4:
				limitX =0
				# print("Remenber limit is: ", limitX)
				# print("Working on ", i2)
				#print("(",i, " , ", i2, ")" , "Check ", self.arr[i][i2].val() )
				i=1
				while i< self.lengthX:
					if self.arr[i][i2].val() > 0:
						i3 = i
						nextX = True
						while i3 > limitX and nextX:
							#print("\t Something must be done")
							if self.arr[i3][i2].val() == self.arr[i3-1][i2].val() :
								
								#movement is going too happen for first time, sooo I want to save the current game
								if occurence == False:
									self.set_current_stage()

								# print("Compare: ",self.arr[i3][i2].val() , " and ", self.arr[i3-1][i2].val() )
								#increase i3-1
								self.arr[i3-1][i2].incr(self.arr[i3][i2].val())

								#increase score
								self.new_score(self.arr[i3-1][i2].val())

								#replace i3 with 0
								self.arr[i3][i2].reset(0)

								#decrease space
								self.spaceD()
								
								# fix the limit
								limitX = i3

								# print("\t\t Print new limit: ", limitX)
								#No new round
								nextX = False
								i3-=1

								#there is an action
								occurence = True
								
							elif self.arr[i3-1][i2].val() == 0:
								
								#movement is going too happen for first time, sooo I want to save the current game
								if occurence == False:
									self.set_current_stage()

								# print("\t Interchange happen" )
								
								#interchangee values
								self.arr[i3-1][i2].reset( self.arr[i3][i2].val() ) 
								self.arr[i3][i2].reset(0)

								#prepare next round
								i3-=1
								nextX =True
								#there is an action
								occurence = True
							else:
								# print("\tAction no taken")
								#nothing happen => cancel, no modificatioon on new currrent
								nextX= False
					i+=1
				i2+=1
			# i+=1
				
		elif val == "down":
			# print("Running DOWN")
			i=2
			# while i >= 0:
			i2 = 0
			while i2 < 4:
				i =2
				limitX = 3
				# print("(",i, " , ", i2, ")" , "Check ", self.arr[i][i2].val() )
				while i >= 0:
					if self.arr[i][i2].val() > 0:
						i3 = i
						nextX = True
						while i3 < limitX and nextX:
							if self.arr[i3][i2].val() == self.arr[i3+1][i2].val() :
								
								#movement is going too happen for first time, sooo I want to save the current game
								if occurence == False:
									self.set_current_stage()

								# print("Compare: ",self.arr[i3][i2].val() , " and ", self.arr[i3-1][i2].val() )
								#increase i3+1
								self.arr[i3+1][i2].incr(self.arr[i3][i2].val())
								#increase score
								self.new_score(self.arr[i3+1][i2].val())

								#replace i3 with 0
								self.arr[i3][i2].reset(0)
								#decrease space
								self.spaceD()

								# fix the limit
								limitX = i3

								#No new round
								nextX = False
								i3-=1
								#there is an action
								occurence = True

							elif self.arr[i3+1][i2].val() == 0:
								
								#movement is going too happen for first time, sooo I want to save the current game
								if occurence == False:
									self.set_current_stage()

								# print("\t Interchange happen" )
								#interchangee values
								self.arr[i3+1][i2].reset( self.arr[i3][i2].val() )
								self.arr[i3][i2].reset(0)
								#prepare next round
								i3+=1
								nextX =True
								#there is an action
								occurence = True
							else:
								# print("\tAction no taken")
								#nothing happen => cancel, no modifiction oon current stage
								nextX= False
					i-=1			
				i2+=1
				# i-=1
		elif val == "right":
			i2=2
			#while i2 >= 0:
			i=0
			while i < 4:
				# print("(",i, " , ", i2, ")" , "Check ", self.arr[i][i2].val() )
				limitX = 3
				i2 = 2
				while i2 >=0: 
					if self.arr[i][i2].val() > 0:
						i3 = i2
						nextX = True
						while i3 < limitX and nextX:
							if self.arr[i][i3+1].val() == self.arr[i][i3].val():
								
								#movement is going too happen for first time, sooo I want to save the current game
								if occurence == False:
									self.set_current_stage()

								# print("Compare: ",self.arr[i][i3+1].val() , " and ", self.arr[i][i3].val())
								#increase i3-1
								self.arr[i][i3+1].incr(self.arr[i][i3].val())
								#increase score
								self.new_score(self.arr[i][i3+1].val())
								#replace i3 with 0
								self.arr[i][i3].reset(0)
								#decrease space
								self.spaceD()
								# fix the limit
								limitX = i3
								#No new round
								nextX = False
								i3+=1
								#there is an action
								occurence = True
							elif self.arr[i][i3+1].val() == 0:
								
								#movement is going too happen for first time, sooo I want to save the current game
								if occurence == False:
									self.set_current_stage()

								# print("\t Interchange happen" )
								#interchangee values
								self.arr[i][i3+1].reset( self.arr[i][i3].val() )
								self.arr[i][i3].reset(0)

								#prepare next round
								i3+=1
								nextX =True
								#there is an action
								occurence = True
							else:
								# print("\tAction no taken")
								#nothing happen => cancel
								nextX = False
					i2-=1
				i+=1
					#i2-=1
		elif val == "left":
			i2=1
			#while i2 < 4:
			i = 0
			while i < 4:
				# print("(",i, " , ", i2, ")")
				# if i2 < 4:
				# 	print("(",i, " , ", i2, ")" , "Check ", self.arr[i][i2].val() )
				limitX = 0
				i2 = 1
				while i2 < 4: 
					#print("Something happen ", i, " and ", i2)
					if self.arr[i][i2].val() > 0:
							i3 = i2
							nextX = True
							while i3 >limitX and nextX:
								#print("i3 => ", i3)
								if self.arr[i][i3-1].val() == self.arr[i][i3].val():
									
									#movement is going too happen for first time, sooo I want to save the current game
									if occurence == False:
										self.set_current_stage()

									# print("Compare: ",self.arr[i][i3-1].val() , " and ", self.arr[i][i3].val())
									#increase i3-1
									self.arr[i][i3-1].incr(self.arr[i][i3].val())
									#increase score
									self.new_score(self.arr[i][i3-1].val())
									#replace i3 with 0
									self.arr[i][i3].reset(0)
									#decrease space
									self.spaceD()
									# fix the limit
									limitX = i3
									#No new round
									nextX = False
									i3-=1
									#there is an action
									occurence = True
									
								elif self.arr[i][i3-1].val() == 0:
									
									#movement is going too happen for first time, sooo I want to save the current game
									if occurence == False:
										self.set_current_stage()

									# print("\t Interchange happen" )
									#interchangee values
									self.arr[i][i3-1].reset( self.arr[i][i3].val() )
									self.arr[i][i3].reset(0)

									#prepare next round
									i3-=1
									nextX =True
									#there is an action
									occurence = True
								else:
									# print("\tAction no taken")
									#nothing happen => cancel
									nextX = False
					i2+=1				
				i+=1
				#i2+=1
			
		return occurence











