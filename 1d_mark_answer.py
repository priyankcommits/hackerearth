inp = map(int, raw_input().split())
arr = map(int, raw_input().split())
maxdiff = inp[1]
answers = 0
skip = 0
for i in arr:
    if i > maxdiff:
        skip = skip + 1
    else:
        answers = answers+1
    if skip >= 2:
        break
print answers

# above is the best answer
