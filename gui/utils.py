from gui.customComboBox import *
import darkdetect

class Utils():
    def __init__(self):
        super().__init__()
        try:
            self.isDark = darkdetect.isDark()
        except:
            self.isDark = False

    def createCell(self, size):
        # crete che combobox
        cell = customComboBox()
        cell.setFixedSize(size, size)
        return cell

    def createString(self, cells):
        # create the string that will be printed in the data.dzn file
        # that will be used from minizinc to get the cell inserted from the user
        string = "pre = \n[| "
        for i in range(81):
            string = string + cells[i].currentText()
            if i == 80:
                string = string + "\n|];"
            elif ((i+1) % 9 == 0):
                string = string + "\n| "
            else:
                string = string + ", "
        return string

    def getResList(self, res):
        # method used to parse the result of minizinc into a list of numbers
        # see exampleFile.dzn to see an example of output
        resList = []
        a1 = res.split('=')[1]
        a1 = a1.split(';')[0]
        a1 = a1.split('[')[1]
        a1 = a1.split(']')[0]
        blocks = a1.strip().split('|')
        
        for i in range(1,10):
            b = blocks[i].split(' ')
            for j in range(1,9):
                resList.append(int(b[j].split(',')[0]))
            resList.append(int(b[9].split('\\')[0]))
        
        return resList
    
    def insertInTheCell(self, cells, resList, data):
        # insert in the cells the numbers of resList
        dataList = self.getResList(data)
        for cell in cells:
            number1 = resList.pop(0)
            number2 = dataList.pop(0)
            if number2 == 0:
                cell.setCurrentIndex(int(number1))
                if self.isDark:
                    cell.setStyleSheet("QComboBox"
                                        "{"
                                        "border : 2px white;"
                                        "border-style : dashed;"
                                        "}")   
                else:
                    cell.setStyleSheet("QComboBox"
                                        "{"
                                        "border : 2px black;"
                                        "border-style : dashed;"
                                        "}")
                
    def clearAll(self, cells):
        # clear all the cells
        for cell in cells:
            cell.setCurrentIndex(0)
  

    def addTestFile(self, cells, resList):
        # insert in the cells the numbers in exampleFile.dzn
        for i in range(len(resList)):
            cells[i].setCurrentIndex(resList[i])

