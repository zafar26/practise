timesum = ["5:39:42", "10:02:08", "8:26:33"]
trimed_time =[]
total_hours = 0
total_minutes = 0
total_seconds = 0
print(5/2)
print(5//2)
for i in range(len(timesum)):
    trimed_time = timesum[i].rsplit(":")
    hours = trimed_time[0]
    minutes = trimed_time[1]
    seconds = trimed_time[2]
    
    total_hours += int(hours) 
    total_minutes += int(minutes) 
    total_seconds += int(seconds)
    if total_seconds / 60 >=1:
        total_minutes += (total_seconds // 60)
        total_seconds = (total_seconds % 60)
    if total_minutes / 60 >=1:
        total_hours += (total_minutes // 60)
        total_minutes = (total_minutes % 60)
print(total_hours, total_minutes,total_seconds)

