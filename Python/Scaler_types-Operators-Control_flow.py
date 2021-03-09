Scalar Types:
    - int (arbitrary precision integer)
        - 10
        - 0b10 (2 binary)
        - 0o10 (8 octal)
        - 0x10 (16 hexadecimal)
        - int(3.5) - 3
        - int(-3.5) - -3
        - int("496") - 496
        - int("1000",3) - 81

    - float (64-bit floating point numbes)
        - 3.125 - 3.125
        - 3e8 - 300000000.0
        - 1.616e-35 -1.616e-35
        - float(7) - 7.0
        - float("nan") - nan
        - float("inf") - inf
        - float("-inf") - -inf
        - 3.0 +1  - 4.0
    - NoneType (the null object)
        - None
        - a = None
        - a is None - True
    - bool (true or false)
        - bool(0) - False
        - bool(42) - True
        - bool(0.0) - False
        - bool(0.207) - True
        - bool(-1.117) - True
        - bool([]) - False
        - bool([1,5,9]) - True
        - bool("") - False
        - bool("Spam") - True
        - bool("False") - True

Relational Opreators:
    - ==
    - !=
    - <
    - >
    - <=
    - >=

Control Flow:
    - Conditional Statement (Branch execution based on the value of an expression)
    - if True:
        print("It is True")
    - if exp:
        ....
      else:
        ....
    - if exp:
        ....
      elif:
        ....
      else:
        ...

While-loops:
    while True:
...     response = input()
...     if int(response) % 7 ==0:
...         break
...     print("This is not divisible by 7")
