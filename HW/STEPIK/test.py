"""Test.assert_equals(likes([]), 'no one likes this')
Test.assert_equals(likes(['Peter']), 'Peter likes this')
Test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
Test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
Test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')"""

# def likes(names):
#     n = len(names)
#     return {
#         0: 'no one likes this',
#         1: '{} likes this',
#         2: '{} and {} like this',
#         3: '{}, {} and {} like this',
#         4: '{}, {} and {others} others like this'
#     }[min(4, n)].format(*names[:3], others=n-2)
#
# print(likes(['Alex', 'Jacob', 'Mark', 'Max']))

"""Test.assert_equals(digital_root(16), 7)
Test.assert_equals(digital_root(942), 6)
Test.assert_equals(digital_root(132189), 6)
Test.assert_equals(digital_root(493193), 2)"""

# def digital_root(n):
#     n = str(n)
#     while len(n) > 1:
#         n = list(n)
#         res = int()
#         for el in n:
#             res = res + int(el)
#         n = str(res)
#     return n
#
# print(digital_root(493193))


# def digital_root(n):
#     return n if n < 10 else digital_root(sum(map(int,str(n))))

# def digital_root(n):
#     return n%9 or n and 9
# print(942 % 9)
# print(digital_root(9))

"""accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"""

# def accum(s):
#     itr = iter(range(1, len(s)+1))
#     return '-'.join(str(i) for i in [((el * next(itr)).lower()).title() for el in list(s)])
#     #[((el * (s.index(el) + 1)).lower()).title() for el in list(s)])
#
# print(accum('ZpglnRxqenU'))
#
# return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

"""Test.assert_equals(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
Test.assert_equals(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])"""

# def anagrams(word, words):
#     return [el for el in words if sorted(el) == sorted(word)]
#
# print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))

"""n = 5
ar = [[0 for i in range(n)] for i in range(n)]

for i in range(len(ar)):
    print(ar[i])"""

# def multiples(x):
#     return [i for i in range(1, x) if x % i == 0]
#
#
# print(multiples(9))

"""spiral"""

n = 6
ar = [[0 for i in range(n)] for i in range(n)]
el = 1
qel = 0

for ring in range(n//2):

    for i in range(n - qel):
        ar[ring][i+ring] = el
        el += 1
    for i in range(ring+1, n-ring):
        ar[i][-ring-1] = el
        el += 1
    for i in range(ring+1, n-ring):
        ar[-ring-1][-i-1] = el
        el += 1
    for i in range(ring+1, n-(ring+1)):
        ar[-i-1][ring] = el
        el += 1

    qel += 2

for i in range(len(ar)):
    print(ar[i])