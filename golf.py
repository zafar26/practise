course =[4, 4, 4, 4, 5, 3, 3, 4, 3, 5, 4, 4, 3, 4, 5, 4, 4, 5]
result = ['double-bogey', 'par', 'par', 'double-bogey', 'eagle', 'par', 'bogey', 'birdie', 'birdie', 'bogey', 'par', 'birdie', 'par', 'par', 'par', 'par', 'bogey', 'par']
score = 0
for i in range(len(course)):
    if result[i] == "eagle" :
        score += course[i] - 2      
    if result[i] ==  "birdie":
        score += course[i] - 1
    if result[i] ==  "bogey":
        score += course[i] + 1
    if result[i] ==  "double-bogey":
        score += course[i] + 2
    if result[i] == "par":
        score += course[i] + 0

print(score)