import sys
import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QColorDialog
from PyQt5.QtGui import QPixmap, QPainter, QColor, QImage
from PyQt5.QtCore import Qt, QRectF
import numpy as np
import qdarkgraystyle


from aliasDict import AliasDict

global padding
padding = 2

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()
		uic.loadUi('./mainwindow.ui', self)  # Load the .ui file
		self.initVariables()
		
		# Connect the textChanged signal to the slot
		self.engOut.textChanged.connect(self.convert)
		self.allLetters.triggered.connect(lambda: self.engOut.setText("k f t j l m w sh ng z v p n r ch s d h th a ai e ea i igh o oa u ew oo oi b "))
		self.menuSaveImage.triggered.connect(self.savePixmap)
		self.menuEnunciation.triggered.connect(self.changeEnunc)
		self.menuChangeColor.triggered.connect(self.changeImageColor)

	def initVariables(self):
		ah = QPixmap("../letters/oo.png")
		a = QPixmap("../letters/a.png")
		d = QPixmap("../letters/d.png")
		e = QPixmap("../letters/e.png")
		g = QPixmap("../letters/f.png")
		i = QPixmap("../letters/i.png")
		k = QPixmap("../letters/k.png")
		l = QPixmap("../letters/l.png")
		n = QPixmap("../letters/n.png")
		oo = QPixmap("../letters/ah.png")
		rr = QPixmap("../letters/rr.png")
		s = QPixmap("../letters/s.png")
		t = QPixmap("../letters/t.png")
		u = QPixmap("../letters/u.png")
		v = QPixmap("../letters/v.png")
		h = QPixmap("../letters/w.png")
		z = QPixmap("../letters/z.png")
		consonant = QPixmap("../letters/consonant.png")
		KA = QPixmap("../letters/KA.png")
		space = QPixmap("../letters/space.png")
		vowle = QPixmap("../letters/vowle.png")
		print("ah  exists: ",os.path.exists("../letters/ah.png"))
		print("a exists: ",os.path.exists("../letters/a.png"))
		print("d  exists: ",os.path.exists("../letters/s.png"))
		print("e  exists: ",os.path.exists("../letters/e.png"))
		print("f  exists: ",os.path.exists("../letters/f.png"))
		print("i  exists: ",os.path.exists("../letters/i.png"))
		print("k  exists: ",os.path.exists("../letters/k.png"))
		print("l  exists: ",os.path.exists("../letters/l.png"))
		print("n  exists: ",os.path.exists("../letters/n.png"))
		print("oo  exists: ",os.path.exists("../letters/oo.png"))
		print("rr exists: ",os.path.exists("../letters/rr.png"))
		print("s exists: ",os.path.exists("../letters/s.png"))
		print("t  exists: ",os.path.exists("../letters/t.png"))
		print("u exists: ",os.path.exists("../letters/u.png"))
		print("v  exists: ",os.path.exists("../letters/v.png"))
		print("w  exists: ",os.path.exists("../letters/w.png"))
		print("z  exists: ",os.path.exists("../letters/z.png"))
		print("consonant  exists: ",os.path.exists("../letters/consonant.png"))
		print("KA  exists: ",os.path.exists("../letters/KA.png"))
		print("space  exists: ",os.path.exists("../letters/space.png"))
		print("vowle  exists: ",os.path.exists("../letters/vowle.png"))

		# Make Lists of the new consonant and vowle pixmaps
		consonants = [s, n, t, z, k, h, v, g]
		newC = self.paintNewMaps(consonants, consonant) 
		vowles = [e, a, u, i, oo, ah]
		newV = self.paintNewMaps(vowles, vowle) 
	
		initialData = {
		# consonants
			('k', 'c', 'qu', 'ck', 'lk', 'q')				: ('s', s),  # /k/ sound
			('t', 'tt')										: ('n', n),  # /t/ sound
			('l', 'll')										: ('t', t),  # /l/ sound
			('w', 'wh')										: ('z', z),  # /w/,/h/ sound
			('ng', 'ngue', 'g', 'gg', 'gh', 'gue')			: ('k', k),  # /ng/,/g/ sound
			('v', 'ph',)									: ('h', h),  # /v/ sound
			('s', 'sc', 'ps', 'st')							: ('v', v),  # /s/ sound
			('h')											: ('g', g),  # /p/ sound
			('n', 'nn', 'kn', 'gn', 'pn', 'x')				: ('rr', rr),	# /n/ sound
			('r', 'rr', 'wr', 'rh')							: ('l', l),  # /r/ sound
			('ch', 'tch')									: ('d', d),  # /ch/ sound
		# digraphs
			('f', 'ff', 'gh', 'lf', 'ft')					: ('sh', newC[0]),	# /f/ sound
			('j', 'ge', 'dge', 'gg')						: ('ng', newC[1]),	# /j/ sound
			('m', 'mm', 'mb', 'mn', 'lm')					: ('th', newC[2]),	# /m/ sound
			('sh', 'sci')									: ('zh', newC[3]),	# /sh/ sound
			('z', 'se', 'ss', 'ze')							: ('ch', newC[4]),	# /z/ sound
			('p', 'pp')										: ('w', newC[5]),	# /p/ sound
			('d', 'dd', 'ed')								: ('f', newC[6]),  # /d/ sound
			('th')											: ('j', newC[7]),  # /th/ sound
			('b', 'bb')										: ('KH', KA),	# /b/
		# vowels
			('a', 'ea',)									: ('eh', e),  # /a/ sound (short a)
			('e', 'eo', 'ei', 'ae', 'ay', 'a')				: ('a', a),  # /e/ sound
			('i', 'ie', 'ui')								: ('uh', u),  # /i/ sound
			('o', 'ho', 'y')								: ('i', i),  # /o/,/y/ sound
			('u')											: ('ou', oo),	# /u/ sound
			('oo', 'ou')									: ('ah', ah),	# /oo/ sound (short oo)
		#long_vowels
			('ai', 'eigh', 'ay', 'a-e')						: ('ie', newV[0]),	# /ā/ sound
			('ea', 'ee', 'ie', 'ei', 'y')					: ('ay', newV[1]),	# /ē/ sound
			('igh', 'i-e')									: ('ew', newV[2]),	# /ī/ sound
			('oa', 'o-e', 'ow')								: ('ī', newV[3]),	# /ō/ sound
			('ew')											: ('oy', newV[4]),	# /ü/ sound
			('oi', 'oy', 'uoy')								: ('ō', newV[5]),  # /oi/ sound
		#special chars
			' '	: (' ', space),												
			'('	: ('(', space),												
			')'	: (')', space),												
			','	: (',', space),												
		}


		# Make a new Dictionary using AliasDict
		self.convertDict = AliasDict(initialData)

		# bool for Enunciation
		self.enuncBool = True

		# Color for letter font
		self.color = QColor("white")

	# Makes the new Maps by adding a letter and Diacrit
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

	# changes the enuncBool and re-calls convert
	# Effectivly changing the setting
	def changeEnunc(self):
			self.enuncBool = not self.enuncBool
			self.convert()

	# Replace the non-transparent pixels with a color
	def replaceImageColor(self, pixmap):
		image = pixmap.toImage()
		image = image.convertToFormat(QImage.Format_RGBA8888)
		width = image.width()
		height = image.height()

		red = self.color.red()
		green = self.color.green()
		blue = self.color.blue()
	
		# Get the image as a buffer of bytes
		ptr = image.bits()
		ptr.setsize(width * height * 4)
	
		# Convert to a numpy array
		arr = np.frombuffer(ptr, np.uint8).reshape((height, width, 4))
	
		# Only modify pixels with non-zero alpha
		arr[arr[:, :, 3] > 0] = [red, green, blue, 255] # white
	
		return QPixmap.fromImage(image)

	# Get color and change the font color
	def changeImageColor(self):
		self.color = QColorDialog.getColor()
		self.convert()
		
	# Saved the rendered image as a png
	def savePixmap(self):
		# Makes the file
		name = self.engOut.toPlainText()
		name = name.replace(" ","_")
		f = "../savedWords/" + name + ".png"

		# Gets the pixmap
		scene = self.graphicsView.scene()
		sceneRect = scene.sceneRect()
		pixmap = QPixmap(sceneRect.size().toSize())
		pixmap.fill(Qt.transparent)
		painter = QPainter(pixmap)
		scene.render(painter, QRectF(pixmap.rect()), sceneRect)
		painter.end()

		# Saves the image
		pixmap.save(f)

		print("Image Saved")

	# Converts the english to zentil and calls letterDisplay
	def convert(self):
		engWord = self.engOut.toPlainText().lower()
		zenWord = ""
		convertedList = self.convertDict.convertString(engWord)
		for pair in convertedList:
			zenWord += pair[0]

		self.zenOut.setText(zenWord)

		self.letterDisplay(convertedList)

	def getSubPixmap(self, subList):
		if not subList:
			return	
		width = 0
		height = 0
		for pair in subList:
			width += pair[1].width()-padding
			height = max(height, pair[1].height())

		if (self.enuncBool == True):
			height = height + 60

		disp = QPixmap(width, height)
		disp.fill(Qt.transparent)
		#print(f"Final width: {width}, height: {height}")

		painter = QPainter()
		if not painter.begin(disp):
			print("Failed to initialize QPainter")
			return

		font = painter.font();
		font.setPixelSize(48);
		painter.setFont(font);

		# Paint the proper images
		width = 0
		if (self.enuncBool == True):
			for pair in subList:
				pairWidth = pair[1].width() - padding
				spacer = width + pairWidth // 2 
				painter.drawPixmap(width, 60, pair[1])
				painter.drawText(spacer, 40, pair[0])
				width += pairWidth

		else:
			for pair in subList:
				pairWidth = pair[1].width() - padding
				painter.drawPixmap(width, 0, pair[1])
				width += pairWidth

		painter.end()  # Ensure this is called to finish painting
		return disp

	def addPixmap(self, pixList):
		if not pixList:
			return	
		width = 0
		height = 0
		for pixmap in pixList:
			width = max(width, pixmap.width())
			height += pixmap.height()
		height += 30 * (len(pixList) - 1)

		disp = QPixmap(width, height)
		disp.fill(Qt.transparent)

		painter = QPainter()
		if not painter.begin(disp):
			print("Failed to initialize QPainter")
			return

		# Paint the proper images
		height = 0
		for pixmap in pixList:
			pixHeight = pixmap.height() + 30
			painter.drawPixmap(0, height, pixmap)
			height += pixHeight

		painter.end()  # Ensure this is called to finish painting
		return disp

	'''
	def commaPixmap(self, subList)
		pixList = []
		lastIndex = 0
		for index, (char, _) in enumerate(subList):
			if char == ',' :
				pixmap = self.getSubPixmap(subList[lastIndex:index])
				lastIndex = index+1
				pixList.append(pixmap)

		if lastIndex != len(subList):
			pixmap = self.getSubPixmap(subList[lastIndex:len(subList)])
			pixList.append(pixmap)
	'''

	def getPixmap(self, recList):
		pixList = []
		newList = []
		print(recList)
		for element in recList:
			print(element)
			if isinstance(element, list):
				if newList:
					pixList.append(self.getSubPixmap(newList))
				if element:
					pixList.append(self.getPixmap(element))
				newList = []
			elif isinstance(element, tuple):
				newList.append(element)

		if newList:
			pixList.append(self.getSubPixmap(newList))
		print("\n",pixList, "\n")
		return self.addPixmap(pixList)

	# Constructs a pixpam of the conversion from ConvertedList
	def letterDisplay(self, convertedList):
		# Set up an empty pixmap to paint the images
		scene = QGraphicsScene(self)
		self.graphicsView.setScene(scene)
		if not convertedList:
			return

		for pair in convertedList:
			if pair[1].isNull():
				print(f"Error: One of the pixmaps is null! Pair: {pair}")
				return

		splitList = self.parseParentheses(convertedList)

		#disp = self.addPixmap(convertedList)
		disp = self.getPixmap(splitList)
		disp = self.replaceImageColor(disp)

		self.graphicsView.scene().addPixmap(disp.scaled(disp.width() // 2, disp.height() // 2))
	
	def parseParentheses(self, tuplesList):
		def helper(index):
			nested = []
			while index < len(tuplesList):
				char, value = tuplesList[index]
				if char == '(':
					sublist, index = helper(index + 1)
					nested.append(sublist)
				elif char == ')':
					return nested, index
				else:
					nested.append((char, value))
				index += 1
			return nested, index

		parsed, _ = helper(0)
		return parsed

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	ui = UI()
	ui.show()
	app.setStyleSheet(qdarkgraystyle.load_stylesheet())

	sys.exit(app.exec_())
