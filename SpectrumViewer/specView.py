import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons
class SpecView:
    def __init__(self,filename):
        self.figure = plt.figure(filename, figsize=(10, 8), dpi=100)

        #self.graphAx = self.figure.add_subplot(212)
        self.graphAx = self.figure.add_subplot(111)
        self.graphAx.set_xlabel('lambda/Å')
        self.graphAx.set_ylabel('10-17 ergs/s/cm2/Å')
        self.graphAx.set_ylim([0, 500])
        #self.tableAx = self.figure.add_subplot(211)
        #self.tableAx.axis('tight')
        #self.tableAx.axis('off')

        self.rax = plt.axes([0.00, 0.05, 0.10, 0.15])
        self.checkBtns = CheckButtons(self.rax, ('Skyline',
                                                 'Flux',
                                                 'Model',
                                                 'Emission',
                                                 'Absorption',
                                                 'A or E',
                                                 'Other'),
                                      (True, True, True,True,True,True,True))
    def show(self):


        plt.show()