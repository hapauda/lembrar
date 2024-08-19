if __name__ == '__main__':
    list = []
    n = int(input())
    for _ in range(n):
        command, *args = input().split
        if command == "print":
            print(list)
        else:
            getattr(list, command)(*map(int, args))