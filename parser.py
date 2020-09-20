import sys
import os
os.system("cls || clear")

def get_filename():
    if len(sys.argv) >= 3:
        input1 = int(sys.argv[1])
        input2 = int(sys.argv[2])
        return input1 + input2
    else:
        print("You should run this program by calling: python parser.py filename")
        return ""


def main():
    filename = get_filename()
    if filename == "":
        return
    
    print(f"File to add: {filename}")

if __name__ == "__main__":
    main()