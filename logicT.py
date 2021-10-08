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
		print("\t", end='')
		while i < 4:
			i2=0
			while i2 < 4:
				print(self.arr[i][i2].val(), "\t", end='')
				i2+=1
			i+=1
			print("\n\t", end='')
		self.scoreX()

	def array_illustration(self):
		arr2048 = []
		ix = len(self.arr)
		#print("ix: ", ix)
		i = 0
		while i < ix:
			ix2 = len(self.arr[i])
			#print("\tix2: ", ix2)
			i2 = 0
			arr_2048_0 = []
			while i2 < ix2:
				arr_2048_0.append(self.arr[i][i2].val())
				i2+=1
			arr2048.append(arr_2048_0)	
			i+=1
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

	def new_round(self):
    	
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
				print("\tSpecial key => down")
				self.new_move(xa)
				xa = keyboard.read_key()
				break
			elif xa == "right":
				print("\tSpecial Key =>  right")
				self.new_move(xa)
				xa = keyboard.read_key()
				break
			elif xa == "left":
				print("\tSpecial Key =>left")
				self.new_move(xa)
				xa = keyboard.read_key()
				break
			elif xa == "up":
				print("\tSpecial Key => up")
				self.new_move(xa)
				xa = keyboard.read_key()
				break
			else:
				print("\tKey pressed: ", xa)



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
				print("Remenber limit is: ", limitX)
				print("Working on ", i2)
				#print("(",i, " , ", i2, ")" , "Check ", self.arr[i][i2].val() )
				i=1
				while i< self.lengthX:
					if self.arr[i][i2].val() > 0:
						i3 = i
						nextX = True
						while i3 > limitX and nextX:
							#print("\t Something must be done")
							if self.arr[i3][i2].val() == self.arr[i3-1][i2].val() :
								print("Compare: ",self.arr[i3][i2].val() , " and ", self.arr[i3-1][i2].val() )
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
								print("\t Interchange happen" )
								
								#interchangee values
								self.arr[i3-1][i2].reset( self.arr[i3][i2].val() ) 
								self.arr[i3][i2].reset(0)

								#prepare next round
								i3-=1
								nextX =True
								#there is an action
								occurence = True
							else:
								print("\tAction no taken")
								#nothing happen => cancel
								nextX= False
					i+=1
				i2+=1
			# i+=1
				
		elif val == "down":
			print("Running DOWN")
			i=2
			# while i >= 0:
			i2 = 0
			while i2 < 4:
				i =2
				limitX = 3
				print("(",i, " , ", i2, ")" , "Check ", self.arr[i][i2].val() )
				while i >= 0:
					if self.arr[i][i2].val() > 0:
						i3 = i
						nextX = True
						while i3 < limitX and nextX:
							if self.arr[i3][i2].val() == self.arr[i3+1][i2].val() :
								print("Compare: ",self.arr[i3][i2].val() , " and ", self.arr[i3-1][i2].val() )
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
								print("\t Interchange happen" )
								#interchangee values
								self.arr[i3+1][i2].reset( self.arr[i3][i2].val() )
								self.arr[i3][i2].reset(0)
								#prepare next round
								i3+=1
								nextX =True
								#there is an action
								occurence = True
							else:
								print("\tAction no taken")
								#nothing happen => cancel
								nextX= False
					i-=1			
				i2+=1
				# i-=1
		elif val == "right":
			i2=2
			#while i2 >= 0:
			i=0
			while i < 4:
				print("(",i, " , ", i2, ")" , "Check ", self.arr[i][i2].val() )
				limitX = 3
				i2 = 2
				while i2 >=0: 
					if self.arr[i][i2].val() > 0:
						i3 = i2
						nextX = True
						while i3 < limitX and nextX:
							if self.arr[i][i3+1].val() == self.arr[i][i3].val():
								print("Compare: ",self.arr[i][i3+1].val() , " and ", self.arr[i][i3].val())
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
								print("\t Interchange happen" )
								#interchangee values
								self.arr[i][i3+1].reset( self.arr[i][i3].val() )
								self.arr[i][i3].reset(0)

								#prepare next round
								i3+=1
								nextX =True
								#there is an action
								occurence = True
							else:
								print("\tAction no taken")
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
				if i2 < 4:
					print("(",i, " , ", i2, ")" , "Check ", self.arr[i][i2].val() )
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
									print("Compare: ",self.arr[i][i3-1].val() , " and ", self.arr[i][i3].val())
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
									print("\t Interchange happen" )
									#interchangee values
									self.arr[i][i3-1].reset( self.arr[i][i3].val() )
									self.arr[i][i3].reset(0)

									#prepare next round
									i3-=1
									nextX =True
									#there is an action
									occurence = True
								else:
									print("\tAction no taken")
									#nothing happen => cancel
									nextX = False
					i2+=1				
				i+=1
				#i2+=1
			
		return occurence



	# def new_move_original(self, val):
	# 	#print("\tDouble Special key is ", val)
	# 	if val == "up":
	# 		#print("Running right")
	# 		i=1
	# 		limitX = 0
	# 		while i < self.lengthX:
	# 			i2 = 0
	# 			 #this is the last square can be compare, in case oof fusion, this sqaurre most be take out of equation
	# 			while i2 < 4:
	# 				print("Remenber limit is: ", limitX)
	# 				print("Working on => ", i, ",", i2, "=>", limitX)
	# 				#print("(",i, " , ", i2, ")" , "Check ", self.arr[i][i2].val() )
	# 				if self.arr[i][i2].val() > 0:
	# 					i3 = i
	# 					nextX = True
	# 					while i3 > limitX and nextX:
	# 						#print("\t Something must be done")
	# 						if self.arr[i3][i2].val() == self.arr[i3-1][i2].val() :
	# 							print("Compare: ",self.arr[i3][i2].val() , " and ", self.arr[i3-1][i2].val() )
	# 							#increase i3-1
	# 							self.arr[i3-1][i2].incr(self.arr[i3][i2].val())

	# 							#increase score
	# 							self.new_score(self.arr[i3-1][i2].val())

	# 							#replace i3 with 0
	# 							self.arr[i3][i2].reset(0)

	# 							#decrease space
	# 							self.spaceD()
								
	# 							# # fix the limit
	# 							# limitX = i3

	# 							# print("\t\t Print new limit: ", limitX)
	# 							#No new round
	# 							nextX = False
	# 							i3-=1

								
	# 						elif self.arr[i3-1][i2].val() == 0:
	# 							print("\t Interchange happen" )
								
	# 							#interchangee values
	# 							self.arr[i3-1][i2].reset( self.arr[i3][i2].val() ) 
	# 							self.arr[i3][i2].reset(0)

	# 							#prepare next round
	# 							i3-=1
	# 							nextX =True
	# 						else:
	# 							print("\tAction no taken")
	# 							#nothing happen => cancel
	# 							nextX= False
	# 				i2+=1
	# 			i+=1
				
	# 	elif val == "down":
	# 		#print("Running right")
	# 		i=2
	# 		while i >= 0:
	# 			i2 = 0
	# 			while i2 < 4:
	# 				print("(",i, " , ", i2, ")" , "Check ", self.arr[i][i2].val() )
	# 				if self.arr[i][i2].val() > 0:
	# 					i3 = i
	# 					nextX = True
	# 					while i3 < 3 and nextX:
	# 						if self.arr[i3][i2].val() == self.arr[i3+1][i2].val() :
	# 							print("Compare: ",self.arr[i3][i2].val() , " and ", self.arr[i3-1][i2].val() )
	# 							#increase i3+1
	# 							self.arr[i3+1][i2].incr(self.arr[i3][i2].val())
	# 							#increase score
	# 							self.new_score(self.arr[i3+1][i2].val())

	# 							#replace i3 with 0
	# 							self.arr[i3][i2].reset(0)
	# 							#decrease space
	# 							self.spaceD()
	# 							#No new round
	# 							nextX = False
	# 							i3-=1

	# 						elif self.arr[i3+1][i2].val() == 0:
	# 							print("\t Interchange happen" )
	# 							#interchangee values
	# 							self.arr[i3+1][i2].reset( self.arr[i3][i2].val() )
	# 							self.arr[i3][i2].reset(0)
	# 							#prepare next round
	# 							i3+=1
	# 							nextX =True
	# 						else:
	# 							print("\tAction no taken")
	# 							#nothing happen => cancel
	# 							nextX= False
	# 				i2+=1
	# 			i-=1
	# 	elif val == "right":
    #                     i2=2
    #                     while i2 >= 0:
    #                             i=0
    #                             while i < 4:
    #                                     print("(",i, " , ", i2, ")" , "Check ", self.arr[i][i2].val() )
    #                                     if self.arr[i][i2].val() > 0:
    #                                             i3 = i2
    #                                             nextX = True
    #                                             while i3 < 3 and nextX:
    #                                                     if self.arr[i][i3+1].val() == self.arr[i][i3].val():
    #                                                             print("Compare: ",self.arr[i][i3+1].val() , " and ", self.arr[i][i3].val())
    #                                                             #increase i3-1
    #                                                             self.arr[i][i3+1].incr(self.arr[i][i3].val())
    #                                                             #increase score
    #                                                             self.new_score(self.arr[i][i3+1].val())
    #                                                             #replace i3 with 0
    #                                                             self.arr[i][i3].reset(0)
    #                                                             #decrease space
    #                                                             self.spaceD()
    #                                                             #No new round
    #                                                             nextX = False
    #                                                             i3+=1
    #                                                     elif self.arr[i][i3+1].val() == 0:
    #                                                             print("\t Interchange happen" )
    #                                                             #interchangee values
    #                                                             self.arr[i][i3+1].reset( self.arr[i][i3].val() )
    #                                                             self.arr[i][i3].reset(0)

    #                                                             #prepare next round
    #                                                             i3+=1
    #                                                             nextX =True
    #                                                     else:
    #                                                             print("\tAction no taken")
    #                                                             #nothing happen => cancel
    #                                                             nextX = False

                                                                
                                                        
    #                                     i+=1
    #                             i2-=1
	# 	elif val == "left":
    #                     i2=1
    #                     while i2 < 4:
    #                             i=0
    #                             while i < 4:
    #                                     print("(",i, " , ", i2, ")" , "Check ", self.arr[i][i2].val() )
    #                                     if self.arr[i][i2].val() > 0:
    #                                             i3 = i2
    #                                             nextX = True
    #                                             while i3 >0 and nextX:
    #                                                     if self.arr[i][i3-1].val() == self.arr[i][i3].val():
    #                                                             print("Compare: ",self.arr[i][i3-1].val() , " and ", self.arr[i][i3].val())
    #                                                             #increase i3-1
    #                                                             self.arr[i][i3-1].incr(self.arr[i][i3].val())
    #                                                             #increase score
    #                                                             self.new_score(self.arr[i][i3-1].val())
    #                                                             #replace i3 with 0
    #                                                             self.arr[i][i3].reset(0)
    #                                                             #decrease space
    #                                                             self.spaceD()
    #                                                             #No new round
    #                                                             nextX = False
    #                                                             i3-=1
    #                                                     elif self.arr[i][i3-1].val() == 0:
    #                                                             print("\t Interchange happen" )
    #                                                             #interchangee values
    #                                                             self.arr[i][i3-1].reset( self.arr[i][i3].val() )
    #                                                             self.arr[i][i3].reset(0)

    #                                                             #prepare next round
    #                                                             i3-=1
    #                                                             nextX =True
    #                                                     else:
    #                                                             print("\tAction no taken")
    #                                                             #nothing happen => cancel
    #                                                             nextX = False

                                                                
                                                        
    #                                     i+=1
    #                             i2+=1
		


# print("=======================================================================")
# print("======================PRINT EXTRA TEST=================================")
# print("=======================================================================")

# ballon = Arr_block()
# ballon.length()
# arrX = [[2,2,2,2],[2,2,2,4],[0,0,0,0],[0,0,0,4]]
# ballon.cheap_2048(arrX)
# ballon.illustrate()
# ballon.new_move("up")
# print()
# print()
# ballon.illustrate()

# ballon = Arr_block()
# ballon.length()
# arrX = arrX = [[0,0,0,0],[4,8,4,4],[2,0,0,2],[0,0,0,0]]
# ballon.cheap_2048(arrX)
# ballon.illustrate()
# ballon.new_move("left")
# print()
# print()
# ballon.illustrate()
		






