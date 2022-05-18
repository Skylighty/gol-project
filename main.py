import eventmanager
import model
import view
import controller
import argprs

def run(args):
    evManager = eventmanager.EventManager()
    gamemodel = model.GameEngine(evManager, args.rows, args.columns, args.scale, args.offset, args.fps)
    keyboard = controller.Keyboard(evManager, gamemodel)
    graphics = view.GraphicalView(evManager, gamemodel, args.rows, args.columns)
    gamemodel.run()

if __name__ == '__main__':
    args = argprs.parsing()
    run(args)