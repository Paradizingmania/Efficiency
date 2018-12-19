import Efficiency
while True:
    print()
    # efficiency = Efficiency.Efficiency()
    # create csv file for results
    i = 1
    while True:

        try:
            f = open("results_" + str(i) + ".csv", "x")  # check if result document exists
            break
        except (FileNotFoundError, FileExistsError):
            i += 1

    break
