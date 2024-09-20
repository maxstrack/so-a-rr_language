import sys
import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QGraphicsScene
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt

from aliasDict import AliasDict

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()
		uic.loadUi('../mainwindow.ui', self)  # Load the .ui file
		self.initVariables()
		
		# Connect the textChanged signal to the slot
		self.engOut.textChanged.connect(self.on_engOut_textChanged)

	def initVariables(self):
		a = QPixmap("../../letters/a.png")
		eh = QPixmap("../../letters/eh.png")
		f = QPixmap("../../letters/f.png")
		i = QPixmap("../../letters/i.png")
		k = QPixmap("../../letters/k.png")
		l = QPixmap("../../letters/l.png")
		h = QPixmap("../../letters/m.png")
		n = QPixmap("../../letters/n.png")
		o = QPixmap("../../letters/o.png")
		rr = QPixmap("../../letters/rr.png")
		d = QPixmap("../../letters/s.png")
		sh = QPixmap("../../letters/sh.png")
		t = QPixmap("../../letters/t.png")
		th = QPixmap("../../letters/th.png")
		uh = QPixmap("../../letters/uh.png")
		v = QPixmap("../../letters/v.png")
		z = QPixmap("../../letters/z.png")
		print("a  exists: ",os.path.exists("../../letters/a.png"))
		print("eh exists: ",os.path.exists("../../letters/eh.png"))
		print("f  exists: ",os.path.exists("../../letters/f.png"))
		print("i  exists: ",os.path.exists("../../letters/i.png"))
		print("k  exists: ",os.path.exists("../../letters/k.png"))
		print("l  exists: ",os.path.exists("../../letters/l.png"))
		print("h  exists: ",os.path.exists("../../letters/m.png"))
		print("n  exists: ",os.path.exists("../../letters/n.png"))
		print("o  exists: ",os.path.exists("../../letters/o.png"))
		print("rr exists: ",os.path.exists("../../letters/rr.png"))
		print("d  exists: ",os.path.exists("../../letters/s.png"))
		print("sh exists: ",os.path.exists("../../letters/sh.png"))
		print("t  exists: ",os.path.exists("../../letters/t.png"))
		print("th exists: ",os.path.exists("../../letters/th.png"))
		print("uh exists: ",os.path.exists("../../letters/uh.png"))
		print("v  exists: ",os.path.exists("../../letters/v.png"))



		#self.english = ['e', 't', 'a',  'o', 'i',	'n',  's','h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f',	'g']
		#self.zentil =	["a-","z-","eh-","i-","uh-","rr-","f-","n-","h-","v-","t-","l-","o-","th-","k-","sh-","d-"]
		#self.pixmaps = [ a,   z,	eh,   i,   uh,	 rr,   f,	n,	 h,   v,   t,	l,	 o,   th,	k,	 sh,   d]
		initialData = {
		# consonants
			('d', 'dd', 'ed')								: ('v-',),  # /d/ sound
			('k', 'c', 'qu', 'ck', 'lk', 'q')				: ('s-',),  # /k/ sound
			('l', 'll', 'b', 'bb')							: ('t-',),  # /l/,/b/ sound
			('n', 'nn', 'kn', 'gn', 'pn')					: ('rr-',),  # /n/ sound
			('r', 'rr', 'wr', 'rh')							: ('l-',),  # /r/ sound
			('s', 'ce', 'se', 'sc', 'ps', 'st')				: ('f-',),  # /s/ sound
			('t', 'tt', 'p', 'pp')							: ('z-',),  # /t/,/p/ sound
			('z', 'se', 'ss', 'ze')							: ('ch-',),  # /z/ sound
			('v', 'ph', 've')								: ('k-',),  # /v/ sound
		# digraphs
			('j', 'ge', 'dge', 'di', 'gg')					: ('zh-',),  # /j/ sound
			('ch', 'tch', 'tu','te')						: ('d-',),  # /ch/ sound
			('sh', 'sci', 'ti', 'ci')						: ('n-',),  # /sh/ sound
			('th')											: ('KH-',),  # /th/ sound (feather)
			('f', 'ff', 'gh', 'lf', 'ft')					: ('sh-',),  # /f/ sound
			('w', 'wh', 'h','m', 'mm', 'mb', 'mn', 'lm')	: ('th-',),  # /w/,/m/,/h/ sound
			('ng', 'ngue', 'g', 'gg', 'gh', 'gue', 'gu')	: ('w-',),  # /ng/,/g/ sound
		# vowels
			('a', 'ai', 'ea', 'u', 'ie')					: ('e-',),  # /a/ sound (short a)
			('e', 'eo', 'ei', 'ae', 'ay', 'a')				: ('a-',),  # /e/ sound
			('i', 'ie', 'u', 'ui')							: ('u-',),  # /i/ sound
			('o', 'ho', 'y')								: ('i-',),  # /o/,/y/ sound
			('u')											: ('oo-',),  # /u/ sound
			('oo', 'ou')									: ('ah-',),  # /oo/ sound (short oo)
		#long_vowels
			('ai', 'eigh', 'ay', 'a-e')						: ('ie-',),  # /ā/ sound
			('ea', 'ee', 'ie', 'ei', 'y')					: ('ay-',),  # /ē/ sound
			('igh', 'i-e')									: ('ew-',),  # /ī/ sound
			('oa', 'o-e', 'ow')								: ('ī-',),  # /ō/ sound
			('ew')											: ('oy-',),  # /ü/ sound
			('oi', 'oy', 'uoy')								: ('ow-',),  # /oi/ sound
		#special chars
			' '	: (' ',),												
		}
		self.convertDict = AliasDict(initialData)

	def on_engOut_textChanged(self):
		self.convert()

	def convert(self):
		engWord = self.engOut.toPlainText().lower()
		engSen = []
		zenWord = ""
		convertedList = self.convertDict.convertString(engWord)
		for pair in convertedList:
			zenWord += pair[0]
			

		self.zenOut.setText(zenWord)

		'''
		if self.graphicsView.scene():
			self.graphicsView.scene().clear()
		if engSen:
			self.letterDisplay(engSen)

	def letterDisplay(self, eng):
		# Emplty used for spaces
		empty = QPixmap(self.pixmaps[0].width(), self.pixmaps[0].height())
		empty.fill(Qt.transparent)

		# Set up an empty pixmap to paint the images
		width = 0
		for word in eng:
			for char in word:
				for alph in range(17):
					if char == self.english[alph]:
						width += self.pixmaps[alph].width() - 2
			width += self.pixmaps[0].width()

		disp = QPixmap(width, self.pixmaps[0].height())
		disp.fill(Qt.transparent)
		if disp.isNull():
			print("Error: Disp QPixmap is null!")
			return

		painter = QPainter()
		if not painter.begin(disp):
			print("Failed to initialize QPainter")
			return

		# Paint the proper images based on the english list
		width = 0
		for word in eng:
			for char in word:
				for alph in range(17):
					if char == self.english[alph]:
						# The lists are kept in order so the index is used to find the letter
						painter.drawPixmap(width, 0, self.pixmaps[alph])
						width += self.pixmaps[alph].width() - 2
			# Space
			painter.drawPixmap(width, 0, empty)
			width += empty.width()
		painter.end()  # Ensure this is called to finish painting

		if not self.graphicsView.scene():
			scene = QGraphicsScene(self)
			self.graphicsView.setScene(scene)

		self.graphicsView.scene().addPixmap(disp.scaled(disp.width() // 2, disp.height() // 2))
			'''

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	ui = UI()
	ui.show()
	sys.exit(app.exec_())
