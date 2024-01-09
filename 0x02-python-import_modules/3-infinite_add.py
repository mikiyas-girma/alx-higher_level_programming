#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    cmdsum = 0
    for cmd in sys.argv[1:]:
        cmdsum += int(cmd)
    print(cmdsum)
