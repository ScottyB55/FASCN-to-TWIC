# Description
Takes an input FASCN represented as a Hex string
and converts it inot a TWIC string 

## How to Run
Run the test file provided for a quick check

```
python test.py
```

Import the FASCN to TWIC function and use it like this:
```
python
>>> from FASCN_to_TWIC import fascn_to_twic
>>> fascn_to_twic("D70339DA15256C10843C45A16858210D5B3CCC90870339A3F")
'70991545000072'
```