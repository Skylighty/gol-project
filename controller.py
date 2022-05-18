import pygame
from eventmanager import *

# Handling controls from keyboard
# evManager is necessary for reading ticks and posting input events
class Keyboard(object):
    def __init__(self, evManager, model):
        self.evManager = evManager
        evManager.RegisterListener(self)
        self.model = model

    # Reads event list from evManager
    def notify(self, event):
        if isinstance(event, TickEvent):
            # Called for each game tick. We check our keyboard presses here.
            for event in pygame.event.get():
                # Handle window close input from windows manager
                if event.type == pygame.QUIT:
                    self.evManager.Post(QuitEvent())
                # Handle keyboard input 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.evManager.Post(QuitEvent())
                    elif event.key == pygame.K_RETURN:
                        self.evManager.Post(StartGame())
                    elif event.key == pygame.K_SPACE:
                        self.evManager.Post(GamePauseEvent())