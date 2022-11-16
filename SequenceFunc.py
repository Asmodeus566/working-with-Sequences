def FindSequence(spisoc, sequence: str, allOccurrences = True, together = False) -> int:
    """
    This function returns the number of consecutive characters or sequences of characters
    in a given string or list.

    Parameters
    ----------
    spisoc : Iterable
        A list of strings
        OR String
    sequence : str
        Sequence to search for
    AllOccurrences : bool
        Default: True
        Example: FindSequence('AAACACCC', 'C', True) Returns 4 occurrences of the C character in the string

    together: boll
        Default: False
        Example: FindSequence('AAACACCC', 'C', together=True) Returns 2 occurrences sequences of C characters

    Returns
    -------
    int - number of sequences
    """
    if not together:
        return len(spisoc.split(sequence))-1
    
    spisoc = list(map(str, spisoc))

    for i in range(len(spisoc)):
        if spisoc[i] not in sequence:
            spisoc[i] = ' '

    return len(''.join(spisoc).split()) if len(sequence) == 1 else len(''.join(spisoc).split(sequence))-1

def maxSequence(spisoc, sequence: str) -> str:
    """
    This function returns the maximum consecutive characters or sequences of characters
    in a given string or list.

    Parameters
    ----------
    spisoc : Iterable
        A list of strings
        OR String
    sequence : str
        A character or sequence of characters
    Returns
    -------
    string - the maximum consecutive characters or sequences of characters
    """
    spisoc = list(map(str, spisoc))

    for i in range(len(spisoc)):
        if spisoc[i] not in sequence:
            spisoc[i] = ' '

    return max(''.join(spisoc).split())

def minSequence(spisoc, sequence: str) -> str:
    """
    This function returns the minimum consecutive characters or sequences of characters
    in a given string or list.

    Parameters
    ----------
    spisoc : Iterable
        A list of strings
        OR String
    sequence : str
        A character or sequence of characters
    Returns
    -------
    string - the min consecutive characters or sequences of characters
    """
    spisoc = list(map(str, spisoc))

    for i in range(len(spisoc)):
        if spisoc[i] not in sequence:
            spisoc[i] =' '
    return min(''.join(spisoc).split())

