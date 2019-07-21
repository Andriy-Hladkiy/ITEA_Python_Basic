if __name__ == '__main__':

    count_function = '''
def count_squares(user_list):
    list_of_squares = []
    for n in user_list:
        n = n**2
        list_of_squares.append(n)
    return sum(list_of_squares)
'''
    with open("test2.py", 'w') as count_file:
        print(count_function, file=count_file)
