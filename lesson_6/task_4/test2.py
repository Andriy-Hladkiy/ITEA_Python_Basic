def count_squares(user_list):
    list_of_squares = []
    for n in user_list:
        n = n**2
        list_of_squares.append(n)
    return sum(list_of_squares)
