
import random 

class Agent:
    def __init__(self, i):
        """
        The constructor method. 

        Parameters
        ----------
        i : Integer
            To be unique to each instance.

        Returns
        -------
        None.

        """
        self.i = i 
        self.x = random.randint(0, 99)
        self.y = random.randint(0, 99)
        pass 
    def __str__(self):
        return self.__class__.__name__ + "(i=" + str(self.i) + ", x=" + str(self.x) + ", y=" + str(self.y) + ")"  
    def __repr__(self):
        return str(self)
    def move(self, x_min, y_min, x_max, y_max): 
            # x-coordinate
            rn = random.random()
            #print("rn", rn)
            if rn < 0.5:
                self.x = self.x + 1
            else:
                self.x = self.x - 1
            # y-coordinate
            rn = random.random()
            #print("rn", rn)
            if rn < 0.5:
                self.y = self.y + 1
            else:
                self.y = self.y - 1
        

            
        