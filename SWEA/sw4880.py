def get_winner(p1, p2, cards):
    c1 = cards[p1 - 1]
    c2 = cards[p2 - 1]
    
    win_cases = {1: 3, 2: 1, 3: 2}
    
    if c1 == c2:
        return p1 if p1 < p2 else p2
    elif win_cases[c1] == c2:
        return p1
    else:
        return p2

def divide(i, j, cards):
    if i == j:
        return i
    
    mid = (i + j) // 2
    