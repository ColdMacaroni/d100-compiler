##
# compile.py
# A program to compile d100 tables into small C programs
# 2021-12-31

# To get arguments
import sys

# TODO: Convert to C program
# TODO: Do this by going through directory and sub directories.
# TODO: BIGBOI: Implement tests.

# Steps
#   Read .tab file
#   Get name
#   Get amount of dice. Convert to tuple of ints
#   Create a list full of None * die faces.
#   Read through the table, using the left side of the TAB as index
#   Do this till the end
#   XXX: Temporary. Just print it out to the terminal to make sure it's fine

def main(files: list[str]):
    """
    Goes through the files passed as arguments and parses each tab file.
    Then it creates a corresponding C program and compiles it.
    """
    ...

if __name__ == "__main__":
    assert len(sys.argv) > 1, "Needs at least one file or directory as argument."

    # Skip first one bc that is python file.
    main(sys.argv[1:])
