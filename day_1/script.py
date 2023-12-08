import re
import fileinput

# Part 1
sum1 = 0

# Rewrite using map/filter/reduce
for line in fileinput.input():
    digits = re.findall(r"\d", line)
    if digits:
        first = str(digits[0])
        last = str(digits[-1])
        sum1 += int(first + last)

print("Part 1 answer:", sum1)

# Part 2
digitDict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

sum2 = 0


def replace_words_with_numbers(text):
    for word, number in digitDict.items():
        text = text.replace(word, number)
    return text

search_results = {}
# search_results.update({"key":"value"})

pattern = re.compile("|".join(k for k in digitDict.keys()))
for line in fileinput.input():
    
    # replacedLine = pattern.sub(lambda x: digitDict[x.group()], line)
    # print(replacedLine)
    # digits = re.findall(r"\d", replacedLine)
    # first = str(digits[0])
    # last = str(digits[-1])
    # sum2 += int(first + last)

print("Part 2 answer:", sum1 + sum2)