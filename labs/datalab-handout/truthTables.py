#working on bit xor truth logic

#needs to be logically equivalent to (A and not B) or (not A and B)
def bitxortruth(a, b):
    print (f"Got: {not(not (a and not b) and not (not a and b))} | Expected: {a^b}")

bitxortruth(1,1)
bitxortruth(1,0)
bitxortruth(0,1)
bitxortruth(0,0)