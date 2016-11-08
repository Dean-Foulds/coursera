def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return get_length(dna1) > get_length(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if dna1.find(dna2):
        return True

def is_valid_sequence(dna):
    """ (str) -> bool
    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_seuence('atcgcgc')
    False
    >>> is_valid_sequence('atcggc')
    False
    """
    num_char = 0
    
    for char in dna:
        if not char in 'ATCG':
            num_char += 1

    return num_char == 0

def insert_sequence(x,y,z):
    """(str,str,int) -> str
    >>> insert_sequence('CCGG','AT',2)
    'CCATGG"
    """
    return x[:z] + y + x[z:]

def get_complement(c):
    """(str) -> str
    >>>get_complement('A')
    'T'
    """
    if c == 'A':
        return 'T'
    if c == 'C':
        return 'G'
    if c == 'G':
        return 'C'
    if c == 'T':
        return 'A'

def complementary_sequence(s):
    """ (str) -> str
    >>> ('AATTGGCC')
    'TTAACCGG'
    """
    res = ""
    for char in s:
        tot = res + (get_complement(char))
        
   
    
