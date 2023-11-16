import time 
class MyShape:
    def __init__(self,side ,length, width ,radius):
        self.side = side #邊
        self.length = length #長
        self.width = width #寬
        self.radius = radius #半徑
    
    def getSquareArea(self):
        print("SquareArea is :", end = " ")
        print(self.side*self.side)

    def getRectangleArea(self):
        print("RectangleArea is :", end = " ")
        print(self.length*self.width)

    def getCircleArea(self):
        print("CircleArea is :", end = " ")
        print(self.radius*self.radius*3.14)

print("Loading" , end = " ")
for i in range(10) : 
    print(".",end = '', flush= True)
    time.sleep(0.2)
print("\n")

shape = MyShape(5,6,7,8)

shape.getSquareArea()
shape.getRectangleArea()
shape.getCircleArea()
        
