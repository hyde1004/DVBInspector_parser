import sys
from PyQt5.QtWidgets import QTreeWidget, QApplication, QTreeWidgetItem

app = QApplication(sys.argv)

tree = QTreeWidget()

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

sys.exit(app.exec_()) 