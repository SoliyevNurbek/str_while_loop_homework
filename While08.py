def main(s):
    """
     
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    k=0
    while i<len(s):
        if int(s[i])%2==1:
            k+=1
        i+=1
    return k
print(main("15586763254562"))