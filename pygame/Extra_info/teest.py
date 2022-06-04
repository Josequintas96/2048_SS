import unittest
from logicT import * 


class TestStringMeethods(unittest.TestCase):
	def test_upper(self):
		self.assertEqual('fgo'.upper(), 'FGO')
	def test_lower(self):
		self.assertEqual('FGO'.lower(), 'fgo')

class TestImportMethods(unittest.TestCase):
    
	# def test_array_illustratiion(self):
	# 	gameX2 = Arr_block()
	# 	#print("Print the arrayillustratioon ", gameX2.array_illustration())
	# 	self.assertEqual(gameX2.array_illustration(), [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] )

	def test_importTT(self):
		#print("Hello")
		self.assertEqual(preTest(9), 90)

	def test_InitialScore(self):
		gameX = Arr_block()
		self.assertEqual(gameX.ret_score(), 0)
	def test_first_round(self):
		gameX = Arr_block()
		gameX.new_round()
		self.assertEqual(gameX.ret_score(), 2)
	def test_false_score(self):
		gameX = Arr_block()
		gameX.false_score(9999)
		self.assertEqual(gameX.ret_score(), 9999)

	def test_highspace(self):
		gameX = Arr_block()
		arrX = [[0,0,0,0],[8,16,32,0],[2,2,2,2],[0,0,0,8]]
		gameX.cheap_2048(arrX)
		gameX.array_illustration()
		self.assertEqual(gameX.ret_highspace(), [1,2] )
	
	def test_highspaceV(self):
		gameX = Arr_block()
		arrX = [[0,0,0,0],[8,16,32,0],[2,2,2,2],[64,0,0,8]]
		gameX.cheap_2048(arrX)
		gameX.array_illustration()
		self.assertEqual(gameX.ret_highspace_V(), 64 )

	def test_highspaceT(self):
		gameX = Arr_block()
		arrX = [[0,0,0,0],[8,16,32,0],[2,2,2,2],[64,0,0,8]]
		gameX.cheap_2048(arrX)
		gameX.array_illustration()
		self.assertEqual(gameX.ret_highspace_T(), True )

	def test_length(self):
		gameX = Arr_block()
		self.assertEqual(gameX.return_length(), [4,4] )

	def test_cheap_2048(self):
		gameX = Arr_block()
		arrX = [[0,0,0,0],[8,16,32,0],[2,2,2,2],[0,0,0,8]]
		gameX.cheap_2048(arrX)
		self.assertEqual(gameX.array_illustration(), [[0,0,0,0],[8,16,32,0],[2,2,2,2],[0,0,0,8]] )

	def test_duper_test(self):
		gameX = Arr_block()
		arrX = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
		gameX.cheap_2048(arrX)
		# gameX2.illustrate()
		gameX.new_round()
		# gameX2.illustrate()
		gameX.new_round()
		# gameX2.illustrate()
		gameX.new_move("down")
		gameX.new_move("left")
		arrX2 = gameX.array_illustration()
		self.assertEqual(arrX2, [[0,0,0,0],[0,0,0,0],[0,0,0,0],[4,0,0,0]])

	def test_hard_reset(self):
		gameX = Arr_block()
		arrX = [[32,16,8,2],[32,16,8,2],[32,16,8,4],[2,2,2,0]]
		gameX.reset_2048()
		arrX2 = gameX.array_illustration()
		self.assertEqual(arrX2, [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])

	def test_restore_stage(self):
		gameX = Arr_block()
		arrX = [[2,2,2,2],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
		gameX.cheap_2048(arrX)
		gameX.new_move("down")
		gameX.restore_stage()
		arrX2 = gameX.array_illustration()
		self.assertEqual(arrX2, arrX)

	def test_restore_stage2(self):
		gameX = Arr_block()
		gameX.reset_2048()
		gameX.new_round()
		valX = False
		if gameX.new_move("down") == True:
			if gameX.new_move("left") == True:
				valX =True
		elif gameX.new_move("left") == True:
			valX =True
		gameX.restore_stage()
		self.assertEqual(gameX.ret_score(), 2)

	def test_restore_stage3(self):
		gameX = Arr_block()
		arrX = [[2,2,2,2],[0,0,0,0],[0,0,0,0],[8,0,0,0]]
		gameX.cheap_2048(arrX)
		gameX.set_current_stage()
		arrX3 = [[2,2,2,2],[0,64,0,0],[128,0,0,0],[8,0,0,0]]
		gameX.cheap_2048(arrX3)
		gameX.restore_stage()
		arrX2 = gameX.array_illustration()
		self.assertEqual(arrX2, arrX)


	


	def test_movement(self):
		gameX = Arr_block()
		arrX = [[0,0,0,4],[0,0,0,4],[0,0,0,0],[0,0,0,4]]
		gameX.cheap_2048(arrX)
		gameX.new_move("up")
		arrX2 = gameX.array_illustration()
		self.assertEqual(arrX2, [[0,0,0,8],[0,0,0,4],[0,0,0,0],[0,0,0,0]])

	def test_movement2(self):
		gameX = Arr_block()
		arrX = [[2,2,2,2],[2,2,2,4],[0,0,0,0],[0,0,0,4]]
		gameX.cheap_2048(arrX)
		gameX.new_move("up")
		arrX2 = gameX.array_illustration()
		self.assertEqual(arrX2, [[4,4,4,2],[0,0,0,8],[0,0,0,0],[0,0,0,0]])

	def test_movement3(self):
		gameX = Arr_block()
		arrX = [[0,0,0,0],[0,0,2,0],[0,0,0,0],[0,0,0,0]]
		gameX.cheap_2048(arrX)
		gameX.new_move("down")
		arrX2 = gameX.array_illustration()
		self.assertEqual(arrX2, [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,2,0]])

	def test_movement4(self):
		gameX = Arr_block()
		arrX = [[0,0,0,0],[0,0,2,4],[2,16,0,0],[0,0,0,0]]
		gameX.cheap_2048(arrX)
		gameX.new_move("down")
		arrX2 = gameX.array_illustration()
		self.assertEqual(arrX2, [[0,0,0,0],[0,0,0,0],[0,0,0,0],[2,16,2,4]])

	def test_movement5(self):
		gameX = Arr_block()
		arrX = [[0,0,0,0],[0,0,2,4],[2,16,0,0],[0,0,0,0]]
		gameX.cheap_2048(arrX)
		gameX.new_move("down")
		gameX.new_move("up")
		arrX2 = gameX.array_illustration()
		self.assertEqual(arrX2, [[2,16,2,4],[0,0,0,0],[0,0,0,0],[0,0,0,0]])

	def test_movement6(self):
		gameX = Arr_block()
		arrX = [[0,0,0,0],[0,0,2,4],[2,16,0,0],[0,0,0,0]]
		gameX.cheap_2048(arrX)
		gameX.new_move("left")
		arrX2 = gameX.array_illustration()
		self.assertEqual(arrX2, [[0,0,0,0],[2,4,0,0],[2,16,0,0],[0,0,0,0]])

	def test_movement7(self):
		gameX = Arr_block()
		gameX.reset_2048()
		gameX.new_round()
		valX = False
		if gameX.new_move("down") == True:
			if gameX.new_move("left") == True:
				valX =True
		elif gameX.new_move("left") == True:
			valX =True
		arrX2 = gameX.array_illustration()
		self.assertEqual(arrX2, [[0,0,0,0],[0,0,0,0],[0,0,0,0],[2,0,0,0]])

	def test_movement8(self):
		gameX = Arr_block()
		gameX.reset_2048()
		arrX = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[4,4,4,4]]
		gameX.cheap_2048(arrX)
		gameX.new_move("left")
		gameX.new_move("left")
		arrX2 = gameX.array_illustration()
		self.assertEqual(arrX2, [[0,0,0,0],[0,0,0,0],[0,0,0,0],[16,0,0,0]])	

	def test_movement9(self):
		gameX = Arr_block()
		arrX = [[0,0,0,4],[0,0,0,4],[0,0,0,8],[0,0,0,4]]
		gameX.cheap_2048(arrX)
		gameX.new_move("up")
		arrX2 = gameX.array_illustration()
		self.assertEqual(arrX2, [[0,0,0,8],[0,0,0,8],[0,0,0,4],[0,0,0,0]])

	def test_score2(self):
		gameX = Arr_block()
		gameX.reset_2048()
		arrX = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[4,4,4,4]]
		gameX.cheap_2048(arrX)
		gameX.new_move("left")
		gameX.new_move("left")
		# arrX2 = gameX.array_illustration()
		self.assertEqual(gameX.ret_score(), 32 )

	def test_score3(self):
		gameX = Arr_block()
		gameX.reset_2048()
		arrX = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[4,4,4,4]]
		gameX.cheap_2048(arrX)
		gameX.new_move("left")
		# arrX2 = gameX.array_illustration()
		self.assertEqual(gameX.ret_score(), 16 )

	def test_restort_score(self):
		gameX = Arr_block()
		gameX.reset_2048()
		arrX = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[4,4,4,4]]
		gameX.cheap_2048(arrX)
		gameX.new_move("left")
		gameX.new_move("left")
		gameX.restore_stage()
		# arrX2 = gameX.array_illustration()
		# print("thIS IS A SPECIAL TEST WITH THE SCORE OF: ", gameX.ret_score())
		self.assertEqual(gameX.ret_score(), 16 )	

	def test_Error_movement(self):
		gameX = Arr_block()
		arrX = [[0,0,0,2],[0,0,0,4],[0,0,0,8],[0,0,0,4]]
		gameX.cheap_2048(arrX)
		
		self.assertNotEqual(gameX.new_move("right"), True)


if __name__ == '__main__':
	unittest.main()
