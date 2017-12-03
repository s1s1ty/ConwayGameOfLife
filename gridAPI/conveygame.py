import copy

"""

1 1 1
0 1 0
1 0 0

"""


class ConveyGameLife(object):
	""" Implementation of comway game of life """
	def __init__(self, am, row, col):
		self.am = am
		self.r = row
		self.c = col
		# self.modify_am = copy.copy(am)
		self.modify_am = [[1,1,1],[0,1,0],[1,0,0]] # bcz of python deep and sallow copy

	def state_check(self):
		for i in range(self.r):
			for j in range(self.c):
				live = 0
				for k in range(-1,2,1):
					for kk in range(-1,2,1):
						if(i+k>=0 and i+k<self.r and j+kk>=0 and j+kk<self.c):

							live+=self.am[i+k][j+kk] # count neighbouring 1

				if self.am[i][j]==1:
					live-=1 # as same element is not countable
					if live==2 or live==3:
						self.modify_am[i][j]=1
					else:
						self.modify_am[i][j]=0
				if self.am[i][j]==0:
					if live==3:
						self.modify_am[i][j]=1

		return self.modify_am

