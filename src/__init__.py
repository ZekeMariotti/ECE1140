import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "TrainControllerSoftware"))
sys.path.append(os.path.join(os.path.dirname(__file__), "TrainModel"))

#print(f'Init:{sys.path}')

from TrainControllerSoftware import TrainControllerMainUI
from TrainModel import TrainModelMainUI