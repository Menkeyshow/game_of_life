from grid.grid import grid
from gui.gui import gui
import time


if __name__ == "__main__":
    game_grid = grid(state=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0]])
    game_gui = gui(game_grid.grid)


    while(game_gui.running):
        game_gui.root.update()
        game_gui.root.update_idletasks()
        game_gui.update_cells() #update gui
        print(game_gui.update)
        
        while(game_gui.update):
            game_gui.root.update()
            game_gui.root.update_idletasks()

            game_grid.set_state(game_gui.state) #get from gui
            game_grid.next_state_of_grid() #calc next state
            game_gui.state = game_grid.grid #get from grid
            game_gui.update_cells() #update gui
            time.sleep(0.1)
            print(game_gui.update)





