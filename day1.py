import sys

def main():
    s = 0
    fuels = []

    for f in sys.stdin:
        s += (int(f) // 3) - 2

    print(s)

if __name__ == "__main__":
    main()
