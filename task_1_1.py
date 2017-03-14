def like(numbers, a_set, b_set):

    likes = 0

    for el in numbers.split(" "):
        if el in a_set.split(" "):
            likes += 1
        if el in b_set.split(" "):
            likes -= 1

    return likes


if __name__ == "__main__":
    
    numbers = "3 2 10 7 5 5 2 1 2"
    a = "2 3 7"
    b = "5 10 7"

    print(like(numbers, a, b))

    numbers = "1 4 10 20 1 11 12"
    a = "1 4 1 12"
    b = "1 12 10 20"

    print(like(numbers, a, b))

    numbers = "1 2 3 4 5 6"
    a = "1 2 3"
    b = "4 5 6"

    print(like(numbers, a, b))