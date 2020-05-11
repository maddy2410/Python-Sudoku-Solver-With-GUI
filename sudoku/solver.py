# board = [
#     [7,8,0,4,0,0,1,2,0],
#     [6,0,0,0,7,5,0,0,9],
#     [0,0,0,6,0,1,0,7,8],
#     [0,0,7,0,4,0,2,6,0],
#     [0,0,1,0,5,0,9,3,0],
#     [9,0,4,0,6,0,0,0,5],
#     [0,7,0,3,0,0,0,1,2],
#     [1,2,0,0,0,7,4,0,0],
#     [0,4,9,2,0,6,0,0,7]
# ]





from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType


sudokugui,_=loadUiType('sudokugui.ui')


class gui(QMainWindow,sudokugui):

	def __init__(self):
		QMainWindow.__init__(self)
		self.setupUi(self)
		self.val=True
		self.handleButton()


	def handleButton(self):
		self.pushButton.clicked.connect(self.solver_in)


	def set_board(self):
		self.board = [

		[int(self.l11.text()),int(self.l12.text()),int(self.l13.text()),int(self.l14.text()),int(self.l15.text()),int(self.l16.text()),int(self.l17.text()),int(self.l18.text()),int(self.l19.text())],

		[int(self.l21.text()),int(self.l22.text()),int(self.l23.text()),int(self.l24.text()),int(self.l25.text()),int(self.l26.text()),int(self.l27.text()),int(self.l28.text()),int(self.l29.text())],

		[int(self.l31.text()),int(self.l32.text()),int(self.l33.text()),int(self.l34.text()),int(self.l35.text()),int(self.l36.text()),int(self.l37.text()),int(self.l38.text()),int(self.l39.text())],

		[int(self.l41.text()),int(self.l42.text()),int(self.l43.text()),int(self.l44.text()),int(self.l45.text()),int(self.l46.text()),int(self.l47.text()),int(self.l48.text()),int(self.l49.text())],

		[int(self.l51.text()),int(self.l52.text()),int(self.l53.text()),int(self.l54.text()),int(self.l55.text()),int(self.l56.text()),int(self.l57.text()),int(self.l58.text()),int(self.l59.text())],

		[int(self.l61.text()),int(self.l62.text()),int(self.l63.text()),int(self.l64.text()),int(self.l65.text()),int(self.l66.text()),int(self.l67.text()),int(self.l68.text()),int(self.l69.text())],

		[int(self.l71.text()),int(self.l72.text()),int(self.l73.text()),int(self.l74.text()),int(self.l75.text()),int(self.l76.text()),int(self.l77.text()),int(self.l78.text()),int(self.l79.text())],

		[int(self.l81.text()),int(self.l82.text()),int(self.l83.text()),int(self.l84.text()),int(self.l85.text()),int(self.l86.text()),int(self.l87.text()),int(self.l88.text()),int(self.l89.text())],

		[int(self.l91.text()),int(self.l92.text()),int(self.l93.text()),int(self.l94.text()),int(self.l95.text()),int(self.l96.text()),int(self.l97.text()),int(self.l98.text()),int(self.l99.text())]


		]



	



	def print_board(self,bo):

		print('\n\n')
		for i in range(len(bo)):

			if i%3 == 0:
				print("--- "*7)


			for j in range(len(bo[i])):

				if j%3 == 0 and j!=0:
					print(" || ",end="")

				print(bo[i][j],end=" ")

			print('')
		print('\n\n')


	def show_board(self,fa):

		self.l11.setText(str(fa[0][0]))

		self.l12.setText(str(fa[0][1]))

		self.l13.setText(str(fa[0][2]))

		self.l14.setText(str(fa[0][3]))

		self.l15.setText(str(fa[0][4]))

		self.l16.setText(str(fa[0][5]))

		self.l17.setText(str(fa[0][6]))

		self.l18.setText(str(fa[0][7]))

		self.l19.setText(str(fa[0][8]))



		self.l21.setText(str(fa[1][0]))

		self.l22.setText(str(fa[1][1]))

		self.l23.setText(str(fa[1][2]))

		self.l24.setText(str(fa[1][3]))

		self.l25.setText(str(fa[1][4]))

		self.l26.setText(str(fa[1][5]))

		self.l27.setText(str(fa[1][6]))

		self.l28.setText(str(fa[1][7]))

		self.l29.setText(str(fa[1][8]))



		self.l31.setText(str(fa[2][0]))

		self.l32.setText(str(fa[2][1]))

		self.l33.setText(str(fa[2][2]))

		self.l34.setText(str(fa[2][3]))

		self.l35.setText(str(fa[2][4]))

		self.l36.setText(str(fa[2][5]))

		self.l37.setText(str(fa[2][6]))

		self.l38.setText(str(fa[2][7]))

		self.l39.setText(str(fa[2][8]))


		self.l41.setText(str(fa[3][0]))

		self.l42.setText(str(fa[3][1]))

		self.l43.setText(str(fa[3][2]))

		self.l44.setText(str(fa[3][3]))

		self.l45.setText(str(fa[3][4]))

		self.l46.setText(str(fa[3][5]))

		self.l47.setText(str(fa[3][6]))

		self.l48.setText(str(fa[3][7]))

		self.l49.setText(str(fa[3][8]))


		self.l51.setText(str(fa[4][0]))

		self.l52.setText(str(fa[4][1]))

		self.l53.setText(str(fa[4][2]))

		self.l54.setText(str(fa[4][3]))

		self.l55.setText(str(fa[4][4]))

		self.l56.setText(str(fa[4][5]))

		self.l57.setText(str(fa[4][6]))

		self.l58.setText(str(fa[4][7]))

		self.l59.setText(str(fa[4][8]))



		self.l61.setText(str(fa[5][0]))

		self.l62.setText(str(fa[5][1]))

		self.l63.setText(str(fa[5][2]))

		self.l64.setText(str(fa[5][3]))

		self.l65.setText(str(fa[5][4]))

		self.l66.setText(str(fa[5][5]))

		self.l67.setText(str(fa[5][6]))

		self.l68.setText(str(fa[5][7]))

		self.l69.setText(str(fa[5][8]))



		self.l71.setText(str(fa[6][0]))

		self.l72.setText(str(fa[6][1]))

		self.l73.setText(str(fa[6][2]))

		self.l74.setText(str(fa[6][3]))

		self.l75.setText(str(fa[6][4]))

		self.l76.setText(str(fa[6][5]))

		self.l77.setText(str(fa[6][6]))

		self.l78.setText(str(fa[6][7]))

		self.l79.setText(str(fa[6][8]))



		self.l81.setText(str(fa[7][0]))

		self.l82.setText(str(fa[7][1]))

		self.l83.setText(str(fa[7][2]))

		self.l84.setText(str(fa[7][3]))

		self.l85.setText(str(fa[7][4]))

		self.l86.setText(str(fa[7][5]))

		self.l87.setText(str(fa[7][6]))

		self.l88.setText(str(fa[7][7]))

		self.l89.setText(str(fa[7][8]))



		self.l91.setText(str(fa[8][0]))

		self.l92.setText(str(fa[8][1]))

		self.l93.setText(str(fa[8][2]))

		self.l94.setText(str(fa[8][3]))

		self.l95.setText(str(fa[8][4]))

		self.l96.setText(str(fa[8][5]))

		self.l97.setText(str(fa[8][6]))

		self.l98.setText(str(fa[8][7]))

		self.l99.setText(str(fa[8][8]))




	def checker(self,n,i,j):

		for m in range(9):
			if self.board[m][j] == n:
				return False
			if self.board[i][m] == n:
				return False

		k=i//3
		l=j//3

		for t in range(k*3,k*3+3):
			for g in range(l*3,l*3+3):
				if self.board[t][g]==n:
					return False

				
		return True


	def next_empty(self):

		for k in range(9):
			for t in range(9):
				if self.board[k][t] == 0:
					return (k,t)
		return (9,9)


	def solver(self,i,j):
		#self.show_board(self.board)
		#self.print_board(self.board)
		for num in range(1,10):

			if self.checker(num,i,j):
				self.board[i][j]=num
				
				_i,_j = self.next_empty()
				if _i != 9 and _j != 9:
					self.solver(_i,_j)

				else:
					if self.val:
						self.finalizedans=self.board
						self.print_board(self.finalizedans)
						self.show_board(self.board)
						val=False
					return

		self.board[i][j]=0
		return


	def solver_in(self):
		
		self.set_board()
		print(self.board)
		self.ni,self.mi=self.next_empty()
		print(self.ni,self.mi)
		self.solver(self.ni,self.mi)





def main():
	app=QApplication(sys.argv)
	window=gui()

	window.show()
	app.exec_()


if __name__ == '__main__':
	main()