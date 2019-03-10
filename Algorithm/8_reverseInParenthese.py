def reverseInParentheses(inputString):
    tmp=inputString
    while True:
        if ')' in tmp:
            b = tmp.index(')')
            a = max([i for i, j in enumerate(tmp[:b]) if j == '('])
            tmp = tmp[:a]+tmp[a:b+1][::-1][1:-1]+tmp[b+1:]
            print(tmp)
        else:break
    return tmp
print(reverseInParentheses('foo(bar(baz))blim(hi)'))
#foobazrabblimih