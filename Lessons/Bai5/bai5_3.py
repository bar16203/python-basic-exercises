n = int(input("Enter number of subjects: "))
score = []
for i in range(n):
    s = float(input("Enter score: "))
    score.append(s)
total = 0
for i in score:
    total += i
avg = total / len(score)
print("Scores: ", score)
print("Average: ", avg)