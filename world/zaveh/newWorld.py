import sys
import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QGraphicsScene
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt

from aliasDict import AliasDict

global padding
padding = 2

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()
		uic.loadUi('../mainwindow.ui', self)  # Load the .ui file
		self.initVariables()
		
		# Connect the textChanged signal to the slot
		self.engOut.textChanged.connect(self.on_engOut_textChanged)

	def initVariables(self):
		ah = QPixmap("../../letters/ah.png")
		a = QPixmap("../../letters/a.png")
		d = QPixmap("../../letters/d.png")
		e = QPixmap("../../letters/e.png")
		f = QPixmap("../../letters/f.png")
		i = QPixmap("../../letters/i.png")
		k = QPixmap("../../letters/k.png")
		l = QPixmap("../../letters/l.png")
		n = QPixmap("../../letters/n.png")
		oo = QPixmap("../../letters/oo.png")
		rr = QPixmap("../../letters/rr.png")
		s = QPixmap("../../letters/s.png")
		t = QPixmap("../../letters/t.png")
		u = QPixmap("../../letters/u.png")
		v = QPixmap("../../letters/v.png")
		w = QPixmap("../../letters/w.png")
		z = QPixmap("../../letters/z.png")
		consonant = QPixmap("../../letters/consonant.png")
		KA = QPixmap("../../letters/KA.png")
		space = QPixmap("../../letters/space.png")
		vowle = QPixmap("../../letters/vowle.png")
		print("ah  exists: ",os.path.exists("../../letters/ah.png"))
		print("a exists: ",os.path.exists("../../letters/a.png"))
		print("d  exists: ",os.path.exists("../../letters/s.png"))
		print("e  exists: ",os.path.exists("../../letters/e.png"))
		print("f  exists: ",os.path.exists("../../letters/f.png"))
		print("i  exists: ",os.path.exists("../../letters/i.png"))
		print("k  exists: ",os.path.exists("../../letters/k.png"))
		print("l  exists: ",os.path.exists("../../letters/l.png"))
		print("n  exists: ",os.path.exists("../../letters/n.png"))
		print("oo  exists: ",os.path.exists("../../letters/oo.png"))
		print("rr exists: ",os.path.exists("../../letters/rr.png"))
		print("s exists: ",os.path.exists("../../letters/s.png"))
		print("t  exists: ",os.path.exists("../../letters/t.png"))
		print("u exists: ",os.path.exists("../../letters/u.png"))
		print("v  exists: ",os.path.exists("../../letters/v.png"))
		print("w  exists: ",os.path.exists("../../letters/w.png"))
		print("z  exists: ",os.path.exists("../../letters/z.png"))
		print("consonant  exists: ",os.path.exists("../../letters/consonant.png"))
		print("KA  exists: ",os.path.exists("../../letters/KA.png"))
		print("space  exists: ",os.path.exists("../../letters/space.png"))
		print("vowle  exists: ",os.path.exists("../../letters/vowle.png"))
		consonants = [s, z, t, n, k]
		newC = self.paintNewMaps(consonants, consonant) 
		vowles = [e, a, u, i, oo, ah]
		newV = self.paintNewMaps(vowles, vowle) 
	
		initialData = {
		# consonants
			('k', 'c', 'qu', 'ck', 'lk', 'q')				: ('s-', s),  # /k/ sound
			('t', 'tt', 'p', 'pp')							: ('z-', z),  # /t/,/p/ sound
			('l', 'll', 'b', 'bb')							: ('t-', t),  # /l/,/b/ sound
			('sh', 'sci', 'ti', 'ci')						: ('n-', n),  # /sh/ sound
			('v', 'ph', 've')								: ('k-', k),  # /v/ sound
			('n', 'nn', 'kn', 'gn', 'pn', 'x')				: ('rr-', rr),	# /n/ sound
			('r', 'rr', 'wr', 'rh')							: ('l-', l),  # /r/ sound
			('ch', 'tch', 'tu','te')						: ('d-', d),  # /ch/ sound
			('ng', 'ngue', 'g', 'gg', 'gh', 'gue', 'gu')	: ('w-', w),  # /ng/,/g/ sound
			('s', 'ce', 'se', 'sc', 'ps', 'st')				: ('f-', f),  # /s/ sound
			('d', 'dd', 'ed')								: ('v-', v),  # /d/ sound
		# digraphs
			('f', 'ff', 'gh', 'lf', 'ft')					: ('sh-', newC[0]),  # /f/ sound
			('j', 'ge', 'dge', 'di', 'gg')					: ('zh-', newC[1]),  # /j/ sound
			('m', 'mm', 'mb', 'mn', 'lm')					: ('th-', newC[2]),  # /m/ sound
			('w', 'wh', 'h')								: ('ng-', newC[3]),  # /w/,/h/ sound
			('z', 'se', 'ss', 'ze')							: ('ch-', newC[4]),  # /z/ sound
			('th')											: ('KH-', KA),  # /th/ sound (feather)
		# vowels
			('a', 'ai', 'ea', 'u', 'ie')					: ('e-', e),  # /a/ sound (short a)
			('e', 'eo', 'ei', 'ae', 'ay', 'a')				: ('a-', a),  # /e/ sound
			('i', 'ie', 'u', 'ui')							: ('u-', u),  # /i/ sound
			('o', 'ho', 'y')								: ('i-', i),  # /o/,/y/ sound
			('u')											: ('oo-', oo),	# /u/ sound
			('oo', 'ou')									: ('ah-', ah),	# /oo/ sound (short oo)
		#long_vowels
			('ai', 'eigh', 'ay', 'a-e')						: ('ie-', newV[0]),  # /ā/ sound
			('ea', 'ee', 'ie', 'ei', 'y')					: ('ay-', newV[1]),  # /ē/ sound
			('igh', 'i-e')									: ('ew-', newV[2]),  # /ī/ sound
			('oa', 'o-e', 'ow')								: ('ī-', newV[3]),	# /ō/ sound
			('ew')											: ('oy-', newV[4]),  # /ü/ sound
			('oi', 'oy', 'uoy')								: ('ow-', newV[5]),  # /oi/ sound
		#special chars
			' '	: (' ', space),												
		}

		self.convertDict = AliasDict(initialData)

	def paintNewMaps(self, letterList, letterType ):
		newMaps = []
		for pixmap in letterList:
			width = pixmap.width() + letterType.width()
			height = max(pixmap.height(), letterType.height())

			newMap = QPixmap(width, height)
			newMap.fill(Qt.transparent)

			painter = QPainter()
			painter.begin(newMap)
			painter.drawPixmap(0, 0, pixmap)
			width = pixmap.width()
			painter.drawPixmap(width-padding, 0, letterType)

			painter.end()
			newMaps.append(newMap)
		return newMaps

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

		self.letterDisplay(convertedList)

	def letterDisplay(self, convertedList):
		# Set up an empty pixmap to paint the images
		for pair in convertedList:
			if pair[1].isNull():
				print(f"Error: One of the pixmaps is null! Pair: {pair}")
				return

		width = 0
		height = 0
		for pair in convertedList:
			width += pair[1].width()-padding
			height = max(height, pair[1].height())

		disp = QPixmap(width, height)
		disp.fill(Qt.transparent)
		#print(f"Final width: {width}, height: {height}")

		if disp.isNull():
			print("Error: Disp QPixmap is null!")
			return

		painter = QPainter()
		if not painter.begin(disp):
			print("Failed to initialize QPainter")
			return

		# Paint the proper images
		width = 0
		for pair in convertedList:
			painter.drawPixmap(width, 0, pair[1])
			width += pair[1].width()-padding

		painter.end()  # Ensure this is called to finish painting

		if not self.graphicsView.scene():
			scene = QGraphicsScene(self)
			self.graphicsView.setScene(scene)
		else:
			self.graphicsView.scene().clear()
			
		self.graphicsView.scene().addPixmap(disp.scaled(disp.width() // 2, disp.height() // 2))

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	ui = UI()
	ui.show()
	sys.exit(app.exec_())
