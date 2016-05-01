import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		self.tree = QtGui.QTreeWidget()
		self.setGeometry(300, 300, 250, 150)
		self.LoadFile()
		self.show()

	def LoadFile(self):
		in_file = open('PSI-TS-5CLEAR_08102015.txt', 'rt')
		strings = in_file.readlines()
		depths = []

		for string in strings:
			string = string.rstrip()

			if len(string) == 0:
				continue

			pos = string.find('+-')
			level = pos // 2 + 1

			if pos >= 0:
				text = string[pos+2:]
				parent = depths[level-1]
				item = QTreeWidgetItem(parent, [text])
				depths = depths[0:level]
				depths.append(item) 
			else:
				text = string
				item = QTreeWidgetItem(tree, [text])
				depths = []
				depths.append(item)

			tree.setGeometry(300, 300, 900, 500)
		tree.show()		


def main():
	app = QtGui.QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
