from collections import deque


def fill_the_box(h, d, w, *args):
    volume = h * d * w
    available_space = volume
    residue_elements = 0
    elements = deque(args)
    box_is_full = False
    no_more_elements = False

    while True:
        if elements[0] == 'Finish':
            break
        el = elements.popleft()
        if available_space >= el:
            available_space -= el

        elif available_space < el:
            box_is_full = True
            residue_elements = el - available_space
            available_space = 0
            
            while True:
                if elements[0] == 'Finish':
                    no_more_elements = True
                    break
                el = elements.popleft()
                residue_elements += el
        if no_more_elements:
            break

    if box_is_full:
        result = f"No more free space! You have {residue_elements} more cubes."
    else:
        result = f"There is free space in the box. You could put {available_space} more cubes."

    return result


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
