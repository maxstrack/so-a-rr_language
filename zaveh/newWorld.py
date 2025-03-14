import sys
import re
import math
import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QColorDialog
from PyQt5.QtGui import QPixmap, QPainter, QColor, QImage
from PyQt5.QtCore import Qt, QRectF, QPointF, QSizeF
import numpy as np
import qdarkgraystyle

from PyQt5.QtGui import QImage, QTransform

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
		self.splitLineEdit.textChanged.connect(self.changeAngle)
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

		numStart = QPixmap("../letters/numStart.png")
		numEnd = QPixmap("../letters/numEnd.png")
		'''
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
		'''

		# Make Lists of the new consonant and vowle pixmaps
		consonants = [s, n, t, z, k, h, v, g]
		newC = self.paintNewMaps(consonants, consonant) 
		vowles = [e, a, u, i, oo, ah]
		newV = self.paintNewMaps(vowles, vowle) 
	
		initialData = {
		# consonants
			('k', 'c', 'qu', 'ck', 'lk', 'q', 'cc', 'cqu')	: ('s', s),  # /k/ sound
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
			'~' : ('~', space),
		}


		numData = {
			'0' : ('0', h),
			'1' : ('1', d),
			'2' : ('2', s),
			'3' : ('3', g),
			'4' : ('4', k),
			'5' : ('5', oo),
			'6' : ('6', l),
			'7' : ('7', t),
			'8' : ('8', u),
			'9' : ('9', a),
			'a' : ('a', v),
			'b' : ('b', z),
			'c' : ('c', ah),
			'd' : ('d', e),
			'e' : ('e', rr),
			'f' : ('f', i),
			'g' : ('g', n),
			'(' : ('', numStart),
			')' : ('', numEnd),
		}
		# Make a new Dictionaries using AliasDict
		self.convertDict = AliasDict(initialData)
		self.numDict = AliasDict(numData)

		# bool for Enunciation
		self.enuncBool = True

		# Color for letter font
		self.color = QColor("white")

		# Degree for angle split
		self.totalAngle = 90

	# takes the english string, replaces all numbers with ~ 
	# Then returns new string and list of base 17 numbers
	def parseReplace(self, engString):
		numList = []

		def int_to_base(n, base=17):
			# Base 17 digits: 0-9 then a, b, c, d, e, f, g 
			digits = "0123456789abcdefg"
			if n == 0:
				return "0"
			result = ""
			while n:
				n, remainder = divmod(n, base)
				result = digits[remainder] + result
			return result

		# This helper will be called for every match.
		def repl(match):
			numberStr = match.group(0)
			number = int(numberStr)
			converted = int_to_base(number)
			numList.append(converted)
			return "~"	# Replace the number with "~"

		newstring = re.sub(r'\d+', repl, engString)
		return newstring, numList

	# takes a vector of tuples, and replaces the the '~' (first element of the tuple) 
	# with the corresponding number in numList
	def numInsert(self, convertList, numList):
		newConvertList = []
		num_idx = 0 
		
		for tup in convertList:
			# If the first element of the tuple is '~' and we have a number to insert:
			if tup[0] == '~' and num_idx < len(numList):
				num = numList[num_idx]
				pixList = self.numDict.convertString('('+num+')')
				(newPix,_) = self.getSubPixmap(pixList, False)
				new_tuple = (num, newPix)
				num_idx += 1
			else:
				new_tuple = tup
			newConvertList.append(new_tuple)
		
		return newConvertList


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

	# changes the totalAngle and re-calls convert
	# Effectivly changing the setting
	def changeAngle(self):
		try:
			self.totalAngle = int(self.splitLineEdit.text())
			self.convert()
		except:
			return

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

	# Converts a list of letter tupes into a pixmap
	def getSubPixmap(self, subList, enunc=None):
		if enunc is None:
			enunc = self.enuncBool

		if not subList:
			return	

		width = 0
		height = 0
		for pair in subList:
			width += pair[1].width()-padding
			height = max(height, pair[1].height())

		if (enunc == True):
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
		# enouncciation
		if (enunc == True):
			for pair in subList:
				pairWidth = pair[1].width() - padding
				spacer = width + pairWidth // 2 
				painter.drawPixmap(width, 60, pair[1])
				painter.drawText(spacer, 40, pair[0])
				width += pairWidth

		# No enouncciation
		else:
			for pair in subList:
				pairWidth = pair[1].width() - padding
				painter.drawPixmap(width, 0, pair[1])
				width += pairWidth

		painter.end()  # Ensure this is called to finish painting
		return (disp, disp.height()//2)

	# Adds a list of pixmaps verticaly into a new pixmap
	def addPixmapV(self, pixList):
		if len(pixList) == 1:
			return	pixList[0]

		n = len(pixList)

		theta = self.totalAngle / (n - 1)

		if n % 2 == 1:
			# For odd numbers, use integer multipliers.
			multipliers = list(range(-(n - 1) // 2, (n - 1) // 2 + 1))
		else:
			# For even numbers, use half-step multipliers.
			start = -(n - 1) / 2.0
			multipliers = [start + i for i in range(n)]

		angles = [mult * theta for mult in multipliers]
		pixmaps = list(zip(pixList, angles))

		totAngle = self.totalAngle/2
		anchorGap = 100

		minY = float('inf')
		maxY = float('-inf')
		maxX = 0

		for i, ((pixmap, _), angle) in enumerate(pixmaps):
			if not pixmap:
				return

			rotated = pixmap.transformed(QTransform().rotate(angle))
			baseOffset = i * anchorGap

			# For positive angles, the pixmap’s "tip" is at the top.
			# For negative angles, the tip is at the bottom.
			if angle > 0:
				drawY = baseOffset
			elif angle < 0:
				drawY = baseOffset - rotated.height()
			else:
				drawY = baseOffset - rotated.height() // 2

			drawX = int(totAngle - abs(angle)) * 4

			minY = min(minY, drawY)
			maxY = max(maxY, drawY + rotated.height())
			maxX = max(maxX, drawX + rotated.width())

		h = maxY - minY
		w = maxX
		baseline = -minY

		result = QPixmap(w, h)
		result.fill(Qt.transparent)

		painter = QPainter(result)
		# Paint the proper images
		for i, ((pixmap, _), angle) in enumerate(pixmaps):
			rotated = pixmap.transformed(QTransform().rotate(angle))
			anchor = baseline + i * anchorGap

			if angle > 0:
				# the top of the rotated pixmap aligns with the anchor
				drawY = anchor	
			elif angle < 0:
				# the bottom aligns with the anchor
				drawY = anchor - rotated.height()  
			else:
				# center the pixmap vertically on the anchor.
				drawY = anchor - rotated.height() // 2

			drawX = int(totAngle - abs(angle)) * 4
			painter.drawPixmap(drawX, drawY, rotated)

		painter.end()  # Finish painting
		midPoint = int(baseline + (len(pixList)-1)/2 * anchorGap)

		return (result, midPoint)

	# Adds a list of pixmaps horisontaly into a new pixmap
	def addPixmapH(self, pixList):
		if not pixList:
			return	
		width = 0
		height = 0
		midHeight = 0
		# get the base size
		for (pixmap, midPoint) in pixList:
			width += pixmap.width()
			height = max(height, pixmap.height())
			midHeight = max(midHeight, midPoint)

		disp = QPixmap(width, height)
		disp.fill(Qt.transparent)

		painter = QPainter()
		if not painter.begin(disp):
			print("Failed to initialize QPainter")
			return

		# Paint the proper images
		width = 0
		for (pixmap, midPoint) in pixList:
			pixWidth = pixmap.width()
			placeHeight = (midHeight - midPoint)
			painter.drawPixmap(width, placeHeight, pixmap)
			width += pixWidth

		painter.end()  # Ensure this is called to finish painting
		return (disp, midHeight)

	# Go through the recusive list deviding the sentence verticaly and horizontaly
	# ( , ) for vertical seperation
	# Base case is connecting horizontaly
	def getPixmap(self, recList):
		pixListV = []
		pixListH = []
		newList = []
		comma = 0
		for element in recList:
			# for adding pixmaps horisontaly
			if isinstance(element, list):
				if newList:
					# condence individual tupels into a pixmap
					pixListH.append(self.getSubPixmap(newList))
				if element:
					# Called recursivly on subLists
					pixListH.append(self.getPixmap(element))
				newList = []
			# for adding pixmaps verticaly
			elif isinstance(element, tuple) and newList and element[0] == ',':
				# combine all horixontal maps and add resulting map to verical list
				pixListH.append(self.getSubPixmap(newList))
				pixListV.append(self.addPixmapH(pixListH))
				newList = []
				pixListH = []
				comma = 1
			# base case
			else:
				newList.append(element)

		# Catch all remainig elements after last list or comma
		if newList:
			pixListH.append(self.getSubPixmap(newList))
		if pixListH:
			dispTuple = self.addPixmapH(pixListH)
			pixListV.append(dispTuple)
		if comma == 1:	
			dispTuple = self.addPixmapV(pixListV)
			#disp = self.rotate_and_composite_pixmaps(pixListV)
		try: return dispTuple 
		except: return

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


		#disp = self.gutSubPixmap(convertedList)
		try: 
			splitList = self.parseParentheses(convertedList)
			(disp, _) = self.getPixmap(splitList)
		except:
			(disp, _) = self.getSubPixmap(convertedList)

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

	# Converts the english to zentil and calls letterDisplay
	def convert(self):
		engWord = self.engOut.toPlainText().lower()
		zenWord = ""
		noNumWord, numberList = self.parseReplace(engWord)
		convertedList = self.convertDict.convertString(noNumWord)
		convertedList = self.numInsert(convertedList, numberList)
		for pair in convertedList:
			zenWord += pair[0]

		self.zenOut.setText(zenWord)

		self.letterDisplay(convertedList)

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	ui = UI()
	ui.show()
	app.setStyleSheet(qdarkgraystyle.load_stylesheet())

	sys.exit(app.exec_())
