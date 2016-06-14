from sys import argv


def compress(s):
    c = 0
    r = ''
    for i in range(len(s)):
        if i == 0:
            r += s[i]
            c += 1
        else:
            if s[i] != s[i - 1]:
                if c > 1:
                    r += str(c)

                r += s[i]
                c = 1
            else:
                c += 1

    if s and c > 1:
        r += str(c)

    return r if len(r) < len(s) else s

if __name__ == '__main__':
    l = len(argv)
    if l == 1:
        print('Error: No string input')
    else:
        print(compress(argv[1]))
