#You are given an integer N. You need to convert all zeroes of N to 5.

def convertFive(n):
    # Code here
    s = str(n)
    new = ''
    for alf in s:
        if alf == '0':
            new+='5'
        else:
            new+=alf
    n = int(new)
    return n
