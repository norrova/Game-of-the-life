import random
import os

#region Level 1
def initialization(size_map):
    cells_alive = []
    for index_x in range(size_map):
        for index_y in range(size_map):
            cursor = random.randrange(0, 100)
            if cursor >=  random.randrange(0, 100):
                cells_alive.append([index_x, index_y])
    return cells_alive

def evolution(cells_alive, game_setting):
    new_cells_alive = []
    for cell in cells_alive:
        for new_cell in get_next_generation(cell, cells_alive, new_cells_alive, game_setting):
            new_cells_alive.append(new_cell)
    return new_cells_alive

def show_map(cells_alive, gen, size_map):
    os.system('clear')
    for index_y in range(size_map):
        for index_x in range(size_map):
            if (index_x > 0  and index_x < size_map - 1
            and index_y > 0 and index_y < size_map - 1):
                if([index_x, index_y] in cells_alive):
                    state = '\033[92m□'
                else:
                    state = '\033[91mx'
                print(state + "\033[0m ", end = '')
        print("")

#endregion

#region Niveau 2

def get_next_generation(cell, cells_alive, new_cells_alive, game_setting):
    cells_new_gen = []
    for cell_new_gen in  get_around_cells(cell, game_setting["size_map"]):
        if False == (cell_new_gen in new_cells_alive):
            # Vérifier nombre de voisins en vie
            neighbor = get_neighbor(cell_new_gen, cells_alive, game_setting["size_map"])
            # Vérifier règles
            alive = can_alive(neighbor, game_setting["rules"], (cell_new_gen in cells_alive))
            if alive:
                cells_new_gen.append(cell_new_gen)
    return cells_new_gen
#endregion

#region Niveau 3

def get_around_cells(cell, size_map):
    tmp_x = cell[0]
    tmp_y = cell[1]
    positions_x = [ tmp_x-1, tmp_x, tmp_x+1]
    positions_y = [ tmp_y-1, tmp_y, tmp_y+1]
    cells_around = []
    for x in positions_x:
        for y in positions_y:
            if(x >= 0 and x < size_map and y >= 0 and y < size_map):
                cells_around.append([x, y])
    return cells_around

def get_neighbor(cell, cells_alive, size_map):
    neighbor = 0
    for tmp_cell in get_around_cells(cell, size_map):
        if (cell != tmp_cell and True == (tmp_cell in cells_alive)):
            neighbor+=1
    return neighbor

def can_alive(neighbor, rules, alive):
    numbers = rules['alive'] if alive else rules['birth']
    index = 0
    alive = False
    while(False == alive and index < len(numbers)):
        if numbers[index] == neighbor:
            alive = True
        index+=1
    return alive

#endregion

#region Main

def get_input():
    stop = None
    try:
        input(f'Generation : {game_setting["generation"]} | Press Enter to continue or crtl+c to quit...')
        stop = False
    except KeyboardInterrupt:
        stop = True
    return stop

if __name__ == "__main__":
    game_setting = {
        "size_map" : 10,
        "rules" : {
            "alive": [2, 3],
            "birth": [3]
        },
        "generation" : 1
    }
    game_setting["size_map"]+=2
    cells_alive = initialization(game_setting["size_map"])
    show_map(cells_alive, game_setting["generation"], game_setting["size_map"])
    stop = get_input()
    while False == stop:
        cells_alive = evolution(cells_alive, game_setting)
        game_setting["generation"]+=1
        show_map(cells_alive, game_setting["generation"], game_setting["size_map"])
        stop = get_input()
#endregion
