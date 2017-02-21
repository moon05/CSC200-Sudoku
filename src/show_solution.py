import board
import sys

def get_results(file):
    values = []
    for line in file.readlines():
        if line == "UNSAT":
            return 0
        elif line != "SAT\n":
            att = line.split(" ")
            for each_val in att[:-1]:
                if "-" not in each_val:
                    values.append(int(each_val))
    return values

def main(argv):
    file = open(argv[0], 'r')
    v = get_results(file)
    b = board.extract(v)
    for each_row in b:
        print(each_row)
if __name__ == "__main__":
    main(sys.argv[1:])