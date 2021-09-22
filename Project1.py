#%%
'''
Problem 1
'''
#Part 1
def identify_rules(input_number):
    input_binary = bin(input_number)
    input_binary_list = []
    for i in range(len(input_binary)):
        input_binary_list.append(input_binary[i])
    input_binary_list = input_binary_list[2:]
    while len(input_binary_list) < 8:
        input_binary_list.insert(0,'0')
    for i in range(len(input_binary_list)):
        input_binary_list[i] = int(input_binary_list[i])
    return input_binary_list
#identify_rules(175)
# %%
#Part 2
def next_state(previous_state, rules_dictionary):
    possible_states = [[1,1,1],[1,1,0],[1,0,1],[1,0,0],[0,1,1],[0,1,0],[0,0,1],[0,0,0]]
    threes_previous = []
    previous_state.insert(0,0)
    previous_state.insert(0,0)
    previous_state.append(0)
    previous_state.append(0)
    for i in range(len(previous_state)-2):
        threes_previous.append([previous_state[i],previous_state[i+1],previous_state[i+2]])
    NextState = []
    #index each set of three then add the according rule
    for i in range(len(threes_previous)):
        rule_index = possible_states.index(threes_previous[i])
        NextState.append(rules_dictionary[rule_index])
    return NextState
next_state(previous_state = [1], rules_dictionary = identify_rules(175))

# %%
#part 3
def initial_condition(iterations):
    if type(iterations) != int:
        return 'Error, please enter an integer number of iterations'
    output_list = []
    first_line = []
    for i in range(iterations):
        first_line.append(0)
    first_line.append(1)
    for i in range(iterations):
        first_line.append(0)
    output_list.append(first_line)
    for i in range(iterations):
        intermediate_list = []
        for i in range(iterations*2+1):
            intermediate_list.append(0)
        output_list.append(intermediate_list)
    if type(iterations) != int:
        return 'Error, please enter an integer number of iterations'
    return output_list
#initial_condition(3)    
            
        

#%%
#Part 4
def one_dimension(iterations, rules_library):
    framework_with_impulse = initial_condition(iterations)
    impulse = [1]
    for i in range(iterations+1):
        temporary_row = []
        for j in range(iterations-i):
            temporary_row.append(0)
        for j in range(len(impulse)):
            temporary_row.append(impulse[j])
        for k in range(iterations-i):
            temporary_row.append(0)
        framework_with_impulse[i] = temporary_row
        impulse = next_state(impulse,rules_library)
    return framework_with_impulse
one_dimension(iterations = 3, rules_library = identify_rules(175))


# %%
#part 5
from graphics import *
def visual_one_dimension(iterations, rules_library):
    win = GraphWin("1D ConwaysGameOfLife",700,700)
    win.setCoords(0,0,2*iterations+1,iterations+1)
    one_dimension_matrix = one_dimension(iterations, rules_library)
    for i in range(len(one_dimension_matrix)):
        for j in range(len(one_dimension_matrix[i])):
            rect = Rectangle(Point(j,iterations - (i)),Point(j+1,iterations - (i-1)))
            if one_dimension_matrix[i][j] == 1:
                rect.setFill('blue')
            rect.draw(win)
    p = win.getMouse()
    if p.getX() < 400:
        win.close()
visual_one_dimension(iterations = 50, rules_library = identify_rules(175))

# %%
#Part 6




# %%
'''
Problem 2
'''
# %%
#Part 7
from graphics import *

row = []
zero_matrix = []
for i in range(15):
    row.append(0)
for i in range(15):
    zero_matrix.append(row)
win = GraphWin("2D ConwaysGameOfLife",700,700)
win.setCoords(0,0,15,15)
#draw the horizontal lines
for i in range(15):
    for j in range(15):
        rect = Rectangle(Point(i,j),Point(i+1,j+1))
        rect.draw(win)
p = win.getMouse()
if p.getX() < 400:
    win.close()


# %%
#Part 8

row = []
interactive_matrix = []
for i in range(15):
    row.append(0)
for i in range(15):
    interactive_matrix.append(row)
win = GraphWin("2D ConwaysGameOfLife",700,700)
win.setCoords(0,0,15,15)
#draw the horizontal lines
for i in range(len(interactive_matrix)):
    for j in range(len(interactive_matrix[i])):
        rect = Rectangle(Point(i,j),Point(i+1,j+1))
        if interactive_matrix[i][j] == 1:
            rect.fill('blue')
        rect.draw(win)
p = win.getMouse()
def toggle
if p.getX() < 400:
    win.close()
# %%
