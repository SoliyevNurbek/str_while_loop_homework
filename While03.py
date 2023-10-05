import string
def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    k=0
    while i in s:
        if i in string.punctuations:
            k+=1
    return len(s)
print(main("1254sfgdfgh.,%#&3"))