def flip(list_to_flip, bit_to_flip):
    list_to_flip[bit_to_flip+1] = 1
    return list_to_flip


def odd_or_even(flipped_list, start, end):
    list_to_eval = flipped_list[start+1:end+1]
    if int(list_to_eval[-1]) == 1:
        return "EVEN"
    else:
        return "ODD"

input_line_one = raw_input()
input_line_one_split = input_line_one.split(" ")
# n = int(input_line_one_split[0])
q = int(input_line_one_split[1])
n = raw_input()
N = n.split(" ")
result = ""
flipped = []
for i in range(0, q):
    Q = raw_input()
    Q_split = Q.split(" ")
    if int(Q_split[0]) == 1:
        flipped = flip(N, int(Q_split[1]))
    else:
        if flipped:
            result = odd_or_even(flipped, int(Q_split[1]), int(Q_split[2]))
        else:
            result = odd_or_even(N, int(Q_split[1]), int(Q_split[2]))
print result

# best asnwer
#  def f():
#      b = raw_input().split()
#      q = int(b[1])
#      a = raw_input().split()
#      for i in range(q):
#          b = raw_input().split()
#          if b[0] == '0':
#              if a[int(b[2]) - 1] == '0':
#                  print "EVEN"
#              else:
#                  print "ODD"
#          else:
#              t = int(b[1]) - 1
#              if a[t] == '0':
#                  a[t] = '1'
#              else:
#                  a[t] = '0'
#  f()
