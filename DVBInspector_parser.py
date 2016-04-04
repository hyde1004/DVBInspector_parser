import sys
from PyQt5.QtWidgets import QTreeWidget, QApplication, QTreeWidgetItem

app = QApplication(sys.argv)

tree = QTreeWidget()


str = '''
PSI
+-PAT
| +-TableType: program_association_section (0/0)
|   +-table_id: 0x0 (0) => program_association_section
|   +-section_syntax_indicator: 0x1 (1)
|   +-private_indicator: 0x0 (0)
|   +-section_length: 0xA5 (165)
|   +-table_id_extension: 0x5 (5)
|   +-version: 0x0 (0)
|   +-current_next_indicator: 0x1 (1) => current
|   +-section_number: 0x0 (0)
|   +-last_section_number: 0x0 (0)
|   +-private_data: 0x0000E0100488FB5808B4F5E00A10F7D40A3DF3240DBBF4B415A8E7D015B5EC8015BCE5781887F004189EF0CC189FF57C1D7CF964205AF70C2187F3EC2C62FC842F34FCE82F3CFD4C1D4DFAF41D8AF7702EF5FDB02F3FFF9A2F6CFF182F6DFC2015C5E1F4 ".......X.........=.$...............x...........|.|.d Z..!...,b../4../<.L.M.....p..../?../l../m. ...."
|   +-programs: 39 entries
|     +-program (null)
|     | +-program_number: 0x0 (0)
|     | +-program_map_PID: 0x10 (16)
|     +-program (SONY MAX)
|     | +-program_number: 0x488 (1160)
|     | +-program_map_PID: 0x1B58 (7000)
'''
depths = []

strings = str.split('\n')
for string in strings:

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
	# if pos < 0: # root
	# 	depths = []
	# 	depths.append(items)
	#QTreeWidgetItem(tree, ['PSI'])

tree.show()

sys.exit(app.exec_()) 