# Char
Small python program which converts ascii codes to chars and vice versa.  Can also do some neat things.
Not heavily tested so it might break...  You've been warned.

```
➜  ./char.py 72 101 108 108 111 32 87 111 114 108 100 33           
Hello World!
➜  echo 72 101 108 108 111 32 87 111 114 108 100 33 | ./char.py  
Hello World!
```

```
usage: char [-h] [-d] [-x] [-b] [-a ADDS] [-s SUBTRACTS] [-e SEPARATOR] [-n] ...

Converts ascii codes to chars and vice versa

positional arguments:
  codes

optional arguments:
  -h, --help            show this help message and exit
  -d, --decimal         Input as decimal ascii codes -- default
  -x, --hex             Input as hexadecimal ascii codes
  -b, --binary          Input as binary ascii codes
  -a ADDS, --adds ADDS  Adds value to all the codes before processing
  -s SUBTRACTS, --subtracts SUBTRACTS
                        Subtracts value to all the codes before processing
  -e SEPARATOR, --separator SEPARATOR
                        Separator to use, default is a space.
  -n, --newline         Use a newline as a separator.
```
