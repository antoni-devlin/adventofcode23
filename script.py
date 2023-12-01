import re
import fileinput

# sum = 0

# # Rewrite using map/filter/reduce
# for line in fileinput.input():
#   digits = re.findall("\d", line)
#   first = str(digits[0])
#   last = str(digits[-1])
#   print(first+last)
#   sum += int(first+last)

# print(sum)

#Bad news
print(sum([(lambda digits: int(digits[0]+digits[-1]))(re.findall("\d", line)) for line in fileinput.input()]))