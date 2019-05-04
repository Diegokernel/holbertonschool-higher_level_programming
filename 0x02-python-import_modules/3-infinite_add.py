#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_num = len(sys.argv)
    sum = 0
    for count in range(1, args_num):
        sum += int(sys.argv[count])
    print("{:d}".format(sum))
