import sys

def get_data():
    f = open("day2.txt","r")
    data = list(map(int,f.read().split(',')))

    return data

def main():
    data = get_data()

    for n in range(0, 100):
        for b in range(0, 100):
            t_data = data.copy()
            t_data[1] = n
            t_data[2] = b

            i = 0

            while t_data[i] != 99:
                if t_data[i] == 1:
                    t_data[t_data[i+3]] = t_data[t_data[i+1]] + t_data[t_data[i+2]]
                elif t_data[i] == 2:
                    t_data[t_data[i + 3]] = t_data[t_data[i + 1]] * t_data[t_data[i + 2]]

                i += 4

            if t_data[0] == 19690720:
                print(100 * n + b)
                return


if __name__ == "__main__":
    main()
