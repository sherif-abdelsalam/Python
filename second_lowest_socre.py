# records = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     records.append((name,score))

# scores = sorted(set([score for name, score in records]))
# second_lowest = scores[1]
# names = sorted([name for name, score in records if score == second_lowest])

# for name in names:
#     print(name)


from __future__ import print_function
score_list = {}
for _ in range(int(input())):
    name = input()
    score = float(input())
    if score in score_list:
        score_list[score].append(name)
    else:
        score_list[score] = [name]
print(score_list)
new_list = []
for i in score_list:
    print(i)
    new_list.append([i, score_list[i]])

print(new_list)

new_list.sort()
print(new_list)

result = new_list[1][1]
result.sort()
print (*result, sep = "\n")
