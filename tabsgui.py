import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout,QGridLayout,QGroupBox,QHBoxLayout,QLineEdit,QLabel,QCheckBox,QRadioButton,QListWidget,QListWidgetItem
from PyQt5.QtCore import pyqtSlot
import random
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure 

matplotlib.use("Qt5Agg")
class PlotSpot(FigureCanvasQTAgg) :

    def __init__(self, parent=None, width=5, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)
  
    def plot(self, x, y) :
        self.axes.clear()
        self.axes.plot(x, y)


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 tabs - pythonspot.com'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.setWindowTitle(self.title)
        #self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        
        self.show()
        
    
class MyTableWidget(QWidget):
    
    def __init__(self, parent):
      
        super(QWidget, self).__init__(parent)
        #
        #
        #Set up for Tab 2
        self.val1 = random.randint(1, 10)
        self.val2 = random.randint(1, 10)
        self.val3 = random.randint(1, 10)
        self.val4 = random.randint(1, 10)
        self.createTopGroupBox()
        self.createBottomRightGroupBox()

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.topGroupBox, 1, 0,1,1)
        mainLayout.addWidget(self.bottomRightGroupBox, 2, 0,1,1)
        #mainLayout.setRowStretch(1, 1)
        #mainLayout.setRowStretch(2, 1)
        #mainLayout.setColumnStretch(0, 1)
        #mainLayout.setColumnStretch(1, 1)
        #
        #
        #
        #setup tab 1
        self.createLeftGroupBox1()
        self.createLeftGroupBox2()
        self.createLeftGroupBox3()
        self.createLeftGroupBox4()
        self.createRightGroupBox1()
        self.createRightGroupBox2()
        self.createBottomBox()

        mainLayout1 = QGridLayout()
        mainLayout1.addWidget(self.LeftGroupBox1, 1, 0)
        mainLayout1.addWidget(self.LeftGroupBox2, 2, 0)
        mainLayout1.addWidget(self.LeftGroupBox3, 3, 0)
        mainLayout1.addWidget(self.LeftGroupBox4, 4, 0)
        mainLayout1.addWidget(self.RightGroupBox1, 1, 1,3,1)
        mainLayout1.addWidget(self.RightGroupBox2, 4, 1)
        mainLayout1.addWidget(self.BottomBox, 5, 0,1,2)
        '''mainLayout1.setRowStretch(1, 1)
        mainLayout1.setRowStretch(2, 1)
        mainLayout1.setColumnStretch(0, 1)
        mainLayout1.setColumnStretch(1, 1)'''
        #
        #
        #
                
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        #self.tabs.resize(300,200)
        
        # Add tabs
        self.tabs.addTab(self.tab1,"Thermal Battery Simulator")
        self.tabs.addTab(self.tab2,"Plots and Trends")
        
        # Create first tab



        self.tab1.setLayout(mainLayout1)
        self.tab2.setLayout(mainLayout)
        
        # Add tabs to widget










        # Add tabs to widget
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


    ###FIRST GAME CODE


   
    def GETERDONE(self):
        #gets a string with the material name in it
        Material = self.Material_widget.currentItem().text()
        #Get's Particle size
        Partsize = 0.0
        if self.materialsize1.isChecked():
            Partsize = .003
            print(Partsize)
        if self.materialsize2.isChecked():
            Partsize = .006
            print(Partsize)
        #Heat exchanger area
        A = float(self.HEI1.text())
        #Heat transfer Coefficient
        U = float(self.HEI2.text())
        #Bed Length
        L = float(self.HEI3.text())
        #Ambient Temp
        Tamb = float(self.TMF1.text())
        #Storage Inlet Temp
        Stin = float(self.TMF2.text())
        #Hot Fluid Exit Temp
        Thout = float(self.TMF3.text())
        #Hot Fluid Inlet Temp
        Thin = float(self.TMF4.text())
        #Mass flowrate hot
        mhot = float(self.TMF5.text())
        #Cold Fluid Inlet Temp
        TCin = float(self.TMF6.text())
        #Mass flowrate hot
        mcold = float(self.TMF7.text())
        #gets a string with the material name in it
        HETYPE = self.HeatExchangerTypes.currentItem().text()
        print(A)
        print(U)
        print(L)
        print(Tamb)
        print(Stin)
        print(Thout)
        print(Thin)
        print(mhot)
        print(TCin)
        print(mcold)
        print(HETYPE)



        pass
    def createTopGroupBox(self):

        self.topGroupBox = QGroupBox(self.tr("Pressure drop"))
        self.Plot1 = PlotSpot()

        layout = QVBoxLayout()
        layout.addWidget(self.Plot1)
        layout.addStretch(1)
        self.topGroupBox.setLayout(layout)

    def createBottomRightGroupBox(self):

        self.bottomRightGroupBox = QGroupBox(
        self.tr("Plot 2 Title"))

        self.Plot2 = PlotSpot()

        layout = QVBoxLayout()
        layout.addWidget(self.Plot2)
        layout.addStretch(1)
        self.bottomRightGroupBox.setLayout(layout)


    ###
    ###GUI Layout
    def createLeftGroupBox1(self):
        self.LeftGroupBox1 = QGroupBox(self.tr("Select a Material"))
        self.Material_widget = QListWidget()
        item = QListWidgetItem("Denstone Delta P1")
        self.Material_widget.addItem(item)
        item = QListWidgetItem("Denstone 99")
        self.Material_widget.addItem(item)
        item = QListWidgetItem("Rethink Ceramic Flora, 100% Recycled Ceramic")
        self.Material_widget.addItem(item)
        layout = QVBoxLayout()
        layout.addWidget(self.Material_widget)
        #layout.addWidget(self.HelpMessage)
        self.LeftGroupBox1.setLayout(layout)
    def createLeftGroupBox2(self):
        self.LeftGroupBox2 = QGroupBox(self.tr("Select Material Size"))
        self.materialsize1 = QRadioButton(self)
        self.materialsizelabel1= QLabel()
        self.materialsizelabel1.setText("3 mm")
        self.materialsizelabel2= QLabel()
        self.materialsizelabel2.setText("6 mm")
        
        self.materialsize2 = QRadioButton(self)
        layout = QGridLayout()
        layout.addWidget(self.materialsize1, 1, 0)
        layout.addWidget(self.materialsizelabel1, 1, 1)
        layout.addWidget(self.materialsizelabel2, 2, 1)
        layout.addWidget(self.materialsize2, 2, 0)
        #layout.addWidget(self.HelpMessage)
        self.LeftGroupBox2.setLayout(layout)
    def createLeftGroupBox3(self):
        self.LeftGroupBox3 = QGroupBox(self.tr("Heat Exchanger Imputs"))

        self.HEI1 = QLineEdit(self)
        self.HEI1Label= QLabel()
        self.HEI1Label.setText("Heat Exchanger Area")
        self.HEI1Units= QLabel()
        self.HEI1Units.setText("m^2")

        self.HEI2 = QLineEdit(self)
        self.HEI2Label= QLabel()
        self.HEI2Label.setText("Overall Heat Transfer Coefficient")
        self.HEI2Units= QLabel()
        self.HEI2Units.setText("kW/m^2*K")

        self.HEI3 = QLineEdit(self)
        self.HEI3Label= QLabel()
        self.HEI3Label.setText("Bed Length")
        self.HEI3Units= QLabel()
        self.HEI3Units.setText("m") 



        layout = QGridLayout()
        layout.addWidget(self.HEI1Label, 1, 0)
        layout.addWidget(self.HEI1, 1, 1)
        layout.addWidget(self.HEI1Units, 1, 2)
        layout.addWidget(self.HEI2Label, 2, 0)
        layout.addWidget(self.HEI2, 2, 1)
        layout.addWidget(self.HEI2Units, 2, 2)
        layout.addWidget(self.HEI3Label, 3, 0)
        layout.addWidget(self.HEI3, 3, 1)
        layout.addWidget(self.HEI3Units, 3, 2)

        #layout.addWidget(self.HelpMessage)
        self.LeftGroupBox3.setLayout(layout)
        
    def createRightGroupBox1(self):
        self.RightGroupBox1 = QGroupBox(self.tr("Temperature and Mass Flowrate Inputs"))

        self.TMF1 = QLineEdit(self)
        self.TMF1Label= QLabel()
        self.TMF1Label.setText("Ambient Temperature")
        self.TMF1Units= QLabel()
        self.TMF1Units.setText("C")

        self.TMF2 = QLineEdit(self)
        self.TMF2Label= QLabel()
        self.TMF2Label.setText("Storage Inlet Temperature")
        self.TMF2Units= QLabel()
        self.TMF2Units.setText("C")

        self.TMF3 = QLineEdit(self)
        self.TMF3Label= QLabel()
        self.TMF3Label.setText("Hot Fluid Exit Temperature")
        self.TMF3Units= QLabel()
        self.TMF3Units.setText("C") 

        self.TMF4 = QLineEdit(self)
        self.TMF4Label= QLabel()
        self.TMF4Label.setText("Hot Fluid Inlet Temperature")
        self.TMF4Units= QLabel()
        self.TMF4Units.setText("C") 

        self.TMF5 = QLineEdit(self)
        self.TMF5Label= QLabel()
        self.TMF5Label.setText("Mass Flow Rate of Hot Fluid")
        self.TMF5Units= QLabel()
        self.TMF5Units.setText("kg/s") 

        self.TMF6 = QLineEdit(self)
        self.TMF6Label= QLabel()
        self.TMF6Label.setText("Cold Fluid Inlet Temperature")
        self.TMF6Units= QLabel()
        self.TMF6Units.setText("C") 

        self.TMF7 = QLineEdit(self)
        self.TMF7Label= QLabel()
        self.TMF7Label.setText("Mass Flow Rate of Cold Fluid")
        self.TMF7Units= QLabel()
        self.TMF7Units.setText("kg/s") 

        layout = QGridLayout()
        layout.addWidget(self.TMF1Label, 1, 0)
        layout.addWidget(self.TMF1, 1, 1)
        layout.addWidget(self.TMF1Units, 1, 2)
        layout.addWidget(self.TMF2Label, 2, 0)
        layout.addWidget(self.TMF2, 2, 1)
        layout.addWidget(self.TMF2Units, 2, 2)
        layout.addWidget(self.TMF3Label, 3, 0)
        layout.addWidget(self.TMF3, 3, 1)
        layout.addWidget(self.TMF3Units, 3, 2)
        layout.addWidget(self.TMF4Label, 4, 0)
        layout.addWidget(self.TMF4, 4, 1)
        layout.addWidget(self.TMF4Units, 4, 2)
        layout.addWidget(self.TMF5Label, 5, 0)
        layout.addWidget(self.TMF5, 5, 1)
        layout.addWidget(self.TMF5Units, 5, 2)
        layout.addWidget(self.TMF6Label, 6, 0)
        layout.addWidget(self.TMF6, 6, 1)
        layout.addWidget(self.TMF6Units, 6, 2)
        layout.addWidget(self.TMF7Label, 7, 0)
        layout.addWidget(self.TMF7, 7, 1)
        layout.addWidget(self.TMF7Units, 7, 2)

        #layout.addWidget(self.HelpMessage)
        self.RightGroupBox1.setLayout(layout)
    
    def createLeftGroupBox4(self):
        self.LeftGroupBox4 = QGroupBox(self.tr("Outputs"))

        self.O1 = QLineEdit(self)
        self.O1.setDisabled(True)
        self.O1Label= QLabel()
        self.O1Label.setText("Heat Exchanger Effectivness")
        self.O1Units= QLabel()
        self.O1Units.setText("")

        self.O2 = QLineEdit(self)
        self.O2.setDisabled(True)
        self.O2Label= QLabel()
        self.O2Label.setText("Exergy Efficiency")
        self.O2Units= QLabel()
        self.O2Units.setText("%")

        self.O3 = QLineEdit(self)
        self.O3.setDisabled(True)
        self.O3Label= QLabel()
        self.O3Label.setText("Storage Exit Temperature")
        self.O3Units= QLabel()
        self.O3Units.setText("C") 

        self.O4 = QLineEdit(self)
        self.O4.setDisabled(True)
        self.O4Label= QLabel()
        self.O4Label.setText("Pressure Drop Ratio")
        self.O4Units= QLabel()
        self.O4Units.setText("") 

        self.O5 = QLineEdit(self)
        self.O5.setDisabled(True)
        self.O5Label= QLabel()
        self.O5Label.setText("Storage Cost")
        self.O5Units= QLabel()
        self.O5Units.setText("kW/h") 





        layout = QGridLayout()
        layout.addWidget(self.O1Label, 1, 0)
        layout.addWidget(self.O1, 1, 1)
        layout.addWidget(self.O1Units, 1, 2)
        layout.addWidget(self.O2Label, 2, 0)
        layout.addWidget(self.O2, 2, 1)
        layout.addWidget(self.O2Units, 2, 2)
        layout.addWidget(self.O3Label, 3, 0)
        layout.addWidget(self.O3, 3, 1)
        layout.addWidget(self.O3Units, 3, 2)
        layout.addWidget(self.O4Label, 4, 0)
        layout.addWidget(self.O4, 4, 1)
        layout.addWidget(self.O4Units, 4, 2)
        layout.addWidget(self.O5Label, 5, 0)
        layout.addWidget(self.O5, 5, 1)
        layout.addWidget(self.O5Units, 5, 2)


        #layout.addWidget(self.HelpMessage)
        self.LeftGroupBox4.setLayout(layout)

    def createRightGroupBox2(self):
        self.RightGroupBox2 = QGroupBox(self.tr("Temperature and Mass Flowrate Inputs"))
        self.HeatExchangerTypes = QListWidget()
        item = QListWidgetItem("Parallel Flow")
        self.HeatExchangerTypes.addItem(item)
        item = QListWidgetItem("Counter Flow")
        self.HeatExchangerTypes.addItem(item)
        item = QListWidgetItem("One Shell Pass")
        self.HeatExchangerTypes.addItem(item)
        item = QListWidgetItem("N Shell Pass")
        self.HeatExchangerTypes.addItem(item)
        item = QListWidgetItem("Cross both Unmixed")
        self.HeatExchangerTypes.addItem(item)
        item = QListWidgetItem("Cross Cmax Mixed")
        self.HeatExchangerTypes.addItem(item)
        item = QListWidgetItem("Cross Cmin Mixed")
        self.HeatExchangerTypes.addItem(item)
        layout = QVBoxLayout()
        layout.addWidget(self.HeatExchangerTypes)
        #layout.addWidget(self.HelpMessage)

        #layout.addWidget(self.HelpMessage)
        self.RightGroupBox2.setLayout(layout)
    def createBottomBox(self):
        self.BottomBox = QGroupBox()

        self.RunButton = QPushButton(self.tr("Run"))
        self.RunButton.setDefault(True)
        self.RunButton.clicked.connect(self.GETERDONE)

        layout = QVBoxLayout()
        layout.addWidget(self.RunButton)
        layout.addStretch(1)
        self.BottomBox.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
