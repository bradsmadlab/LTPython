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
    return dna1 > dna2


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    num_nucleotide = 0
    for char in dna:
        if char in nucleotide:
            num_nucleotide = num_nucleotide + 1
    
    return num_nucleotide


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    if dna2 in dna1:
        return True
    else: return False

def is_valid_sequence(dna):
    """ (str) - > bool

    Return True if and if DNA sequence is valid with letters 'ACTG' only.

    >>> is_valid_sequence('ACTG')
    True
    >>> is_valid_sequence('ACTGx')
    False)

    """

    nucleotide = True
    for char in dna:
        if char not in 'ATCG':
            nucleotide = False

    return nucleotide

def insert_sequence(dna1, dna2, splice):
    """ (str, str, int) -> str

    Return new_dna by combining dna1 and dna2 at position splice.
    
    >>> insert_sequence('ATCG', 'AA', 3)
    'ATCAAG'
    >>> insert_sequence('AAGTCCG', 'GA', 5)
    'AAGTCGACG'
    
    """
    new_dna = dna1[:splice] + dna2 + dna1[splice:]
    return new_dna

def get_complement(dna):
    """ (str) -> str

    Return complemt of dna for each base nucleotide.
    The complement of T is A, A is T, G is C, and C is G.
    
    >>> get_complement('A')
    'T'
    >>> get_complement('G')
    'C'
    
    """

    complement = ''
    for char_index in range(len(dna)):
        if dna[char_index] == 'T':
            complement = complement + 'A'
        elif dna[char_index] == 'A':
            complement = complement + 'T'
        elif dna[char_index] == 'G':
            complement = complement + 'C'
        else:
            dna[char_index] == 'C'
            complement = complement + 'G'
        
    return complement

def get_complementary_sequence(dna):
    """ (str) -> str

    Return complemtary_sequence of dna for each dna sequence.
    The complement of T is A, A is T, G is C, and C is G.
    
    >>> get_complementary_sequence('ATCG')
    'TAGC'
    >>> get_complementary_sequence('GACT')
    'CTGA'
    
    """

    complement = ''
    for char_index in range(len(dna)):
        if dna[char_index] == 'T':
            complement = complement + 'A'
        if dna[char_index] == 'A':
            complement = complement + 'T'
        if dna[char_index] == 'G':
            complement = complement + 'C'
        if dna[char_index] == 'C':
            complement = complement + 'G'
        
    return complement
    
