from eventmanager import *
from numpy import ndarray
from random import randint


# evManager (EventManager): Allows posting messages to the event queue.        
# Attributes:
# running (bool): True while the engine is online. Changed via QuitEvent().
class GameEngine(object):
    def __init__(self, evManager, width, height, scale, offset, fps):  
        self.evManager = evManager                      # Pass the evManager
        evManager.RegisterListener(self)                # Registers object for event spam list
        self.started = False                            # Gets True when StartGame() sent
        self.running = False                            # Gets True when pygame.init successfull
        self.scale = scale                              # Scale to include to sizes
        self.columns = int(height/scale)                # No. of columns - height includes scale
        self.rows = int(width/scale)                    # No. of rows - width includes scale
        self.size = (self.rows, self.columns)           # Size of main pygame window
        self.grid_array = ndarray(shape=(self.size))    # Initialize array from size property (array to fill)
        self.offset = offset                            # Offset property value
        self.fps = fps                                  # To pass for view object
        self.initial_randomize_grid()                   # Randomizes starting cell values


    # If gets called by event in message queue
    def notify(self, event):
        if isinstance(event, TickEvent) and self.started == True:
            self.update()
            self.evManager.Post(ArrayModified(self.grid_array))
        elif isinstance(event, StartGame):
            self.started = True
        elif isinstance(event, GamePauseEvent) and self.started == True:
            self.started = False
        elif isinstance(event, GamePauseEvent) and self.started == False:
            self.started = True
            

    # Start the game engine loop.
    # Start tick event into event queue for each loop.
    # Loop ends when object GameEngine hears QuitEvent in notify() method
    def run(self):
        self.running = True
        self.evManager.Post(InitializeEvent())
        while self.running:
            newTick = TickEvent()
            self.evManager.Post(newTick)


    # Method fills grid we work on with random values
    def initial_randomize_grid(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = randint(0,1)

    # Calculates a total number of neighbor cells for cell
    def get_neighbors(self, x, y):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x + n + self.rows) % self.rows
                y_edge = (y + m + self.columns) % self.columns
                total += self.grid_array[x_edge][y_edge]
        total -= self.grid_array[x][y]
        return total

    # Calculates new numpy array - next move of 'life'
    def update(self):
        updated = ndarray(shape=(self.size))
        for x in range(self.rows):
            for y in range(self.columns):
                cell_state = self.grid_array[x][y]
                neighbours = self.get_neighbors(x,y)
                if cell_state == 0 and neighbours == 3:
                    updated[x][y] = 1
                elif cell_state == 1 and (neighbours < 2 or neighbours > 3):
                    updated[x][y] = 0
                else:
                    updated[x][y] = cell_state 
        self.grid_array = updated





