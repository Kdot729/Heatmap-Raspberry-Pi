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

        if (Sum >= 0.0) and (Sum <= 0.15):
            Color = self.Red
        elif (Sum > 0.15) and (Sum <= 0.30):
            Color = self.Orange
        elif (Sum > 0.30) and (Sum <= 0.45):
            Color = self.Yellow
        elif (Sum > 0.45) and (Sum <= 0.60):
            Color = self.Green
        elif (Sum > 0.75) and (Sum <= 0.90):
            Color = self.Blue
        elif (Sum > 0.90) and (Sum <= 1.05):
            Color = self.Indigo
        elif (Sum > 1.05) and (Sum <= 1.20):
            Color = self.Violet
        else:
            Color = self.White
        self._Pixel_Color = Color