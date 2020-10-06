import random, os

#region Level 1
def initialization(size_map):
    cell_alive = []
    for index_x in range(size_map):
        for index_y in range(size_map):
            cursor = random.randrange(0, 100)
            if ( cursor >=  random.randrange(0, 100)):
                cell_alive.append([index_x, index_y])
    return cell_alive

def evolution(cell_alive, game_setting):
    new_cell_alive = []
    for cell in cell_alive:
        for new_cell in get_next_generation(cell, cell_alive, new_cell_alive, game_setting):
            new_cell_alive.append(new_cell)
    game_setting["generation"]+=1
    show_map(cell_alive, game_setting["generation"], game_setting["size_map"])
    evolution(new_cell_alive, game_setting)

def show_map(cell_alive, gen, size_map):
    os.system('clear')
    for index_x in range(size_map):
        for index_y in range(size_map):
            state = '\033[92m□' if [index_x, index_y] in cell_alive else '\033[91mx'
            print(state + "\033[0m ", end = '')
        print("")
    try:
        input(f'Generation : {gen} | Press Enter to continue or crtl+c to quit...')
    except KeyboardInterrupt:
        exit()

#endregion

#region Niveau 2

def get_next_generation(cell, cell_alive, new_cell_alive, game_setting):
    tmp_cells = []
    for tmp_cell in  get_around_cell(cell, game_setting["size_map"]):
        if (False == (tmp_cell in new_cell_alive)):
            # Vérifier nombre de voisins en vie
            neighbor = get_neighbor(tmp_cell, cell_alive, game_setting)
            # Vérifier règles
            alive = can_alive(neighbor, game_setting["rules"], (tmp_cell in cell_alive))
            if (alive):
                tmp_cells.append(tmp_cell)
    return tmp_cells
#endregion

#region Niveau 3

def get_around_cell(cell, size_map):
    x = cell[0]
    y = cell[1]
    position_x = [ x-1, x, x+1]
    position_y = [ y-1, y, y+1]
    tmp_cells = []
    for x in position_x:
        for y in position_y:
            if(x >= 0 and x < size_map and y >= 0 and y < size_map):
                tmp_cells.append([x, y])
    return tmp_cells
        

def get_neighbor(cell, cell_alive, game_setting):
    neighbor = 0
    for tmp_cell in get_around_cell(cell, game_setting["size_map"]):
        if (cell != tmp_cell and True == (tmp_cell in cell_alive)):
            neighbor+=1
    return neighbor

def can_alive(neighbor, rules, alive):
    numbers = rules['alive'] if alive else rules['birth']
    index = 0
    alive = False
    while(False == alive and index < len(numbers)):
        if(numbers[index] == neighbor):
            alive = True
        index+=1
    return alive

#endregion

#region Main

if __name__ == "__main__":
    game_setting = {
        "size_map" : 40,
        "rules" : {
            "alive": [2, 3],
            "birth": [3]
        },
        "generation" : 1
    }
    cell_alive = initialization(game_setting["size_map"])
    show_map(cell_alive, game_setting["generation"], game_setting["size_map"])
    evolution(cell_alive, game_setting)

#endregion
