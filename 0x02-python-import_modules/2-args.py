#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_num = len(sys.argv)
    if args_num == 1:
        print("0 arguments.")
    elif args_num == 2:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(args_num - 1))
    for count in range(1, args_num):
        print("{:d}: {}".format(count, sys.argv[count]))
