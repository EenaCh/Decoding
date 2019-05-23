s = input()
XYZ = ['0', '1', '2', '3', '4', '5', '6', '7', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ah = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
s = s.lower()

count_decod = 0
n = 1
while n != 0:
    s1 = ''
    i = 0
    n = 0
    while i < len(s)-3:
        if (s[i] == 'o') and (s[i+1] in XYZ) and (s[i+2] in XYZ) and (s[i+3] in XYZ):
            if s[i + 1] in ah:
                X = ah[s[i+1]]
            else:
                X = int(s[i+1])
            if s[i + 2] in ah:
                Y = ah[s[i+2]]
            else:
                Y = int(s[i+2])
            if s[i + 3] in ah:
                Z = ah[s[i + 3]]
            else:
                Z = int(s[i + 3])
            k = 64 * X + 8 * Y + Z
            if k < 256:
                s1 += chr(k)
                i += 4
                n = 1
                continue
        s1 += s[i]
        i += 1
    if i < len(s):
        s1 += s[i:]
    s = s1
    if n == 1:
        count_decod += 1
print(count_decod)