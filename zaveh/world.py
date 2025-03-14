import sys
import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QGraphicsScene
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt

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



        self.english = ['e', 't', 'a',  'o', 'i',  'n',  's','h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f',  'g']
        self.zentil =  ["a-","z-","eh-","i-","uh-","rr-","f-","n-","h-","v-","t-","l-","o-","th-","k-","sh-","d-"]
        self.pixmaps = [ a,   z,   eh,   i,   uh,   rr,   f,   n,   h,   v,   t,   l,   o,   th,   k,   sh,   d]

        end2 = ["ed", "er"]
        end3 = ["ion", "ing"]
        self.endAll = [end2, end3]

        r1L1 = ["y", "da"]
        r2L1 = ["p", "t"]
        r3L1 = ["v", "f"]
        r4L1 = ["j", "g"]
        r5L1 = ["x", "on"]
        r6L1 = ["q", "k"]
        r7L1 = ["z", "s"]
        r8L1 = ["b", "oe"]
        r9L1 = ["k", "c"]

        r1L2 = ["cc", "c"]
        r2L2 = ["ll", "l"]
        r3L2 = ["sh", "s"]
        r4L2 = ["th", "t"]
        r5L2 = ["oo", "o"]
        r6L2 = ["nn", "n"]
        r7L2 = ["tt", "fin"]
        r8L2 = ["ee", "e"]
        r9L2 = ["rr", "r"]
        r10L2 = ["kn", "k"]
        r11L2 = ["ss", "s"]
        r12L2 = ["ck", "c"]
        r13L2 = ["qu", "k"]


        r1L3 = ["ght", "gt"]

        self.replace1 = [r1L1, r2L1, r3L1, r4L1, r5L1, r6L1, r7L1, r8L1, r9L1]
        self.replace2 = [r1L2, r2L2, r3L2, r4L2, r5L2, r6L2, r7L2, r8L2, r9L2, r10L2, r11L2, r12L2, r13L2]
        self.replace3 = [r1L3]
        self.replaceAll = [self.replace1, self.replace2, self.replace3]

    def on_engOut_textChanged(self):
        self.convert()

    def convert(self):
        engWord = self.engOut.toPlainText()
        engSen = []
        zenWord = ""

        # Transforms the imputed sentence into a list of strings
        sepIndx = 0
        while sepIndx < len(engWord):
            tmpIndx = engWord.find(' ', sepIndx)
            if tmpIndx == -1:
                tmpIndx = len(engWord)
            tmpWord = engWord[sepIndx:tmpIndx]
            engSen.append(tmpWord)
            sepIndx = tmpIndx + 1

        # Edits the word depending on replaceAll and endAll list 
        for targetWord in range(len(engSen)):
            # The word that we will be working on
            word = engSen[targetWord]

            # Trim the ending depending on the endAll list
            #if len(word) > 4:
            #    for i in range(2, 4):
            #        for j in range(len(self.endAll[i - 2])):
            #            if word.endswith(self.endAll[i - 2][j]):
            #                word = word[:-i]

            # Replces all unwanted combinations baced on the replaceAll list
            for i in range(3, 0, -1):
                for j in range(len(self.replaceAll[i - 1])):
                    index = 0
                    while index < len(word):
                        index = word.find(self.replaceAll[i - 1][j][0], index)
                        if index == -1:
                            break
                        word = word[:index] + self.replaceAll[i - 1][j][1] + word[index + i:]
                        index += i

            # Remove duplicates
            #for i in range(1, len(word)):
            #    if word[i] == word[i-1]:
            #        word = word[:i-1] + word[i:]
            #        i=-1
            result = []
            for i in range(len(word)):
                if i == 0 or word[i] != word[i-1]:
                    result.append(word[i])
            word = result

            # Save changes to the word
            engSen[targetWord] = word

            # Convert to Zentil
            for char in word:
                for j in range(len(self.zentil)):
                    if char == self.english[j]:
                        zenWord += self.zentil[j]

            # Add space at end of word
            zenWord = zenWord[:-1] + " "

        # remove space at end of sentence
        zenWord = zenWord[:-1]
        # Display engish enounciation
        self.zenOut.setText(zenWord)

        # Display the letters
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

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = UI()
    ui.show()
    sys.exit(app.exec_())
