# don't use max

students_scores = [int(height) for height in input("Enter Heights").split()]

max_score = students_scores[0]

for score in students_scores:
    if score > max_score:
        max_score = score  # update max score

print(students_scores)
print("The Highest Score is: <{}>".format(max_score))
print("The Highest Score is: <{}>".format(max(students_scores)))
