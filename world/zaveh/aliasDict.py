# aliasDict.py
import re

class AliasDict:
	def __init__(self, initialData=None):
		self.dataStore = {}
		self.aliasStore = {}
		if initialData:
			for keyGroup, value in initialData.items():
				if isinstance(keyGroup, tuple):
					primaryKey = keyGroup[0]
					self.addKey(primaryKey, value)
					for alias in keyGroup[1:]:
						self.addAlias(alias, primaryKey)
				else:
					self.addKey(keyGroup, value)

	def addKey(self, key, value):
		self.dataStore[key] = value

	def addAlias(self, alias, key):
		if key in self.dataStore:
			self.aliasStore[alias] = key
		else:
			raise KeyError(f"Key '{key}' not found to alias.")

	def getValue(self, keyOrAlias):
		if keyOrAlias in self.dataStore:
			return self.dataStore[keyOrAlias]
		elif keyOrAlias in self.aliasStore:
			actualKey = self.aliasStore[keyOrAlias]
			return self.dataStore[actualKey]
		else:
			raise KeyError(f"Key or alias '{keyOrAlias}' not found.")

	# Convert a string and return tuple list
	def convertString(self, inputString):
		allKeys = list(self.dataStore.keys()) + list(self.aliasStore.keys())
		allKeys = sorted(allKeys, key=len, reverse=True)

		tupleList = []

		# Use regex to find and replace each key/alias with its value
		def collectMatch(match):
			keyOrAlias = match.group(0)
			try:
				tupleList.append(self.getValue(keyOrAlias))
			except KeyError:
				print(f"Failed to convert '{keyOrAlias}'")

		# Create a regex pattern to match any key or alias
		pattern = re.compile('|'.join(map(re.escape, allKeys)))

		# Find and collect each match without substituting them in the string
		pattern.sub(collectMatch, inputString)
	
		return tupleList
