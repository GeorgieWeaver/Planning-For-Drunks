"""
Author = Georgina Weaver

Core Programming for GIS - Andy Evans, University of Leeds

Modelling drunk people within a town environment to see the routes they take home
They navigate themselves back to their specific house from a central pub within the town

"""



import csv
import random
import drunkagents
import matplotlib 
import matplotlib.pyplot
import matplotlib.animation



# Creating the environment that will represent the town
# Create a list of agents, called drunks, that become the 25 drunk people leaving the pub 

environment = []
drunks = []

num_of_drunks = 25
num_of_iterations = 500



# Add the csv file that shows the pub and houses

f=open('townplan.txt', newline='')
reader=csv.reader (f, quoting = csv.QUOTE_NONNUMERIC)

for row in reader:
    rowlist = []
    for item in row:
        rowlist.append(item)
    environment.append(rowlist)
f.close() 


print(type(environment), len(environment))



# Defining the area for animation, that will become the environment
# Plotting the houses and the pub within this environment 

fig = matplotlib.pyplot.figure(figsize=(9,9))
ax = fig.add_axes([0,0,1,1])

matplotlib.pyplot.xlim(0, 299)
matplotlib.pyplot.ylim(0, 299)


    
# Create the map environment (mapenvironment) in order to map density of each point of the map
# When an agent passes through a point on the map, needs to be calculated, and saved

mapenvironment = []
    
height=len(environment)
width=len(environment[0])

for i in range(height):
    rowlist = []
    for j in range(width):
        rowlist.append(0)
    mapenvironment.append(rowlist)



# Assign the drunks using the class that has been created
# Tell each drunk that their house number is their own agent number plus one, then multiplied by 10

for i in range(num_of_drunks):
    house = (i+1)*10
    drunks.append(drunkagents.Drunk(environment, drunks, house))



# Make each drunk agent move around the environment until they find their home
# If they aren't home, then the drunk will move randomly
# If they haven't reached their home, then add 1 to the environment each time
    
for i in range(num_of_drunks):
    while drunks[i].home==False:
        drunks[i].move()
        mapenvironment[drunks[i].x][drunks[i].y]+=1
    if drunks[i].house==drunks[i].environment[drunks[i].x][drunks[i].y]:
        drunks[i].home==True
        


# Show the animation of the drunks as they move around

carry_on = True
matplotlib.pyplot.xlim(0, 299)
matplotlib.pyplot.ylim(0, 299)

matplotlib.pyplot.imshow(mapenvironment)
matplotlib.pyplot.show()


def update (frame_number):
    """ Creating the animation function """
    fig.clear()
    global carry_on
    
    if random.random() < 0.1:
        carry_on = False


def gen_function(b = [0]):
    """ Creating the animation function """
    a = 0
    global carry_on
    while (a < 10) & (carry_on) :
        yield a		
        a = a + 1
        

animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
matplotlib.pyplot.show()



# Making a Graphical User Interface that displays the model

def run():
    """ Creating the function that will allow the model to be run"""
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    #canvas.show()



# Save the density map to a file as text, using the new environment that was made
# This will show how many drunks pass through each point within the town

f2 = open('densitymap.csv', 'w', newline='')
writer = csv.writer(f2, delimiter=' ')
for row in mapenvironment:
    writer.writerow(row)
f2.close()
