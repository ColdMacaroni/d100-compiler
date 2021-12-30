# d100 compiler
This python script will take d100 tables and compile them into their own individual program

## The .tab format
I completely made this up

Empty lines and any lines starting with `#` will be ignored.

The first line will define the name of the table (echoed out when the program is started).

```
Epic Table
```

The next line will define which dice are required. In the format `d#` and separated by a space.

```
Epic Table
d3 d3
```

Now you need to create a table for each dice roll. Start the table with `---` on an empty line, followed by the dice result and corresponding text separated by a TAB character. You can copy one from here -> `	`

```
Epic Table
d3 d3
# First table
---
1	Good
2	Evil

# I wanted to be original
3	Irritating

# Second table
---
1	Party hat
2	Snail
3	Stick
```


