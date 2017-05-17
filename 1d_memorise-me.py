def memorise_me():
    list_range = raw_input()
    list_items = raw_input().split()
    queries = int(raw_input())
    for i in range(queries):
        query = raw_input()
        count = 0
        for j in list_items:
            if query == j:
                count += 1
        if count == 0:
            print "NOT PRESENT"
        else:
            print count
memorise_me()

# best answer
#  n = input()
#  inp = raw_input().split(' ')[:n]
#  freq = {}
#  for i in inp:
#      if i not in freq:
#          freq[i] = 1
#      else:
#          freq[i] += 1
#  q = input()
#  for i in range(q):
#      j = raw_input()
#      if j not in freq:
#          print 'NOT PRESENT'
#      else:
#          print freq[j]
