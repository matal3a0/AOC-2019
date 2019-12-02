import sys

def calc(t,f):
    s = (f // 3) -2
    if s <= 0:
        return t
    else:
        t += s
        return calc(t,s)

def main():
    sum = 0

    for f in sys.stdin:
        sum += calc(0,int(f))

    print(sum)

if __name__ == "__main__":
    main()
