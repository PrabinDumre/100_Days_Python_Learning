if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    # Creating a tuple from the input integers
    tuple_of_integers = tuple(integer_list)

    # Printing the result of the hash function
    print(hash(tuple_of_integers))
