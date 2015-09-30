import re
import sys
while True:
  txt = raw_input("||Text:   ")
  shift = int(input("||Steps:  "))
  length = len(txt)
  counter = 0

  while counter != length:
    char = int(ord(txt[counter]))
    if re.search(r'[a-z]', txt[counter]):
        newchar = char + shift
        while newchar >= 123:
            change = newchar - 122
            newchar = 96 + change
    elif re.search(r'[A-Z]', txt[counter]):
        newchar = char + shift
        while newchar >= 91:
            change = newchar - 90
            newchar = 64 + change
    else:
        newchar = char
    sys.stdout.write(chr(newchar))
    counter = counter + 1
  sys.stdout.write("\n")
  break

#by defining the ascii values 