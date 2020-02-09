from game_logic.board_logic import board_logic
from gui.gui import gui
import time


if __name__ == "__main__":
    game_logic = board_logic(board_state=  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 1, 1, 1, 0, 0, 0, 0, 0]])
    game_gui = gui(game_logic.board_state)

    #TODO: use events and eventlisteners!
    while(game_gui.app_running):
        game_gui.root.update()
        game_gui.root.update_idletasks()
        game_gui.update_cell_buttons() #update gui

        
        while(game_gui.auto_update_state):
            game_gui.root.update()
            game_gui.root.update_idletasks()

            game_logic.set_state(game_gui.board_state) # GUI => LOGIC
            game_logic.calculate_next_board_state() # LOGIC calculates
            game_gui.board_state = game_logic.board_state # LOGIC => GUI
            game_gui.update_cell_buttons() # GUI update
            #time.sleep(0.1)






