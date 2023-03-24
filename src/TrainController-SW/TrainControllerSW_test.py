# tests file for TrainControllerSW

from distutils.cmd import Command
import sys
from TrainControllerSW import TrainControllerSW
import json



TrainControllerSW_ = TrainControllerSW(None, None, None, None, None, None, None, None, None, None, None, None, None, 
                                       None, None, None, None, None, None, None, None, None, None, None, None, None, 
                                       None, None)

TrainControllerSW_.writeOutputs()
TrainControllerSW_.readInputs()
