# tests file for TrainControllerSW

from distutils.cmd import Command
import sys
from TrainControllerSW import TrainControllerSW
import json

class TestClass:
    def __init__(self, test1, test2):
        self.test1 = test1
        self.test2 = test2

    def printTest1(self):
        print(self.test1)

TestObj = TestClass(5, "test2")
print(json.dumps(TestObj.__dict__))

TrainControllerSW_ = TrainControllerSW(None, None, None, None, None, None, None, None, None, None, None, None, None, 
                                       None, None, None, None, None, None, None, None, None, None, None, None, None, 
                                       None, None)

TrainControllerSW_.writeOutputs()
TrainControllerSW_.readInputs(TrainControllerSW_)
