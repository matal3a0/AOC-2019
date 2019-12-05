import sys, operator

def get_data():
    f = open("day2.txt","r")
    data = list(map(int,f.read().split(',')))

    return data

def main():
    data = get_data()
    ops = {
        1: operator.add,
        2: operator.mul
    }

    ip = 0

    while data[ip] != 99:
        op = ops[data[ip]]
        data[data[ip+3]] = op(data[data[ip+1]],data[data[ip+2]])

        ip += 4

    print(data[0])


if __name__ == "__main__":
    main()
