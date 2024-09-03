def split_and_join(line):
    a = line
    a = a.split(" ")
    a = "-".join(a)
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)