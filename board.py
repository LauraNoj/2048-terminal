class Board:
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.b = []
        for i in range(h*w):
            self.b.append(0)

    def getval(self, x, y):
        idx = self.w*x+y
        return self.b[idx]


    def draw(self):
        for i in range(self.w):
            print("-"),
        print("")
        for x in range(self.h):
            print("|"),
            for y in range(self.w):
                print(self.getval(x, y)),
            print("|")

    def test(self):
        print("TEST")
            
            
        
     
        
