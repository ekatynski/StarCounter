def pair_check(row, target):
    count = 0
    total = 0
    pair = [0, 0]

    while total < target:
        if count % 2 == 0:
            total += row
            pair[0] += 1
        else:
            total += row - 1
            pair[1] += 1
        count += 1

    if total == target:
        return [True, pair]
    else:
        return [False, 0]


if __name__ == "__main__":
    # Get a positive non-zero integer to use for a star count - gotta have at least one
    while True:
        number = input("Enter target star value: ")
        try:
            val = int(number)
            if val <= 0:
                print("Sorry, input must be a positive non-zero integer, try again")
                continue
            break
        except ValueError:
            print("That's not an int!")

    solutions = []

    # Run through every viable combination of rows up to half of the number of stars on the flag
    for i in range(2, round(val / 2)):
        current = pair_check(i, val)
        # Add winning solutions to the list
        if current[0]:
            solutions.append([i, current[1]])

    # Print out the winning solutions
    print("Your flag could have the following " + str(len(solutions)) + " options:")
    for solution in solutions:
        print(solution)
