# created by Elias Axel Kærhøg
import csv
import Efficiency
while True:

    print("To calculate effect of tamper on yield press 1 to calculate effect of core mass on yield press 2")
    selection = input()
    if selection == "1":

        print("select lower bound in grams")
        lower_bound = input()

        try:
            lower_bound = int(lower_bound)
        except ValueError:
            print("not an int")
            break

        print("select upper bound in grams")
        upper_bound = input()

        try:
            upper_bound = int(upper_bound)
        except ValueError:
            print("not an int")
            pass

        print("select interval in grams(standard is 1000)")
        interval = input()

        try:
            interval = int(interval)
        except ValueError:
            print("not an int")
            pass

        print("select mass of core in grams, for default use 0")
        core = input()

        try:
            core = int(core)
        except ValueError:
            print("not an int")
            pass

        i = 1
        while True:

            try:
                f = open("results_varied_tamper" + str(i) + ".csv", "x")  # check if result document exists
                break
            except (FileNotFoundError, FileExistsError):
                i += 1
            break

        j = 1
        tamper = 0

        while tamper <= upper_bound:
            tamper = lower_bound + j * interval

            print (str(Efficiency.efficiency(core, tamper)))

            row = [core, tamper, str(Efficiency.efficiency(core,tamper))]

            with open("results_varied_tamper"+str(i)+".csv", "a") as file:
                writer = csv.writer(file)
                writer.writerow(row)

            j += 1

        file.close()
        break

    if selection == "2":

        print("select lower bound in grams")
        lower_bound = input()

        try:
            lower_bound = int(lower_bound)
        except ValueError:
            print("not an int")
            break

        print("select upper bound in grams")
        upper_bound = input()

        try:
            upper_bound = int(upper_bound)
        except ValueError:
            print("not an int")
            pass

        print("select interval in grams(standard is 1000)")
        interval = input()

        try:
            interval = int(interval)
        except ValueError:
            print("not an int")
            pass

        print("select mass of tamper in grams, for default use 0")
        tamper = input()

        try:
            tamper = int(tamper)
        except ValueError:
            print("not an int")
            pass

        i = 1
        while True:

            try:
                f = open("results_varied_core" + str(i) + ".csv", "x")  # check if result document exists
                break
            except (FileNotFoundError, FileExistsError):
                i += 1
            break

        j = 1
        core = 0

        while core <= upper_bound:
            core = lower_bound + j * interval

            print (str(Efficiency.efficiency(core, tamper)))

            row = [core, tamper, str(Efficiency.efficiency(core,tamper))]

            with open("results_varied_core"+str(i)+".csv", "a") as file:
                writer = csv.writer(file)
                writer.writerow(row)

            j += 1

        file.close()
        break
