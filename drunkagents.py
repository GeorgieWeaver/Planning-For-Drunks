"""
Author = Georgina Weaver

Core Programming for GIS - Andy Evans, University of Leeds

Create and define a class that contains the drunk people who live in the town
They will leave the pub and try and find their own house

"""



import random



# Set the drunk agents' intial location to the pub, where they will then move from 
# Also ensure that they each have a house number, and that they interact with the environment
# They know they are not home, and thus must carry on moving until they reach their destination

class Drunk():
    def __init__(self, environment, drunks, house):
        """ Set the parameters for the drunks class in the model"""
        self.x = 140
        self.y = 150
        self.environment = environment
        self.drunks = drunks
        self.house = house
        self.home = False  
        


# Moving each drunk at random around the environment when the model is run 

    def move(self): 
         """ Make the agents move randomly around the environment"""
        if random.random() < 0.5:
            self.y = (self.y +1) % len(self.environment)
        else:
            self.y = (self.y -1) % len(self.environment)
        
        if random.random() < 0.5:
            self.x = (self.x +1) % len(self.environment)
        else:
            self.x = (self.x -1) % len(self.environment)
