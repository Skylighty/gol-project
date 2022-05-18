import pygame
from eventmanager import *

# Draw the current state of model on the screen
class GraphicalView(object):
    def __init__(self, evManager, model, w_width, w_height):
        self.evManager = evManager
        evManager.RegisterListener(self)
        self.model = model                              # Model object
        self.isinitialized = False                      # Check if module is initialized
        self.screen = None                              # Screen surface
        self.clock = None                               # To-be FPS harness
        self.font = None                                # Font set to display controls on window
        self.helptext = None                            # Controls text to be displayed
        self.text_rect = None                           # Rectangle of help text
        self.rect_center = None                         # Center of help text rectangle object
        self.fps = model.fps                            # FPS harness
        self.win_size = (w_width, w_height)             # Size of window to initialize
        self.COL_GREY = (80,83,83)                      # Grey for dead n fill
        self.COL_SEA = (0,161,153)                      # Sea for alive
        self.COL_WHITE = (255,255,255)                  # White for help - controls text
        self.COL_BLACK = (0,0,0)                        # Black for text background
    
    # Allows object to receive events posted to event queue
    def notify(self, event):
        if isinstance(event, InitializeEvent):
            self.initialize(self.model.rows, self.model.columns)
        elif isinstance(event, QuitEvent):
            # shut down the pygame graphics
            self.isinitialized = False
            pygame.quit()
        elif isinstance(event, ArrayModified):
            self.model.grid_array = event.array
            self.draw(event.array)
            self.clock.tick(self.fps)
            self.evManager.Post(ViewUpdated())
        elif isinstance(event, ViewUpdated):
            pygame.display.update()
    
    # Draw current game state on screen
    # Does nothing if isinitialized == False (pygame.init failed)
    def draw(self, array):
        for x in range(self.model.rows):
            for y in range(self.model.columns):
                x_pos = x * self.model.scale
                y_pos = y * self.model.scale
                if array[x][y] == 1:
                    # Paint living cell
                    pygame.draw.rect(self.screen, self.COL_SEA, [x_pos, y_pos, self.model.scale-self.model.offset, self.model.scale-self.model.offset])
                else:
                    # Paint dead cell
                    pygame.draw.rect(self.screen, self.COL_GREY, [x_pos, y_pos, self.model.scale-self.model.offset, self.model.scale-self.model.offset])
        self.screen.blit(self.helptext, self.text_rect)
        
    # Set up the pygame graphical display and load graphical resources
    def initialize(self, w, h):
        result = pygame.init()
        pygame.font.init()
        pygame.display.set_caption('Game of Life MVC by Pawel Gasiewski')
        self.screen = pygame.display.set_mode(self.win_size)
        self.screen.fill(self.COL_GREY)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 20)
        self.helptext = self.font.render('Enter - Start, Space - Pause/Resume, Esc - Quit', True, self.COL_WHITE, self.COL_BLACK)
        self.text_rect = self.helptext.get_rect()
        self.text_rect.center = (self.win_size[0]/2, 10)
        self.screen.blit(self.helptext, self.text_rect)
        pygame.display.update()
        self.isinitialized = True