import tkinter as tk
import numpy as np
#from ..grid.grid import gamegrid


class gui(object):
    def __init__(self, state):
        self.state = state
        self.cells = np.zeros_like(self.state, dtype=object)
        self.update = False
        self.running = True
        self.root = tk.Tk()
        self.root.title("Conway's Game of Life")
        self.master = tk.Frame(self.root)
        self.master.pack()
        self.update_checkbox = tk.Button(self.root, text="Let Life flow", command=(lambda:self.update_runner()))
        self.update_checkbox.pack()
        self.create_cells()

    def create_cells(self):
        for x in range(np.shape(self.state)[0]):
            for y in range(np.shape(self.state)[1]):
                cellframe = tk.Frame(self.master, height=20, width=20)
                cellframe.grid_propagate(False) #disables resizing of frame
                cellframe.columnconfigure(0, weight=1) #enables button to fill frame
                cellframe.rowconfigure(0,weight=1) #any positive number would do the trick  
                cellframe.grid(row=x, column=y)

                cellbutton = tk.Button(cellframe, bg='gray25', command=(lambda x=x, y=y: self.button_press(x,y)))
                cellbutton.grid(sticky='wens') #expanding buttons
                self.cells[x][y] = cellbutton
                

                #self.cells[x][y] = tk.Button(self.master, bg='gray25', fg='red2', padx=1, pady=1, height=5, width=5)
                #self.cells[x][y].grid(row=x, column=y)
    
    def update_cells(self):
        for x in range(np.shape(self.state)[0]):
            for y in range(np.shape(self.state)[1]):
                cell_status = self.state[x][y]
                if cell_status == 1:
                    self.cells[x][y].config(bg='red2')
                if cell_status == 0:
                    self.cells[x][y].config(bg='gray25')


    def button_press(self, x, y):
        button = self.cells[x][y]
        cell_status = self.state[x][y]
        if cell_status == 1:
            button.config(bg='gray25')
            self.state[x][y] = 0
        if cell_status == 0:
            button.config(bg="red2")
            self.state[x][y] = 1
    
    def set_state(self, state):
        self.state = state
        self.update_cells()
    
    def update_runner(self):
        self.update = not self.update

        


if __name__ == "__main__":
    game_gui = gui(state=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0]])
    game_gui.update_cells()

    while(game_gui.running):
    
        game_gui.root.update()
        game_gui.root.update_idletasks()
        while(game_gui.update):
            game_gui.update_cells()
