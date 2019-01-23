def print_snake(sequence: str, width: int):
    num_of_segments = len(sequence) // (width+1)
    start_from_left = num_of_segments % 2 == 1
    extra_letters = len(sequence) % (width+1)

    if extra_letters != 0:
        output = ''
        if not start_from_left:
            output = ' ' * (width - extra_letters)

        for i in range(0, extra_letters):
            output = output + sequence[i]
        print(output)

    for i in range(0, num_of_segments):
        start_range = i * (width + 1) + extra_letters
        if not start_from_left:
            output = ' ' * (width - 1)
            output = output + sequence[start_range]
            print(output)
            output = ''
            start_range = start_range + 1
            output = output + sequence[start_range:start_range+width][::-1]
            print(output)
        else:
            output = sequence[start_range]
            start_range = start_range + 1
            print(output)
            output = ''
            output = output + (sequence[start_range:start_range+width])
            print(output)
        start_from_left = not start_from_left


print_snake('wtlovessnakes', 3)
