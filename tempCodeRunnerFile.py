numbers = [7, 3, 2, 9, 8]

def insertion(list):
    base_index = 0
    current_index = 1
    reversed_current_index = 1
    n = len(list)
    
    while n > current_index:
        if list[current_index - 1] > list [current_index]:
            while reversed_current_index > base_index and list[reversed_current_index - 1] > list [reversed_current_index]:
                list[reversed_current_index - 1], list[reversed_current_index] = list[reversed_current_index], list[reversed_current_index - 1]
                reversed_current_index -= 1
            current_index += 1
            reversed_current_index = current_index
        else:
            current_index += 1
            reversed_current_index = current_index
    
    print(list)

insertion(numbers)