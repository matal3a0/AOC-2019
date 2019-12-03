import sys

def get_data():
    f = open("day2.txt","r")
    data = list(map(int,f.read().split(',')))

    return data

def main():
    data = get_data()

    i = 0

    while data[i] != 99:
        if data[i] == 1:
            data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
        elif data[i] == 2:
            data[data[i+3]] = data[data[i+1]] * data[data[i+2]]

        i += 4

    print(data[0])


if __name__ == "__main__":
    main()
