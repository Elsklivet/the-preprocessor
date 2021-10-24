from os import replace
import sys

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
        if line.startswith("#"):
            # Directive
            directive = line[1:line.find(" ")]
            line = line[line.find(" ")+1:]
            if directive == "define":
                # Define directive
                subtext = line[:line.find(" ")]
                line = line[line.find(" ")+1:]
                replacetext = line
                code = code.replace(subtext, replacetext)
                # print(f"Replacing '{subtext}' with '{replacetext}'")
                # print(code)


    new_lines = []
    for line in code.splitlines():
        if line.startswith("#"):
            continue
        else:
            new_lines.append(line+"\n")
    with open(path, 'w') as outfile:
        outfile.writelines(new_lines)

__main__()