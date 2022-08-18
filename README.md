# Kali_process_enum
Enumerates various elements in Linux for easy review. 

To run: 

```$ python3 kali_enum.py```

Usage: You'll be greeted by a prompt to make your selection: $ Enter 1 to see processes $ Enter 2 to see process threads $ Enter 3 to see process modules $ Enter 4 to see process executables $ Enter 5 to see process memory (requires hightened privileges $ Enter a number:

Invalid selections will exit the program. Once you make your selection, for options 2 - 5 enter the pid of the process you want to see information about.

Note: Selection 5 to read memory requires administrator privileges. You'll need to run the program as sudo or root. It also takes a while to dump this hex to the screen.
