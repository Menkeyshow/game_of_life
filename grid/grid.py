import numpy as np
class game_grid(object):
    def __init__(self, size=10, wrap_around=True, state=None):
        self.size = (size,size)
        self.wrap_around = wrap_around

        if(state is None):
            self.grid = np.zeros(self.size, dtype=int)
        else:
            self.set_state(state)

    def set_state(self, state):
        """
        Edits an game_grid object with given state.
        Must be of the same size.
        """
        if(np.shape(state) == self.size):
            self.grid = np.array(state)
        else:
            raise Exception('The entered board-state doesn\'t '
                            'match the given size: %s.' % str(self.size))

    def get_number_neighbours_of_cell(self, x_cell, y_cell):
        """
        Given the indices of a cell, checks how many alive neighbours there are.
        """
        number_alive_neighbours = 0
        
        # neighbour indices
        x_indices = [x_cell-1, x_cell, x_cell+1]
        y_indices = [y_cell-1, y_cell, y_cell+1]


            #TODO: use functional programming
            #x_indices = list(filter(lambda x: x < 0 and x > self.size[0], x_indices))
            #y_indices = list(filter(lambda y: y < 0 and y > self.size[1], y_indices))
            
        # chose between open borders or closed ones
        if self.wrap_around:
            for indices in [x_indices, y_indices]:
                if -1 in indices:
                    indices.remove(-1)
                    indices.append(self.size[0] - 1)
                if self.size[0] in indices:
                    indices.remove(self.size[0])
                    indices.append(0)
        else:
            for indices in [x_indices, y_indices]:
                if -1 in indices:
                    indices.remove(-1)
                if self.size[0] in indices:
                    indices.remove(self.size[0])


        # check each neighbour and add to counter
        for x in x_indices:
            for y in y_indices:
                number_alive_neighbours = number_alive_neighbours + self.grid[x][y]

        # dont count own value
        number_alive_neighbours = number_alive_neighbours - self.grid[x_cell][y_cell]

        return number_alive_neighbours

    def next_state_of_cell(self, x_cell, y_cell):
        neighbours = self.get_number_neighbours_of_cell(x_cell, y_cell)
        if(self.grid[x_cell][y_cell] == 1):
            #Any live cell with more than three live neighbours dies, as if by overpopulation.
            if(neighbours > 3):
                return 0
            #Any live cell with fewer than two live neighbours dies, as if by underpopulation.
            elif(neighbours < 2):
                return 0
            #Any live cell with two or three live neighbours lives on to the next generation.
            else:
                return 1
        if(self.grid[x_cell][y_cell] == 0):
            #Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
            if(neighbours == 3):
                return 1
            else:
                return 0
        
    def next_state_of_grid(self):
        new_grid = np.zeros_like(self.grid)

        for x in range(self.size[0]):
            for y in range(self.size[0]):
                new_grid[x][y] = self.next_state_of_cell(x,y)
        
        self.set_state(new_grid)




if __name__ == "__main__":
    game = game_grid()
    print(game.grid)
    game2 = game_grid(
            state= [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0]])
    print(game2.grid)
    game2.next_state_of_grid()
    print(game2.grid)
    def faulty_state():
        game2 = game_grid(
            state= [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [1,2,3]])
        print(game2.grid)
    #faulty_state()

