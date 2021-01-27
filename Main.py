import HumanDataBase
import time

HumanDataBase.Initialize()

HumanDataBase.PrintHumanStats()

while(True):
    HumanDataBase.Simulate()
    HumanDataBase.PrintHumanStats()
    time.sleep(1)

