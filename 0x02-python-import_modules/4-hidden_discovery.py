#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    res = dir(hidden_4)
    for name in res:
        if name[:2] != '__':
            print("{}".format(name))
