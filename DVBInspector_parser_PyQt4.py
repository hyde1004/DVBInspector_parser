import sys
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		openFile = QtGui.QAction('Open', self)
		openFile.triggered.connect(self.showDialog)

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(openFile)

		self.tree = QtGui.QTreeWidget(self)
		self.setCentralWidget(self.tree)

		self.setGeometry(300, 300, 500, 500)
		self.show()

	def showDialog(self):
		fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file')
		try:
			self.LoadFile(filename)
		except:
			print('open error')

	def LoadFile(self, filename):
		in_file = open(filename, 'rt')
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
