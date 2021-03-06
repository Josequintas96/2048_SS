import cv2
import matplotlib.pyplot as plt
import keyboard

from random import seed
from random import randint


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
	space =0
	def __init__(self):
		#print("Initialize happen")
		i=0
		while i < 4:
			arr2 = []
			i2 = 0
			while i2 < 4:
				x = Block()
				arr2.append(x)
				i2 += 1
			i+=1
			self.arr.append(arr2)
		#print("Block has initialize: " , len(self.arr) )

	def spaceX(self):
		return self.space
	def spaceI(self):
		self.space+=1
	def spaceD(self):
		self.space-=1
	def scoreX(self):
		print("Score: ", self.score)
	def new_score(self, val):
		self.score+=val

	def illustrate(self):
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
		ocurrence = False
		while True:
			xa = keyboard.read_key()      
			if xa == "down":
				print("\tSpecial key => down")
				ocurrence = self.new_move(xa)
				xa = keyboard.read_key()
				break
			elif xa == "right":
				print("\tSpecial Key =>  right")
				ocurrence = self.new_move(xa)
				xa = keyboard.read_key()
				break
			elif xa == "left":
				print("\tSpecial Key =>left")
				ocurrence = self.new_move(xa)
				xa = keyboard.read_key()
				break
			elif xa == "up":
				print("\tSpecial Key => up")
				ocurrence = self.new_move(xa)
				xa = keyboard.read_key()
				break
			else:
				print("\tKey pressed: ", xa)
		print("THERE IS AN OCCUREENCE ", ocurrence)
		return ocurrence

	def new_move(self, val):
		print("\tDouble Special key is ", val)
		occurence = False
		if val == "up":
			#print("Running right")
			i=1
			while i < 4:
				i2 = 0
				while i2 < 4:
					print("(",i, " , ", i2, ")" , "Check ", self.arr[i][i2].val() )
					if self.arr[i][i2].val() > 0:
						i3 = i
						nextX = True
						while i3 > 0 and nextX:
							print("\t Something must be done")
							if self.arr[i3][i2].val() == self.arr[i3-1][i2].val() :
								print("Compare: ",self.arr[i3][i2] , " and ", self.arr[i3-1][i2] )
								#increase i3-1
								self.arr[i3-1][i2].incr(self.arr[i3][i2].val())

								#increase score
								self.new_score(self.arr[i3-1][i2].val())

								#replace i3 with 0
								self.arr[i3][i2].reset(0)

								#decrease space
								self.spaceD()

								#No new round
								nextX = False
								i3-=1

								#there iis action
								occurence = True
							elif self.arr[i3-1][i2].val() == 0:
								print("\t Interchange happen" )
								#interchangee values
								self.arr[i3-1][i2].reset( self.arr[i3][i2].val() ) 
								self.arr[i3][i2].reset(0)

								#prepare next round
								i3-=1
								nextX =True
								#there is action
								occurence = True
							else:
								print("\tAction no taken")
								#nothing happen => cancel
								nextX= False
					i2+=1
				i+=1
		elif val == "down":
			#print("Running right")
			i=2
			while i >= 0:
				i2 = 0
				while i2 < 4:
					print("(",i, " , ", i2, ")" , "Check ", self.arr[i][i2].val() )
					if self.arr[i][i2].val() > 0:
						i3 = i
						nextX = True
						while i3 < 3 and nextX:
							if self.arr[i3][i2].val() == self.arr[i3+1][i2].val() :
								print("Compare: ",self.arr[i3][i2] , " and ", self.arr[i3-1][i2] )
								#increase i3+1
								self.arr[i3+1][i2].incr(self.arr[i3][i2].val())
								#increase score
								self.new_score(self.arr[i3+1][i2].val())

								#replace i3 with 0
								self.arr[i3][i2].reset(0)
								#decrease space
								self.spaceD()
								#No new round
								nextX = False
								i3-=1
								#there is action
								occurence = True

							elif self.arr[i3+1][i2].val() == 0:
								print("\t Interchange happen" )
								#interchangee values
								self.arr[i3+1][i2].reset( self.arr[i3][i2].val() )
								self.arr[i3][i2].reset(0)
								#prepare next round
								i3+=1
								nextX =True
								#there is action
								occurence = True
							else:
								print("\tAction no taken")
								#nothing happen => cancel
								nextX= False
					i2+=1
				i-=1
		elif val == "right":
                        i2=2
                        while i2 >= 0:
                                i=0
                                while i < 4:
                                        print("(",i, " , ", i2, ")" , "Check ", self.arr[i][i2].val() )
                                        if self.arr[i][i2].val() > 0:
                                                i3 = i2
                                                nextX = True
                                                while i3 < 3 and nextX:
                                                        if self.arr[i][i3+1].val() == self.arr[i][i3].val():
                                                                print("Compare: ",self.arr[i][i3+1] , " and ", self.arr[i][i3])
                                                                #increase i3-1
                                                                self.arr[i][i3+1].incr(self.arr[i][i3].val())
                                                                #increase score
                                                                self.new_score(self.arr[i][i3+1].val())
                                                                #replace i3 with 0
                                                                self.arr[i][i3].reset(0)
                                                                #decrease space
                                                                self.spaceD()
                                                                #No new round
                                                                nextX = False
                                                                i3+=1
                                                                #there is action
                                                                occurence = True
                                                        elif self.arr[i][i3+1].val() == 0:
                                                                print("\t Interchange happen" )
                                                                #interchangee values
                                                                self.arr[i][i3+1].reset( self.arr[i][i3].val() )
                                                                self.arr[i][i3].reset(0)

                                                                #prepare next round
                                                                i3+=1
                                                                nextX =True
                                                                #there is action
                                                                occurence = True
                                                        else:
                                                                print("\tAction no taken")
                                                                #nothing happen => cancel
                                                                nextX = False

                                                                
                                                        
                                        i+=1
                                i2-=1
		elif val == "left":
			i2=1
			while i2 < 4:
				i=0
				while i < 4:
					print("(",i, " , ", i2, ")" , "Check ", self.arr[i][i2].val() )
					if self.arr[i][i2].val() > 0:
						i3 = i2
						nextX = True
						while i3 >0 and nextX:
							if self.arr[i][i3-1].val() == self.arr[i][i3].val():
                                                                print("Compare: ",self.arr[i][i3-1] , " and ", self.arr[i][i3])
                                                                #increase i3-1
                                                                self.arr[i][i3-1].incr(self.arr[i][i3].val())
                                                                #increase score
                                                                self.new_score(self.arr[i][i3-1].val())
                                                                #replace i3 with 0
                                                                self.arr[i][i3].reset(0)
                                                                #decrease space
                                                                self.spaceD()
                                                                #No new round
                                                                nextX = False
                                                                i3-=1
                                                                #there is action
                                                                occurence = True
							elif self.arr[i][i3-1].val() == 0:
                                                                print("\t Interchange happen" )
                                                                #interchangee values
                                                                self.arr[i][i3-1].reset( self.arr[i][i3].val() )
                                                                self.arr[i][i3].reset(0)

                                                                #prepare next round
                                                                i3-=1
                                                                nextX =True
                                                                #there is action
                                                                occurence = True
							else:
								print("\tAction no taken")
                                                                #nothing happen => cancel
								nextX = False
					i+=1
				i2+=1
		print("NEW ACTION =======> ", occurence)
		return occurence




arr = []
i=0
while i < 4:
	arr2 = []
	i2=0
	while i2 < 4:
		arr2.append(0)
		i2+=1
	arr.append(arr2)
	i+=1

i=0
print("\t", end='')
while i < 4:
	i2=0
	while i2 < 4:
		print(arr[i][i2], "\t", end='')
		i2+=1
	i+=1
	print("\n\t", end='')

print()
print("random =>")
#seed(1)
for _ in range(1):
	valX = randint(0,15)
	loc1 =0
	loc2 =0
	if valX!=0:
		loc1 = int(valX/4)
		loc2 = int(valX%4)
	print(valX, " => ", end='')
	print("Location are: ", loc1, " ", loc2)
	while arr[loc1][loc2] != 0:
		valX = randint(0,15)
		loc1 =0
		loc2 =0
		if valX!=0:
			loc1 = int(valX/4)
			loc2 = int(valX%4)
		print(valX, " => ", end='')
		print("Location are: ", loc1, " ", loc2)
	arr[loc1][loc2] = 2
#	print(valX, " => " )
	i=0
	print("\t\t", end='')
	while i < 4:
		i2=0
		while i2 < 4:
			print(arr[i][i2], "\t", end='')
			i2+=1
		i+=1	
		print("\n\t\t", end='')	
	print()




print()
#seed(1)


#print(random(), random(), random())
#seed(1)
#print(random(),random(), random())
#print()

#name = input("Enter name: ")
#print("Name insert is: " , name)
#print(arr)

#print("=>")

#keyboard.write("python3 logic.py")

print("keyboard")
while False:
	xa = keyboard.read_key()
	if xa == "a":
		print("a is pressed")
		break
	elif xa == "right":
		print("\tSpecial Key pressed =>  right") 
	else:
		print("\tKey pressed: ", xa)
#	keyboard.wait("1")
#	keyboard.write("\n the key '1' waspressed!")

print()

while False:
	#print("Batman")
	key = cv2.waitKey(0) & 0xFF
	print("Super ", key)
	if key == 27:
		quit()
	if key ==0:
		print("up")
	elif key ==1:
		print("down")
	elif key == 2:
		print("left")
	elif key == 3:
		print("right")
	elif key != 255:
		print(key)




print("==================================================")
print("=======================BLOCK======================")
print("==================================================")
print()

game = Arr_block()

game.illustrate()
game.new_round()
game.illustrate()

game.new_action()
game.illustrate()
print()
while game.new_round():
	print("\n New model")
	game.illustrate()
	print("Action")
	while game.new_action() == False:
                print("There is nothing")
                
	print("\n After action")
	game.illustrate()




