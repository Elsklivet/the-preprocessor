#define TEST = print
from os import replace
import sys

def find(string: str, substr: str) -> int:
    counter = 0
    current = 0
    main_index = 0
    for char in string:
        if char == substr[counter]:
            current = main_index
            counter += 1
        elif char in [" ", "\n", "\r", "\t"]:
            continue
        elif counter != 0:
            counter = 0
            current = -1

        main_index += 1

    return current

def __main__():
    path = None
    try:
        path = sys.argv[1]
    except IndexError:
        print("Usage: python3 preproc.py SomeFile.pre.java")
        exit(1)
    # print(sys.argv)
    print(f"Opening {path}")
    infile = open(path, 'r')
    code = infile.read()
    infile.close()
    code_lines = code.splitlines()
    for line in code_lines:
        line = line.lstrip()
        if line.startswith("#"):
            # Directive
            directive = line[1:line.find(" ")]
            line = line[line.find(" ")+1:] # Line now starts after directive
            if directive == "define":
                # Define directive
                code = code[code.find("#define ")+1:] # Code deletes #define
                subtext = line[:line.find("=")]
                subtext = subtext.strip()
                code = code[code.find("=")+1:]
                code = code.lstrip()
                replacetext = code[:code.find("#endef")].rstrip()
                code = code[code.find("#endef")+6:]
                code = code.replace(subtext, replacetext)
                # print(f"Replacing '{subtext}' with '{replacetext}'")
                # print(code)
            if directive == "include":
                filename = line[line.find("<")+1:line.find(">")]
                print(filename)
                insertion = ""
                with open(filename, 'r') as include:
                    insertion = include.read()
                code = code.replace(f"#include <{filename}>", insertion, 1)
                


    new_lines = []
    code.lstrip()
    for line in code.splitlines():
        new_lines.append(line+"\n")
    with open(path.replace("~",""), 'w') as outfile:
        outfile.writelines(new_lines)

__main__()