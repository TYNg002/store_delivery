# returns the maximum value of an element a nested list
def nested_list_max(nested_list, maximum=0):
    # assess each element of the variable 'nested_list'
    for ele in nested_list:
        # if the element is a list
        if isinstance(ele, list):
            # set the variable named 'maximum' to run this function 'nested_list_max'
            # again from the start, with the element being used as the new 
            # 'nested_list' variable
            maximum = nested_list_max(ele, maximum)
        # if the element is not a list, set 'maximum' to the element or current 
        # 'maximum', whichever is greater
        else:
            maximum = max(ele, maximum)
    return maximum

# ask for first input line until input is acceptable
while True:
    try:
        blocks_stores = input(
            "Enter dimension of city in blocks and number of stores e.g. 3 2: \n"
        ).split(" ")
        # separate input into different variables as integer types
        blocks = int(blocks_stores[0])
        store_total = int(blocks_stores[1])
    # ensure sufficient number of inputs are given, and that they are integers
    except (IndexError, ValueError):
        print(
            "Please enter two integers separated by a space."
        )
        continue
    # ensure the number of blocks in one axis and stores are between 1 and 10,000
    if not ((blocks and store_total) in range(1, 10001)):
        print(
            "The integer must be between 1 and 10,000 inclusive."
        )
        continue
    break

# create a 2D grid filled with '0' based on given block size
city = [[0] * blocks for r in range(blocks)]

# repeat block for number of stores
for store_count in range(store_total):

    # ask for input about each store until input is acceptable, one store at a time
    while True:
        try:
            store_info = input(
                "Enter x coordinate, y coordinate, and radius of store {} e.g. 1 3 2: \
                    \n".format(store_count + 1)
            ).split(" ")
            # separate input into different variables as integer types
            store_x_coord = int(store_info[0])
            store_y_coord = int(store_info[1])
            store_radius = int(store_info[2])
            # multiply y coordinate by -1 to reference correct row via index
            row = store_y_coord * -1
            # subtract x coordinate by 1 to reference correct column via index
            column = store_x_coord - 1

        # ensure sufficient number of inputs are given, and that they are integers
        except (IndexError, ValueError):
            print(
                f"Please ensure you have entered three integers separated by a space."
            )
            continue

        # print error message and restart loop if coordinates are not within city blocks
        if not ((store_x_coord and store_y_coord) in range(1, blocks + 1)):
            print(
                f"Please ensure your coordinates are between 1 and {blocks} inclusive."
            )
            continue
        break

    # list to reverse / mirror coordinate modifiers
    pos_neg = [1, -1]
    # y_mod and x_mod used to modify indices
    for y_mod in range(store_radius + 1):
        for x_mod in range(store_radius + 1):
            # reverses polarity of row index modifier
            for flip1 in pos_neg:
                new_row_index = row + (y_mod * flip1)
                # reverses polarity of column index modifier
                for flip2 in pos_neg:
                    new_column_index = column + (x_mod * flip2)

                    # start next iteration if new index number is out of bounds
                    if not (
                        new_column_index in range(blocks)
                        and new_row_index in range(-blocks, 0)
                    ):
                        continue

                    # for store location, only increase count once
                    elif y_mod == x_mod == 0:
                        if flip1 == flip2 == 1:
                            city[new_row_index][new_column_index] += 1

                    # for locations directly above / below or to the right / left
                    # of the store
                    elif y_mod == 0 or x_mod == 0:
                        # only increase count in two completely mirrored instances
                        if flip1 == flip2:
                            city[new_row_index][new_column_index] += 1

                    # for all other locations within store radius
                    elif (y_mod + x_mod - 1) < store_radius:
                        city[new_row_index][new_column_index] += 1

see_grid = input("See the full city grid? (Y/N)\n").lower()
if see_grid == "y":
    print("City grid:")
    for row in city:
        print(row)

print("The greatest number of stores a location in the city can be served by is "
      f"{nested_list_max(city)}.")