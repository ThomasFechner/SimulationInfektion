

class HumanStat():

    class Position():
        
        X: float
        Y: float

        def __init__(self):

            self.X = X
            self.Y = Y

    Origin: Position
    CurrentPosition: Position
    Destination: Position
    Speed: float
    Angle: float
    StopRadius: float
    StopAngle: float

    def __init__(self):

        self.Origin = Origin
        self.CurrentPosition = CurrentPosition
        self.Destination = Destination
        self.Speed = Speed
        self.Angle = Angle
        self.StopRadius = StopRadius
        self.StopAngle = StopAngle

    #OriginX: int
    #OriginY: int

    #CurrentPositionX: int
    #CurrentPositionY: int

    #DestinationX: int
    #DestinationY: int




class HumanConfig():
    
    MaxDestinationRadius: int
    
    MaxSpeed: int
    MinSpeed: int
    
    RadiusFar: int
    RadiusNear: int
    
    Acceleration: int
    
    InfectRadius: int
    IncarnationTime: int

class HumanClass():

    HumanID: int
    maxX: int
    maxY: int
    TimeDelay: int
    TimeStamp: int
    LastMovTime: int
    SpeedHuman: int   #besserer Name




