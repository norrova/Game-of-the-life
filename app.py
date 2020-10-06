import random, os

def evolution(cell_alive, game_setting):
    new_cell_alive = []
    for cell in cell_alive:
        for new_cell in get_next_generation(cell, cell_alive, new_cell_alive, game_setting):
            new_cell_alive.append(new_cell)
    game_setting["generation"]+=1
    show_map(cell_alive, game_setting["generation"], game_setting["size_map"])
    evolution(new_cell_alive, game_setting)

def get_next_generation(cell, cell_alive, new_cell_alive, game_setting):
    tmp_list = []
    for tmp_cell in  get_around_cell(cell, game_setting["size_map"]):
        if (False == (tmp_cell in new_cell_alive)):
            # Vérifier nombre de voisins en vie
            neighbor = get_neighbor(tmp_cell, cell_alive, game_setting)
            # Vérifier règles
            alive = can_alive(neighbor, game_setting["rules"], (tmp_cell in cell_alive))
            if (alive):
                tmp_list.append(tmp_cell)
    return tmp_list

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
    while(alive == False and index < len(numbers)):
        if(numbers[index] == neighbor):
            alive = True
        index+=1
    return alive

def get_around_cell(cell, max):
    x = cell[0]
    y = cell[1]
    position_x = [ x-1, x, x+1]
    position_y = [ y-1, y, y+1]
    tmp_cell = []
    for x in position_x:
        for y in position_y:
            if(x >= 0 and x < max and y >= 0 and y < max):
                tmp_cell.append([x, y])
    return tmp_cell

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

def init(size_map):
    cell_alive = []
    for index_x in range(size_map):
        for index_y in range(size_map):
            cursor = random.randrange(0, 100)
            if ( cursor >=  random.randrange(0, 100)):
                cell_alive.append([index_x, index_y])
    return cell_alive
        

if __name__ == "__main__":
    game_setting = {
        "size_map" : 40,
        "rules" : {
            "alive": [2, 3],
            "birth": [3]
        },
        "generation" : 0
    }
    # Ligne : cell_alive = [[1, 2], [1,3], [1,4]]
    # Planeur : cell_alive = [[3, 2], [3,3], [3,4], [2,4], [1,3]]
    cell_alive = init(game_setting["size_map"])
    show_map(cell_alive, game_setting["generation"], game_setting["size_map"])
    evolution(cell_alive, game_setting)