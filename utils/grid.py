

# def get_neighbours(x: int, y: int, width: int, height: int) -> list[tuple[int, int]]:
#     neighbours = []
#     for xx in [x-1, x, x+1]:
#         for yy in [y-1, y, y+1]:
#             if xx == x and yy == y:
#                 continue
#             if xx < 0 or xx >= width:
#                 continue
#             if yy < 0 or yy >= height:
#                 continue
#             neighbours.append((xx, yy))

#     return neighbours

def get_neighbours(x: int, y: int, distance: int, width: int, height: int) -> list[tuple[int, int]]:
    neighbours = []
    for xx in range(x - distance, x + distance + 1):
        for yy in range(y - distance, y + distance + 1):
            if xx == x and yy == y:
                continue
            if xx < 0 or xx >= width:
                continue
            if yy < 0 or yy >= height:
                continue
            neighbours.append((xx, yy))

    return neighbours
