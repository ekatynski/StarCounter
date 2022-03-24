def pairCheck(row, max):
    count = 0
    sum = 0
    pair = [0,0]

    while sum < max:
        if count % 2 == 0:
            sum += row 
            pair[0] += 1
        else:
            sum += row - 1
            pair[1] += 1
        count += 1

    if sum == max:
        return [True, pair]
    else:
        return [False, 0]


if __name__ == "__main__":
    while True:
        number = input("Enter target star value: ")
        try:
            val = int(number)
            if val < 0:  # if not a positive int print message and ask for input again
                 print("Sorry, input must be a positive integer, try again")
                 continue
            break
        except ValueError:
             print("That's not an int!")     
    # else all is good, val is >=  0 and an integer
    print(val)

    solutions = []

    for i in range(2, round(val/2)):
        current = pairCheck(i, val)
        if current[0] == True:
            solutions.append([i, current[1]])

    print("Your flag could have the following " + str(len(solutions)) + " options:")
    for solution in solutions:
        print(solution)

