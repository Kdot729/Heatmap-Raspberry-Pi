class Pixel:

    Red = (255, 0, 0)
    Orange = (255, 165, 0)
    Yellow = (255, 255, 0)
    Green = (0, 128, 0)
    Blue = (0, 0, 255)
    Indigo = (75, 0, 130)
    Violet = (255, 87, 51)
    White = (255, 255, 255)

    Color_Mapping = [Red, Orange, Yellow, Green, Blue, Indigo, Violet]

    Pink = (246, 29, 195)
    
    def __init__(self) -> None:
        pass

    @property
    def Pixel_Color(self) -> tuple[int, int, int]: 
        return self._Pixel_Color
    
    @Pixel_Color.setter 
    def Pixel_Color(self, Sum):

        if (Sum >= 0.0) and (Sum <= 2):
            Color = self.Red
        elif (Sum > 2) and (Sum <= 4):
            Color = self.Orange
        elif (Sum > 4) and (Sum <= 6):
            Color = self.Yellow
        elif (Sum > 6) and (Sum <= 8):
            Color = self.Green
        elif (Sum > 8) and (Sum <= 10):
            Color = self.Blue
        elif (Sum > 10) and (Sum <= 12):
            Color = self.Indigo
        elif (Sum > 12) and (Sum <= 14):
            Color = self.Violet
        else:
            Color = self.White
        self._Pixel_Color = Color