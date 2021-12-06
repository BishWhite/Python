
PD= {0: {0: 0.5}}
def P(i, j):
    """
    P(0, 0) = 0.5,
    P(i, 0) = 0.0 dla i > 0,
    P(0, j) = 1.0 dla j > 0,
    P(i, j) = 0.5 * (P(i-1), j) + P(i, j-1)), dla i, j > 0
    """

    if i < 0 or j < 0:
        raise ValueError('Niepoprawne argumenty')

    if i == 0 and j == 0:
        return 0.5
    if i == 0:
        return 1.0
    if j == 0:
        return 0.0

    global PD
    if not i in PD:
        PD[i] = {j: 0.5 * (P(i-1, j) + P(i, j-1))}
    elif not j in P[i]:
        PD[i][j] = 0.5 * (P(i-1, j) + P(i, j-1))

    return PD[i][j]

