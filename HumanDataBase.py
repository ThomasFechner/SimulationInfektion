import uuid
#import dataclasses
import random
import time
import math
import datetime


#region HumanStat - Daten zum Darstellen in der GUI
class HumanStat():

    class Position():
        X: float
        Y: float

        def __init__(self, X, Y):
            self.X = X
            self.Y = Y

    Origin: Position  #Herkunft
    CurPos: Position  #Current Position
    Destination: Position  #Ziel
    Speed: float
    Angle: float   #Winkel zu Destination
    StopRadius: float
    StopAngle: float

    def __init__(self):

        self.Origin = self.Position(0.0, 0.0)
        self.CurPos = self.Position(0.0, 0.0)
        self.Destination = self.Position(0.0, 0.0)

#endregion



#region HumanConfig - Configuration eines Objekts
class HumanConfig():
    
    MaxSpeed: float
    MinSpeed: float
    
    RadiusFar: float
    RadiusNear: float
    
    Acceleration: float

    MaxDistance: float
    
    #InfectRadius: float
    #IncarnationTime: float

    def __init__(self, MaxSpeed, MinSpeed, RadiusFar, RadiusNear, Acceleration, MaxDistance):
        self.MaxSpeed = MaxSpeed
        self.MinSpeed = MinSpeed
        self.RadiusFar = RadiusFar
        self.RadiusNear = RadiusNear
        self.Acceleration = Acceleration
        self.MaxDistance = MaxDistance

#endregion

#region Human - Klasse um die Bewegung und die Gesundheit der Objekte zu simulieren
class Human():

    guid: str  #zufälliger Name für Objekte
    Status: HumanStat  #Satus Daten
    Config: HumanConfig  #Daten zur Konfiguration 

    HumanID: int
    maxX: float
    maxY: float
    TimeDelay: float
    TimeStamp: datetime.date
    LastMovTime: datetime.date
    SpeedHuman: float   

 

    def __init__(self, srcx, srcy, dstx, dsty):
        self.Status = HumanStat()
        self.guid = uuid.uuid4()
        if srcx == 0 and srcy == 0:
            self.Status.CurPos.X = random.uniform(0.0, 20.0)
            self.Status.CurPos.Y = random.uniform(0.0, 20.0)
        else:
            self.Status.CurPos.X = srcx
            self.Status.CurPos.Y = srcy

        if dstx == 0 and dsty == 0:
            self.Status.Destination.X = random.uniform(0.0, 20.0)
            self.Status.Destination.Y = random.uniform(0.0, 20.0)
        else:
            self.Status.Destination.X = dstx
            self.Status.Destination.Y = dsty
        self.Status.Origin.X = self.Status.CurPos.X
        self.Status.Origin.Y = self.Status.CurPos.Y

        self.Config = HumanConfig(1.5, 0.5, 0.05, 1.0, 0.5, 50)
        self.Speed = random.uniform(self.Config.MinSpeed, self.Config.MaxSpeed)

        self.TimeDelay = 0.0
        self.TimeStamp = datetime.datetime.now()
        self.SpeedHuman = self.Speed
        self.LastMovTime = datetime.datetime.now()

    def GetGuid(self):
        return self.guid

    #Zeitstempel für Zeitraffer bestimmen
    FicTime = 0  #Fictional Time
    def TimeStamp():   
        #für 50 Tage in 5 Minuten
        #FicTime = (TimeStart - TimeEnd) * 14400  #?
        FicTime = TimeEnd - TimeStart

    
    def Go(self):
        #region Zeitstempel Zeitdifferenz berechnen
        timedelta = datetime.datetime.now() - self.TimeStamp
        self.TimeDelay = timedelta.total_seconds()
        self.TimeStamp = datetime.datetime.now()
        #endregion

        #region Berechnung des Winkels Laufrichtung
        DeltaX = self.Status.Destination.X - self.Status.CurPos.X
        DeltaY = self.Status.Destination.Y - self.Status.CurPos.Y
        RadiusDest = math.sqrt(DeltaX**2 + DeltaY**2)
        
        #Winkel der Bewegung berechnen, wenn kein Hindernis
        self.Status.Angle = (math.acos(DeltaX / RadiusDest)) * 180 / math.pi
        if DeltaY < 0:
           self.Status.Angle = self.Status.Angle * (-1)
        #endregion

        #region Berechnung der Schrittweite
        DeltaRadius = self.TimeDelay * self.SpeedHuman / 1000
        DeltaX = DeltaRadius * math.cos(self.Status.Angle / 360 * 2 * math.pi)
        DeltaY = DeltaRadius * math.sin(self.Status.Angle / 360 * 2 * math.pi)

        #DistX = self.Status.Destination.X - self.Status.CurPos.X
        #DistY = self.Status.Destination.Y - self.Status.CurPos.Y
        #DstRad = math.sqrt(math.pow(DistX, 2) + math.pow(DistY, 2))

        if RadiusDest > DeltaRadius:
            self.Status.CurPos.X = self.Status.CurPos.X + DeltaX
            self.Status.CurPos.Y = self.Status.CurPos.Y + DeltaY
        else:
            self.Status.CurPos.X = self.Status.CurPos.X + DistX
            self.Status.CurPos.Y = self.Status.CurPos.Y + DistY

        self.LastMovTime = datetime.datetime.now()
        #endregion

        return (self.Status.CurPos.X, self.Status.CurPos.Y)

    #region Return
    def GetCurrentPosition(self):
        return (self.Status.CurPos.X, self.Status.CurPos.Y)
    #endregion



#endregion

#region 
HumanList = [] #List

def Initialize():

    for x in range(0,1):
        newi = Human(5.0, 5.0, 20.0, 20.0)
        #HumanList[newi.guid] = newi
        HumanList.append(newi)


def PrintHumanStats():
    for humi in HumanList:
        x, y = humi.GetCurrentPosition()
        print(humi.guid)
        print(x)
        print(y)    

def Simulate():
    for humi in HumanList:
        x, y = humi.Go()
        print(humi.guid)
        print(x)
        print(y)    
        


        



