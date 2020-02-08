import tkinter as tk
import numpy as np


class gui(object):
    def __init__(self, state):
        self.state = state
        self.cells = np.zeros_like(self.state, dtype=object)
        self.update = False
    
        self.root = tk.Tk()
        self.root.title("Conway's Game of Life")
        self.master = tk.Frame(self.root)
        self.master.pack()
        self.update_checkbox = tk.Checkbutton(self.root, text="Let Life flow", variable=self.update)
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

                cellbutton = tk.Button(cellframe, bg='gray25', fg='red2', command=lambda: self.button_press(x,y))
                cellbutton.grid(sticky='wens') #expanding buttons
                self.cells[x][y] = cellbutton
                

                #self.cells[x][y] = tk.Button(self.master, bg='gray25', fg='red2', padx=1, pady=1, height=5, width=5)
                #self.cells[x][y].grid(row=x, column=y)
    
    def update_cells(self):
        pass

    def button_press(self, x, y):
        button = self.cells[x][y]
        button.config(bg='red2')


        


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
    game_gui.root.mainloop()
