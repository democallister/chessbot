from chess_player import ChessPlayer
import random
from copy import deepcopy

class dmcallis_ChessPlayer(ChessPlayer):

	def __init__(self, board, color):
		super().__init__(board, color)
		if self.color == 'black':
			self.friends = {'p', 'k', 'q', 'r', 'n', 'b', 'f', 's'}
			self.foes = {'P', 'K', 'Q', 'R', 'N', 'B', 'F', 'S'}
			self.foecolor = 'white'
		elif self.color == 'white':
			self.friends = {'P', 'K', 'Q', 'R', 'N', 'B', 'F', 'S'}
			self.foes = {'p', 'k', 'q', 'r', 'n', 'b', 'f', 's'}
			self.foecolor = 'black'

	def get_move(self, your_remaining_time, opp_remaining_time, prog_stuff):
		movelist = self.board.get_all_available_legal_moves(self.color)
		enemoves = self.board.get_all_available_legal_moves(self.foecolor)
		checkmoves = []
		checkmoves.clear()
		killmoves = []
		killmoves.clear()
		safemoves = []
		safemoves.clear()
		for m in movelist:
			try:
				planboard = deepcopy(self.board)
				planboard.make_move(m[0],m[1])
				if planboard.is_king_in_checkmate(self.foecolor) == True:
					return m
				if planboard.is_king_in_check(self.foecolor) == True:
					checkmoves.append(m)
					for e in enemoves:
						if e[1] == m[1]:
							checkmoves.remove(m)
			except:
				pass
		for i in movelist:
			try:
				if self.board[i[1]].get_notation() in self.foes:
					killmoves.append(i)
					
			except:
				pass
		for e in enemoves:
			try:
				if self.board[e[1]].get_notation() in self.friends:
					for ee in movelist:
						if ee[0] == e[1]:
							safemoves.append(ee)
			except KeyError:
				pass
		if len(checkmoves) > 0:
			return random.choice(checkmoves)
		elif len(killmoves) > 0:
			return random.choice(killmoves)
		elif len(safemoves) > 0:
			return random.choice(safemoves)
		elif len(movelist) > 0:

			return random.choice(movelist)
		else:
			return random.choice(self.board.get_all_available_legal_moves(self.color))

