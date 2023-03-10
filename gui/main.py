from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox, QGridLayout
from qt_material import apply_stylesheet
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sudoku Solver")
        self.resize(1000,1000)

        layout = QGridLayout() # to create the cells layout
        cellSize = 100

        # row 1
        cell11 = self.createCell(cellSize)
        cell12 = self.createCell(cellSize)
        cell13 = self.createCell(cellSize)
        cell14 = self.createCell(cellSize)
        cell15 = self.createCell(cellSize)
        cell16 = self.createCell(cellSize)
        cell17 = self.createCell(cellSize)
        cell18 = self.createCell(cellSize)
        cell19 = self.createCell(cellSize)
        layout.addWidget(cell11, 1, 1)
        layout.addWidget(cell12, 1, 2) 
        layout.addWidget(cell13, 1, 3)    
        layout.addWidget(cell14, 1, 4)   
        layout.addWidget(cell15, 1, 5)
        layout.addWidget(cell16, 1, 6)
        layout.addWidget(cell17, 1, 7)
        layout.addWidget(cell18, 1, 8)
        layout.addWidget(cell19, 1, 9)

        # row 2
        cell21 = self.createCell(cellSize)
        cell22 = self.createCell(cellSize)
        cell23 = self.createCell(cellSize)
        cell24 = self.createCell(cellSize)
        cell25 = self.createCell(cellSize)
        cell26 = self.createCell(cellSize)
        cell27 = self.createCell(cellSize)
        cell28 = self.createCell(cellSize)
        cell29 = self.createCell(cellSize)
        layout.addWidget(cell21, 2, 1)
        layout.addWidget(cell22, 2, 2) 
        layout.addWidget(cell23, 2, 3)    
        layout.addWidget(cell24, 2, 4)   
        layout.addWidget(cell25, 2, 5)
        layout.addWidget(cell26, 2, 6)
        layout.addWidget(cell27, 2, 7)
        layout.addWidget(cell28, 2, 8)
        layout.addWidget(cell29, 2, 9)

        # row 3
        cell31 = self.createCell(cellSize)
        cell32 = self.createCell(cellSize)
        cell33 = self.createCell(cellSize)
        cell34 = self.createCell(cellSize)
        cell35 = self.createCell(cellSize)
        cell36 = self.createCell(cellSize)
        cell37 = self.createCell(cellSize)
        cell38 = self.createCell(cellSize)
        cell39 = self.createCell(cellSize)
        layout.addWidget(cell31, 3, 1)
        layout.addWidget(cell32, 3, 2) 
        layout.addWidget(cell33, 3, 3)    
        layout.addWidget(cell34, 3, 4)   
        layout.addWidget(cell35, 3, 5)
        layout.addWidget(cell36, 3, 6)
        layout.addWidget(cell37, 3, 7)
        layout.addWidget(cell38, 3, 8)
        layout.addWidget(cell39, 3, 9)

        # row 4
        cell41 = self.createCell(cellSize)
        cell42 = self.createCell(cellSize)
        cell43 = self.createCell(cellSize)
        cell44 = self.createCell(cellSize)
        cell45 = self.createCell(cellSize)
        cell46 = self.createCell(cellSize)
        cell47 = self.createCell(cellSize)
        cell48 = self.createCell(cellSize)
        cell49 = self.createCell(cellSize)
        layout.addWidget(cell41, 4, 1)
        layout.addWidget(cell42, 4, 2) 
        layout.addWidget(cell43, 4, 3)    
        layout.addWidget(cell44, 4, 4)   
        layout.addWidget(cell45, 4, 5)
        layout.addWidget(cell46, 4, 6)
        layout.addWidget(cell47, 4, 7)
        layout.addWidget(cell48, 4, 8)
        layout.addWidget(cell49, 4, 9)

        # row 5
        cell51 = self.createCell(cellSize)
        cell52 = self.createCell(cellSize)
        cell53 = self.createCell(cellSize)
        cell54 = self.createCell(cellSize)
        cell55 = self.createCell(cellSize)
        cell56 = self.createCell(cellSize)
        cell57 = self.createCell(cellSize)
        cell58 = self.createCell(cellSize)
        cell59 = self.createCell(cellSize)
        layout.addWidget(cell51, 5, 1)
        layout.addWidget(cell52, 5, 2) 
        layout.addWidget(cell53, 5, 3)    
        layout.addWidget(cell54, 5, 4)   
        layout.addWidget(cell55, 5, 5)
        layout.addWidget(cell56, 5, 6)
        layout.addWidget(cell57, 5, 7)
        layout.addWidget(cell58, 5, 8)
        layout.addWidget(cell59, 5, 9)

        # row 6
        cell61 = self.createCell(cellSize)
        cell62 = self.createCell(cellSize)
        cell63 = self.createCell(cellSize)
        cell64 = self.createCell(cellSize)
        cell65 = self.createCell(cellSize)
        cell66 = self.createCell(cellSize)
        cell67 = self.createCell(cellSize)
        cell68 = self.createCell(cellSize)
        cell69 = self.createCell(cellSize)
        layout.addWidget(cell61, 6, 1)
        layout.addWidget(cell62, 6, 2) 
        layout.addWidget(cell63, 6, 3)    
        layout.addWidget(cell64, 6, 4)   
        layout.addWidget(cell65, 6, 5)
        layout.addWidget(cell66, 6, 6)
        layout.addWidget(cell67, 6, 7)
        layout.addWidget(cell68, 6, 8)
        layout.addWidget(cell69, 6, 9)

        # row 7
        cell71 = self.createCell(cellSize)
        cell72 = self.createCell(cellSize)
        cell73 = self.createCell(cellSize)
        cell74 = self.createCell(cellSize)
        cell75 = self.createCell(cellSize)
        cell76 = self.createCell(cellSize)
        cell77 = self.createCell(cellSize)
        cell78 = self.createCell(cellSize)
        cell79 = self.createCell(cellSize)
        layout.addWidget(cell71, 7, 1)
        layout.addWidget(cell72, 7, 2) 
        layout.addWidget(cell73, 7, 3)    
        layout.addWidget(cell74, 7, 4)   
        layout.addWidget(cell75, 7, 5)
        layout.addWidget(cell76, 7, 6)
        layout.addWidget(cell77, 7, 7)
        layout.addWidget(cell78, 7, 8)
        layout.addWidget(cell79, 7, 9)

        # row 8
        cell81 = self.createCell(cellSize)
        cell82 = self.createCell(cellSize)
        cell83 = self.createCell(cellSize)
        cell84 = self.createCell(cellSize)
        cell85 = self.createCell(cellSize)
        cell86 = self.createCell(cellSize)
        cell87 = self.createCell(cellSize)
        cell88 = self.createCell(cellSize)
        cell89 = self.createCell(cellSize)
        layout.addWidget(cell81, 8, 1)
        layout.addWidget(cell82, 8, 2) 
        layout.addWidget(cell83, 8, 3)    
        layout.addWidget(cell84, 8, 4)   
        layout.addWidget(cell85, 8, 5)
        layout.addWidget(cell86, 8, 6)
        layout.addWidget(cell87, 8, 7)
        layout.addWidget(cell88, 8, 8)
        layout.addWidget(cell89, 8, 9)

        # row 9
        cell91 = self.createCell(cellSize)
        cell92 = self.createCell(cellSize)
        cell93 = self.createCell(cellSize)
        cell94 = self.createCell(cellSize)
        cell95 = self.createCell(cellSize)
        cell96 = self.createCell(cellSize)
        cell97 = self.createCell(cellSize)
        cell98 = self.createCell(cellSize)
        cell99 = self.createCell(cellSize)
        layout.addWidget(cell91, 9, 1)
        layout.addWidget(cell92, 9, 2) 
        layout.addWidget(cell93, 9, 3)    
        layout.addWidget(cell94, 9, 4)   
        layout.addWidget(cell95, 9, 5)
        layout.addWidget(cell96, 9, 6)
        layout.addWidget(cell97, 9, 7)
        layout.addWidget(cell98, 9, 8)
        layout.addWidget(cell99, 9, 9)

        # creting the widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def createCell(self, size):
        # crete che combobox
        items = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        cell = QComboBox()
        cell.addItems(items)
        cell.setFixedSize(size, size)
        return cell

app = QApplication(sys.argv)

# setup stylesheet
apply_stylesheet(app, theme='light_blue.xml')

window = MainWindow()
window.show()

app.exec()