##
# compile.py
# A program to compile d100 tables into small C programs
# 2021-12-31

import sys

#---------#
# GLOBALS #
#---------#
# For commenting out lines in .tab
COMMENT_CHAR = '#'

# For values which are not defined in the table
DEFAULT_VALUE = 'something'

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

class DiceTable:
    name: str
    dice: tuple[int]
    tables: tuple[dict[int, str]]

    def __init__(self,
            name: str = None,
            dice: tuple[int] = None,
            tables: tuple[dict[int, str]] = None
    ):
        self.name = name
        self.dice = dice
        self.tables = tables


def parse_tab(text: list[str]) -> DiceTable:
    """
    Parses the contents of a .tab file into a DiceTable object.
    Does NOT read the file, takes the contents as a list of strings.
    Runs each line through .strip()
    """
    # We need to get 3 things:
    #   Table name, Dice needed, The tables for each die.
    table = DiceTable()

    # where all the data will be stored
    tables = list()
    for line in text:
        # Get rid of extra spaces and new lines for easier handling.
        line = line.strip()

        # Skip commented out lines and empty lines.
        #
        # Empty line check first so that lazy evaluation saves us from
        # IndexError on the second condition.
        if not line or line[0] == COMMENT_CHAR:
            continue

        # These two are the first two lines
        if table.name is None:
            table.name = line

        elif table.dice is None:
            # Convert to a tuple of ints, must remove d from d#
            table.dice = tuple(
                map(
                    int,
                    line.replace('d', '').split()
                )
            )

        # Table data
        else:
            # This means create a new table filled with defaults
            if line == "---":
                tables.append(
                    {
                        i + 1: DEFAULT_VALUE

                        # By using the len we can select the appropriate die
                        # for this table
                        for i in range(table.dice[len(tables)])
                    }
                )
            else:
                # split only once in case the user wants a tab in their thing
                num, text = line.split("\t", 1)

                # Update the entry.
                tables[-1][int(num)] = text

    table.tables = tuple(tables)

    # print(table.name, table.dice, table.tables)

    return table


def dicetable_to_c(dicetable: DiceTable) -> str:
    """
    Converts a dicetable object to a c program that has that functionality
    """
    base = \
"""
"""


def main(files: list[str]):
    """
    Goes through the files passed as arguments and parses each tab file.
    Then it creates a corresponding C program and compiles it.
    """
    tables = list()

    # Parse tables
    for fn in files:
        with open(fn, "r") as file:
            # Preemptively remove any spaces and new lines to make everything
            # easier later on
            text = file.readlines()

        tables.append(parse_tab(text))

    # Turn them into C code
    for table in tables:
        

    return tables



if __name__ == "__main__":
    assert len(sys.argv) > 1, "Needs at least one file or directory as argument."

    # Skip first one bc that is python file.
    main(sys.argv[1:])
