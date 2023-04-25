#PLC as a class
from WaysideController.TestGenericWayside import Wayside
from WaysideController.NewGreenLine import *
#GreenLine
Gswitch1True=[]
Gswitch1False=[]
Gswitch2True=[]
Gswitch2False=[]
Gswitch3True=[]
Gswitch3False=[]
Gswitch4True=[]
Gswitch4False=[]
Gswitch5True=[]
Gswitch5False=[]
Gswitch6True=[]
Gswitch6False=[]
Ggate=[]
#Signal lights Green line
GLight1=[]
GLight13=[]
GLight77=[]
GLight100=[]
GLight84=[]
#Red Line
Rswitch1True=[]
Rswitch1False=[]
Rswitch2True=[]
Rswitch2False=[]
Rswitch3True=[]
Rswitch3False=[]
Rswitch4True=[]
Rswitch4False=[]
Rswitch5True=[]
Rswitch5False=[]
Rswitch6True=[]
Rswitch6False=[]
Rswitch7True=[]
Rswitch7False=[]
Rgate=[]
class PLC():
    def __init__(self,Wayside1,Wayside2,Line): 
        self.Wayside1 = Wayside1
        self.Wayside2 = Wayside2
        self.Line    = Line
    
    def GloadValues1(self,filename):
        file = open(filename, "r")
        for i in range(0,100):
            line=file.readline()
            line=line.strip()
            #TruePath        
            if(line=="ocT1"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]
                Gswitch1True.append(logic)
            if(line=="ocT2"):
                line=file.readline()
                line=line.strip()              
                logic=self.Wayside1.occupancy[int(line)]
                Gswitch2True.append(logic)
            if(line=="ocT3"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]               
                Gswitch3True.append(logic)
            if(line=="ocT4"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]              
                Gswitch4True.append(logic)
            if(line=="ocT5"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]
                Gswitch5True.append(logic)
            if(line=="ocT6"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]
                Gswitch6True.append(logic)
            # False Path
            if(line=="ocF1"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]
                Gswitch1False.append(logic)
            if(line=="ocF2"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]
                Gswitch2False.append(logic)
            if(line=="ocF3"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]
                Gswitch3False.append(logic)
            if(line=="ocF4"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]
                Gswitch4False.append(logic)
            if(line=="ocF5"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]
                Gswitch5False.append(logic)
            if(line=="ocF6"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]
                Gswitch6False.append(logic)
            #signal lights
            if(line=="ocS1"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]
                GLight1.append(logic)
            if(line=="ocS13"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]
                GLight13.append(logic)                            
            if(line=="ocS77"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]
                GLight77.append(logic)
            if(line=="ocS100"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]
                GLight100.append(logic)
            if(line=="ocS84"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]
                GLight84.append(logic)                                
        file.close()

    def GloadValues2(self,File2):
        file = open(File2, "r")
        for i in range(0,100):
            line=file.readline()
            line=line.strip()
            #TruePath        
            if(line=="ocT1"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside2.occupancy[int(line)]
                Gswitch1True.append(logic)
            if(line=="ocT2"):
                line=file.readline()
                line=line.strip()              
                logic=self.Wayside2.occupancy[int(line)]
                Gswitch2True.append(logic)
            if(line=="ocT3"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside2.occupancy[int(line)]               
                Gswitch3True.append(logic)
            if(line=="ocT4"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside2.occupancy[int(line)]              
                Gswitch4True.append(logic)
            if(line=="ocT5"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside2.occupancy[int(line)]
                Gswitch5True.append(logic)
            if(line=="ocT6"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside2.occupancy[int(line)]
                Gswitch6True.append(logic)
            # False Path
            if(line=="ocF1"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside2.occupancy[int(line)]
                Gswitch1False.append(logic)
            if(line=="ocF2"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside2.occupancy[int(line)]
                Gswitch2False.append(logic)
            if(line=="ocF3"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside2.occupancy[int(line)]
                Gswitch3False.append(logic)
            if(line=="ocF4"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside2.occupancy[int(line)]
                Gswitch4False.append(logic)
            if(line=="ocF5"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside2.occupancy[int(line)]
                Gswitch5False.append(logic)
            if(line=="ocF6"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside2.occupancy[int(line)]
                Gswitch6False.append(logic)
        file.close()

    def setswitches(self):
        
        for i in Gswitch1True:
            if(Gswitch1True[i]==True):
                self.Wayside1.setSwitchPositions(False,1)
                self.Wayside2.setSwitchPositions(False,1)


        for i in Gswitch1False:
            if(Gswitch1False[i]==True):
                self.Wayside1.setSwitchPositions(True,1)
                self.Wayside2.setSwitchPositions(True,1)

                
        for i in Gswitch2True:
            if(Gswitch2True[i]==True):
                self.Wayside1.setSwitchPositions(False,2)
                self.Wayside2.setSwitchPositions(False,2)

        for i in Gswitch2False:
            if(Gswitch2False[i]==True):
                self.Wayside1.setSwitchPositions(True,1)
                self.Wayside2.setSwitchPositions(True,1)

    #Always go to yard maybe change later
        self.Wayside1.setSwitchPositions(True,3)
        self.Wayside1.setSwitchPositions(False,4)
        self.Wayside2.setSwitchPositions(True,3)
        self.Wayside2.setSwitchPositions(False,4)

        for i in Gswitch5True:
            if(Gswitch5True[i]==True):
                self.Wayside1.setSwitchPositions(False,5)
                self.Wayside2.setSwitchPositions(False,5)

        for i in Gswitch5False:
            if(Gswitch5False[i]==True):
                self.Wayside1.setSwitchPositions(True,5)
                self.Wayside2.setSwitchPositions(True,5)

        for i in Gswitch6True:
            if(Gswitch6True[i]==True):
                self.Wayside1.setSwitchPositions(False,6)
                self.Wayside2.setSwitchPositions(False,6)
                
        for i in Gswitch6False:
            if(Gswitch6False[i]==True):
                self.WaysideControllerGreen1.setSwitchPositions(True,6)
                self.Wayside2.setSwitchPositions(True,6)
 
        for i in Ggate:
            if(Ggate[i]==True): 
                self.Wayside1.setGatePositions(False)
                self.Wayside2.setGatePositions(False)
                break
            else:
                self.Wayside1.setGatePositions(True)
                self.Wayside2.setGatePositions(True)
                #set Lights

        for i in GLight1:
            if(GLight1[i]==True):
                self.Wayside1.setSignalLights(False,1)
                break
            else:
                self.Wayside1.setSignalLights(True,1)

        for i in range(0,len(GLight13)):
            if(GLight13[i]==True):
                self.Wayside1.setSignalLights(False,13)
                break
            else:
                self.Wayside1.setSignalLights(True,13)
        
        for i in GLight77:
            if(GLight77[i]==True):
                self.Wayside1.setSignalLights(False,77)
                break
            else:
                self.Wayside1.setSignalLights(True,77)
        
        for i in GLight100:
            if(GLight100[i]==True):
                self.Wayside1.setSignalLights(False,100)
                break
            else:
                self.Wayside1.setSignalLights(True,100)
        Gswitch1True.clear()
        Gswitch1False.clear()
        Gswitch2True.clear()
        Gswitch2False.clear()
        Gswitch3True.clear()
        Gswitch3False.clear()
        Gswitch4True.clear()
        Gswitch4False.clear()
        Gswitch5True.clear()
        Gswitch5False.clear()
        Gswitch6True.clear()
        Gswitch6False.clear()
        GLight1.clear()
        GLight13.clear()
        GLight77.clear()
        GLight84.clear()
        GLight100.clear()
    def RloadValues1(self,file):
        file = open(file, "r")
        for i in range(0,100):
            line=file.readline()
            line=line.strip()
            #TruePath        
            if(line=="auT1"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]
                Rswitch1True.append(logic)
            if(line=="auT2"):
                line=file.readline()
                line=line.strip()              
                logic=self.Wayside1.occupancy[int(line)]
                Rswitch2True.append(logic)
            if(line=="auT3"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]               
                Rswitch3True.append(logic)
            if(line=="auT4"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]              
                Rswitch4True.append(logic)
            if(line=="auT5"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]
                Rswitch5True.append(logic)
            if(line=="auT6"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]
                Rswitch6True.append(logic)
            if(line=="auT7"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]
                Rswitch7True.append(logic)            
            # False Path
            if(line=="auF1"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]
                Rswitch1False.append(logic)
            if(line=="auF2"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]
                Rswitch2False.append(logic)
            if(line=="auF3"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]
                Rswitch3False.append(logic)
            if(line=="auF4"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]
                Rswitch4False.append(logic)
            if(line=="auF5"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]
                Rswitch5False.append(logic)
            if(line=="auF6"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]
                Rswitch6False.append(logic)
            if(line=="auF7"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside1.occupancy[int(line)]
                Rswitch7False.append(logic)                
        file.close()

    def RloadValues2(self,file):
        file = open(file)
        for i in range(0,100):
            line=file.readline()
            line=line.strip()
            #TruePath        
            if(line=="auT1"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside2.occupancy[int(line)]
                Rswitch1True.append(logic)
            if(line=="auT2"):
                line=file.readline()
                line=line.strip()              
                logic=self.Wayside2.occupancy[int(line)]
                Rswitch2True.append(logic)
            if(line=="auT3"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside2.occupancy[int(line)]               
                Rswitch3True.append(logic)
            if(line=="auT4"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside2.occupancy[int(line)]              
                Rswitch4True.append(logic)
            if(line=="auT5"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside2.occupancy[int(line)]
                Rswitch5True.append(logic)
            if(line=="auT6"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside2.occupancy[int(line)]
                Rswitch6True.append(logic)
            if(line=="auT7"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside2.occupancy[int(line)]
                Rswitch7True.append(logic)                
            # False Path
            if(line=="auF1"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside2.occupancy[int(line)]
                Rswitch1False.append(logic)
            if(line=="auF2"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside2.occupancy[int(line)]
                Rswitch2False.append(logic)
            if(line=="auF3"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside2.occupancy[int(line)]
                Rswitch3False.append(logic)
            if(line=="auF4"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside2.occupancy[int(line)]
                Rswitch4False.append(logic)
            if(line=="auF5"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside2.occupancy[int(line)]
                Rswitch5False.append(logic)
            if(line=="auF6"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside2.occupancy[int(line)]
                Rswitch6False.append(logic)
            if(line=="auF7"):
                line=file.readline()
                line=line.strip()
                logic=self.Wayside2.occupancy[int(line)]
                Rswitch7False.append(logic)                
        file.close()

    def Rsetswitches(self):
        for i in Rswitch1True:
            if(Rswitch1True[i]==False):
                self.Wayside1.switches[1]=False
                self.Wayside2.switches[1]=False
        for i in Rswitch1False:
            if(Rswitch1False[i]==False):
                self.Wayside1.switches[1]=True
                self.Wayside2.switches[1]=True
        for i in Rswitch2True:
            if(Rswitch2True[i]==False):
                self.Wayside1.switches[2]=False
                self.Wayside2.switches[2]=False
        for i in Rswitch2False:
            if(Rswitch2False[i]==False):
                self.Wayside1.switches[2]=True
                self.Wayside2.switches[2]=True
        for i in Rswitch3True:
            if(Rswitch3True[i]==False):
                self.Wayside1.switches[3]=False
                self.Wayside2.switches[3]=False
        for i in Rswitch3False:
            if(Rswitch3False[i]==False):
                self.Wayside1.switches[3]=True
                self.Wayside2.switches[3]=True
        for i in Rswitch4True:
            if(Rswitch4True[i]==False):
                self.Wayside1.switches[4]=False
                self.Wayside2.switches[4]=False
        for i in Rswitch4False:
            if(Rswitch4False[i]==False):
                self.Wayside1.switches[4]=True
                self.Wayside2.switches[4]=True
        for i in Rswitch5True:
            if(Rswitch5True[i]==False):
                self.Wayside1.switches[5]=False
                self.Wayside2.switches[5]=False
        for i in Rswitch5False:
            if(Rswitch5False[i]==False):
                self.Wayside1.switches[5]=True
                self.Wayside2.switches[6]=True
        for i in Rswitch6True:
            if(Rswitch6True[i]==False):
                self.Wayside1.switches[6]=False
                self.Wayside2.switches[6]=False
        for i in Rswitch6False:
            if(Rswitch6False[i]==False):
                self.Wayside1.switches[6]=True
                self.Wayside2.switches[6]=True
        self.Wayside1.switches[7]=True
        self.Wayside2.switches[7]=True
        if(self.Wayside1.occupancy[46]==True|self.Wayside1.occupancy[48]==True|self.Wayside1.occupancy[49]==True):
            self.Wayside1.gates[1]=False
            self.Wayside1.gates[1]=False
        else:
            self.Wayside1.gates[1]=True
            self.Wayside2.gates[1]=True
        Rswitch1True.clear()    
        Rswitch1False.clear()
        Rswitch2True.clear()
        Rswitch2False.clear()
        Rswitch3True.clear()
        Rswitch3False.clear()
        Rswitch4True.clear()
        Rswitch4False.clear()
        Rswitch5True.clear()
        Rswitch5False.clear()
        Rswitch6True.clear()
        Rswitch6False.clear()
        Rswitch7True.clear()
        Rswitch7False.clear()        