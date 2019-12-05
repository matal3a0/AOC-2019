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

    for n in range(0, 100):
        for b in range(0, 100):
            t_data = data.copy()
            t_data[1] = n
            t_data[2] = b

            ip = 0

            while t_data[ip] != 99:
                op = ops[t_data[ip]]
                t_data[t_data[ip + 3]] = op(t_data[t_data[ip + 1]], t_data[t_data[ip + 2]])

                ip += 4

            if t_data[0] == 19690720:
                print(100 * n + b)
                return


if __name__ == "__main__":
    main()
