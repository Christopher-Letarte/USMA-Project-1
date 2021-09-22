from graphics import *

def toggle(grid_state, row, column):
    if grid_state[row][column] == 1:
        grid_state[row][column] = 0
    else:
        grid_state[row][column] = 1
    return grid_state


def initial_conditions():
    import math
    row = []
    grid_state = []
    for i in range(15):
        row.append(0)
    for i in range(15):
        grid_state.append(row)
    initial_condition = True
    while initial_condition == True:
        win = GraphWin("2D ConwaysGameOfLife",700,700)
        win.setCoords(0,0,15,15)
        for i in range(15):
            for j in range(15):
                rect = Rectangle(Point(i,j),Point(i+1,j+1))
                if grid_state[i][j] == 1:
                    rect.setFill('blue')
                if i == 0 and j == 14:
                    rect.setFill('green')
                rect.draw(win)
        p = win.getMouse()
        px = math.floor(p.getX())
        py = math.floor(p.getY())
        if px == 0 and py == 14:
            initial_condition = False
            win.close()
        else:
            toggle(grid_state,px,py)
            win.close()
    return grid_state
print(initial_conditions())
