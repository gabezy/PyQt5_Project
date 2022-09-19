import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from design import Ui_MainWindow


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        self.boxesList = [f'self.regua_{x}' for x in range(1, 25)]
        super().__init__(parent)
        super().setupUi(self)
        self.btnCalc.clicked.connect(self.calcP) 


    def calcP(self):
        p = 0
        
        for box in self.boxesList:
            box = eval(box)
            if self.checkB(box):
                p += 1
        
        nome = self.nameInput.text()
        if p < 22:
            self.statusLabel.setText(f'Funcionário {nome.title()} está INAPTO')
            self.statusLabel.setStyleSheet('color: red; font-weight: bold')
        else:
            self.statusLabel.setText(f'Funcionário {nome.title()} está APTO')
            self.statusLabel.setStyleSheet('color: green; font-weight: bold') 
        
        self.pontInput.setText(str(p))
    
    def checkB(self, name_box: int):
        if name_box.isChecked():
            return True
        return False
        

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_() 



