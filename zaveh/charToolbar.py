# charToolbar.py

import os
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
	QWidget, QVBoxLayout, QPushButton,
	QScrollArea, QFrame
)


class CharToolbar:
	def __init__(self, hostWidget: QWidget, targetEditor: QWidget):
		self.hostWidget = hostWidget
		self.targetEditor = targetEditor

		self._build_container()

	def _build_container(self):
		scroll = QScrollArea(self.hostWidget)
		scroll.setWidgetResizable(True)
		scroll.setFrameShape(QFrame.NoFrame)

		content = QWidget()
		self.vbox = QVBoxLayout(content)
		self.vbox.setContentsMargins(8, 8, 8, 8)
		self.vbox.setSpacing(6)

		scroll.setWidget(content)

		layout = self.hostWidget.layout()
		if layout is None:
			layout = QVBoxLayout(self.hostWidget)
			layout.setContentsMargins(0, 0, 0, 0)

		layout.addWidget(scroll)

		self.vbox.addStretch()

	def setItems(self, items):
		while self.vbox.count() > 1:
			item = self.vbox.takeAt(0)
			w = item.widget()
			if w:
				w.deleteLater()

		for it in items:
			btn = QPushButton(it.get("label", ""))

			pixmap = it.get("pixmap")
			btn.setIcon(QIcon(pixmap))
			btn.setIconSize(QSize(24, 24))
			btn.setToolTip(it.get("tooltip", ""))

			btn.setCursor(Qt.PointingHandCursor)
			btn.setMinimumHeight(36)
			btn.setStyleSheet("text-align: left; padding: 6px;")

			toInsert = it["char"]
			btn.clicked.connect(lambda checked=False, c=toInsert: self.insertText(c))

			self.vbox.insertWidget(self.vbox.count() - 1, btn)

	def insertText(self, text: str):
		w = self.targetEditor

		if hasattr(w, "textCursor"):
			cursor = w.textCursor()
			cursor.insertText(text)
			w.setTextCursor(cursor)
			w.setFocus()
			return

		if hasattr(w, "insert"):
			w.insert(text)
			w.setFocus()
			reture
