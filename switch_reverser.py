
def switch_reverser(my_list):
    if all(isinstance(item, int) for item in my_list):
        my_list.reverse()
        return my_list
    elif all(isinstance(item, str) for item in my_list):
        return [item.upper() for item in my_list]
    else:
        return my_list