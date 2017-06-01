def valid_arch(arches, element, next_element):
    valid = True
    for arch in arches:
        if arch[0] > element or arch[1] < next_element:
            valid = False
    return valid


count = 0
for i in xrange(int(raw_input())):
    word_list = list(raw_input())
    arches = []
    valid = True
    for j in xrange(len(word_list)):
        char = word_list[j]
        element = j
        try:
            print element
            next_element = word_list[j:].index(char)
        except ValueError:
            pass
        if not valid_arch(arches, element, next_element):
            valid = False
            break
        else:
            arches.append((element, next_element))
    if valid:
        count += 1

print count

# best asnwer is (pretty cool)

#  n=int(raw_input())
#  lst=[raw_input() for x in range(n)]
#
#  count=0
#  for i in range(n):
#      mystr=lst[i]
#      newlst=list()
#      for mychar in mystr:
#          if len(newlst)==0 or newlst[len(newlst)-1]!=mychar:
#              newlst.append(mychar)
#          else:
#              newlst.pop()
#      if len(newlst)==0:
#          count=count+1
#  print count
