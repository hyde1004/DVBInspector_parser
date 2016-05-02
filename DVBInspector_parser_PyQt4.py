import sys
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		self.tree = QtGui.QTreeWidget(self)
		self.setCentralWidget(self.tree)
		self.setGeometry(300, 300, 500, 500)
		self.LoadFile()
		self.show()

	def LoadFile(self):
		in_file = open('PSI-TS-5CLEAR_08102015.txt', 'rt')
		strings = in_file.readlines()
		in_file.close()
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
				item = QtGui.QTreeWidgetItem(parent, [text])
				depths = depths[0:level]
				depths.append(item) 
			else:
				text = string
				item = QtGui.QTreeWidgetItem(self.tree, [text])
				depths = []
				depths.append(item)

def main():
	app = QtGui.QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
