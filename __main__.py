from cipher import cipher
import unicodedata
import sys


def main():
    print("=== Values are read from file/input.txt file ===")
    with open("files/input.txt", "r") as instr:
        c = 0
        for l in instr.readlines():
            print("Line(" + str(c) + ") " + l)
            c = c + 1
    while True:
        inp = input("Read line: ")
        if(inp != "exit"):
            try:
                option = int(inp)
                cipher(option) # Control what line to run from input.txt
            except Exception:
                print("Input a valid integer")
        else:
            print("===== End of code =====")
            break
        

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()