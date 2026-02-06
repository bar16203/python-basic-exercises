scores = {
    "math" : 8,
    "physics" : 7.5,
    "chemistry": 9
}
total = 0
for s in scores:
    total += scores[s]
avg = total/len(scores)
print("Average: ", round(avg, 2))
for key in scores:
    print(key, " : ", scores[key])
