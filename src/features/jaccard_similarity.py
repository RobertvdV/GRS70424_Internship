def jaccard_similarity(A, B):
    """Calculates the Jaccard similarity two sets.

    Args:
        A (Set): Set A
        B (Set): Set B

    Returns:
        Integer: 0.00 - 1.00
    """

    # Create sets just in case
    A = set(A)
    B = set(B)
    
    # Get intersection of two sets
    nominator = A.intersection(B)

    # Find union of two sets
    denominator = A.union(B)

    # Take the ratio of sizes
    similarity = len(nominator)/len(denominator)

    return similarity