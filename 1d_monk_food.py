queries = int(raw_input())
items = []
for i in range(0, queries):
    query = map(int, raw_input().split())
    if query[0] == 1:
        try:
            print items.pop()
        except IndexError:
            print "No Food"
    else:
        items.insert(0, query[1])

# best answer:
#  t = int(raw_input())
#  stack = []
#  for _ in range(t):
#          line = raw_input()
#          if ' ' in line:
#                  val = int(line.split(' ')[1])
#                  stack.append(val)
#          else:
#                  if len(stack)==0:
#                          print 'No Food'
#                  else:
#                          print stack.pop()
