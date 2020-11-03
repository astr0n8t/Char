#!/usr/bin/env python
"""
char.py
Nathan Higley <nathan@nathanhigley.com>
Nov 2, 2020

Small python program to convert ascii codes to chars and vice versa.
"""

import argparse

"""
Converts the codes to a long string.
Takes the codes array as input.

Outputs a string.
"""
def convert(codes):

    final_string = ""

    for c in codes:
        final_string += chr(c)

    return final_string

"""
Formats the codes based on whether the input is decimal, hex, or binary.
Codes will be in decimal (int) format afterwards.
Takes as input decimal, hex, or binary bools, evaluated in that order of precedence.
Also the separator and codes raw input from the argument.

Returns the properly formatted code array
"""
def format_codes(d, h, b, s, codes):

    code_array = []

    if s:
        code_temp = ""
        for x in range(len(codes)):
            code_temp += codes[x] 
        codes = code_temp.split(s)
        

    base_to_convert = 10

    if d:
        base_to_convert = 10
    elif h:
        base_to_convert = 16
    elif b:
        base_to_convert = 2

    for i in codes:
        if int(i, base=base_to_convert) > 127 or int(i, base=base_to_convert) < 0:
            raise Exception('given value ' + i + ' outside of bounds of ascii table using given options.')
        code_array.append(int(i, base=base_to_convert))

    return code_array

"""
Takes as input the add, the subtract,
and the codes array (a list of ints).

Returns the codes rotated as indicated by the inputs.
"""
def rotate(add, subtract, codes):
    # Check if we need to add
    if add:
        for x in range(len(codes)):
            codes[x] += add
            # Check if we've gone out of the ascii table
            if codes[x] > 127:
                codes[x] -= 127
    # If not adding check if we need to subtract
    elif subtract:
         for x in range(len(codes)):
            codes[x] -= subtract
            # Check if we've gone out of the ascii table
            if codes[x] < 0:
                codes[x] += 127   

    return codes


"""
Adds arguments and description and then parses them.
Returns the arguments with the codes as an array of strings.
"""
def process_args():

    desc = "Converts ascii codes to chars and vice versa"

    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument("-d", "--decimal", help = "Input as decimal ascii codes -- default", action="store_true")
    parser.add_argument("-x", "--hex", help = "Input as hexadecimal ascii codes", action="store_true")
    parser.add_argument("-b", "--binary", help = "Input as binary ascii codes", action="store_true")
    parser.add_argument("-a", "--adds", help = "Adds value to all the codes before processing", type=int)
    parser.add_argument("-s", "--subtracts", help = "Subtracts value to all the codes before processing", type=int)
    parser.add_argument("-e", "--separator", help = "Separator to use, default is a space.")
    parser.add_argument("-n", "--newline", help = "Use a newline as a separator.", action="store_true")
    parser.add_argument("codes", nargs='*')

    options = parser.parse_args()
    if not options.codes: 
        parser.print_help()
        parser.exit(2)
    
    if options.newline:
        options.separator = '\n'

    return options



if __name__ == "__main__":

    args = process_args()
    codes = format_codes(args.decimal, args.hex, args.binary, args.separator, args.codes)
    codes = rotate(args.adds, args.subtracts, codes)
    output = convert(codes)

    print(output)
