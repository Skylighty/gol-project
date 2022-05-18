# Class to inherit from
# General - for any object that will generate event
class Event(object):
    def __init__(self):
        self.name = "Generic event"
    def __str__(self):
        return self.name

# Quit application event    
class QuitEvent(Event):
    def __init__ (self):
        self.name = "Quit event"

# Event sent by Controller when ENTER is pressed
class StartGame(Event):
    def __init__(self):
        self.name = "Starting the game"

# Event sent by Controller when SPACE is pressed
class GamePauseEvent(Event):
    def __init__(self):
        self.name = "Game Pause/Resume Event"

# Event sent by Model when life mutation is executed
class ArrayModified(Event):
    def __init__(self, array):
        self.name = "Numpy array was modified"
        self.array = array

# Event sent by View, when Model changes are committed to visuals
class ViewUpdated(Event):
    def __init__(self):
        self.name = "View updated from model"

# Tick of the application event    
# Basic clock that allows continuous execution
class TickEvent(Event):
    def __init__ (self):
        self.name = "Tick event"
    
# Class for keyboard or mouse
class InputEvent(Event):
    def __init__(self, unicodechar, clickpos):
        self.name = "Input event"
        self.char = unicodechar
        self.clickpos = clickpos
    def __str__(self):
        return '%s, char=%s, clickpos=%s' % (self.name, self.char, self.clickpos)
    

# Tells all listeners to initialize themselves.
# This includes loading libraries and resources.
# Avoid initializing such things within listener __init__ calls 
# to minimize snafus (if some rely on others being yet created.)
class InitializeEvent(Event):
    def __init__ (self):
        self.name = "Initialize event"

# To coordinate communication between Model, Virew and the Controller
class EventManager(object):
    def __init__(self):
        from weakref import WeakKeyDictionary
        self.listeners = WeakKeyDictionary()

    # Adds observator to spam list
    # It will receive Post()ed events throught notify(event) call.
    def RegisterListener(self, listener):
        self.listeners[listener] = 1

    # Removes listener from spam list
    # It's almost never used
    def UnregisterListener(self, listener):
        if listener in self.listeners.keys():
            del self.listeners[listener]

    # Post event to the event queue
    # Every observator will receive it        
    def Post(self, event):
        # TESTING PURPOSE!!
        '''
        if not isinstance(event, TickEvent):
            # print the event (unless it is TickEvent)
            print(str(event))
        '''
        for listener in self.listeners.keys():
            listener.notify(event)