# Самая далекая планета

def find_farthest_orbit(orbits):
    S = list()
    S.append([round(3.14 * i * j, 2) for i, j in orbits])
    S = S[0]
    arr = list()
    arr = zip(S, orbits)
    arr2 = list()
    [arr2.append((s, xy)) for s, xy in arr if xy[0] != xy[1]]
    max_s = max(arr2)
    print(max_s[1])

orbits = [(1, 3), (2.5, 10), (7, 2), (10.5, 10.5), (6, 6), (4, 3), (8.5, 9)]
find_farthest_orbit(orbits)
