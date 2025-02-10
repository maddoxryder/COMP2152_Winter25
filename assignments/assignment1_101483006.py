# Maddox Duggan
# Assignment 1

# variables
gym_member = "Alex Alliton" # string
prefered_weight_kg = 20.5 # float
highest_reps = 25 # int
membership_active = True # boolean

# dictionary
workout_stats = {
    "Alex": (30,45,20),
    "Jamie": (25,40,35),
    "Taylor": (50,30,25)
}

# d.
for friend, minutes in workout_stats.items():
    total_minutes = sum(minutes)
    workout_stats[f"{friend}_Total"] = total_minutes

# 2D List to store workout minutes
# Data type: Nested List
workout_list = [list(minutes) for friend, minutes in workout_stats.items() if "_Total" not in friend]

# Slicing workout_list
# Extracting yoga and running minutes for all friends
yoga_running = [row[:2] for row in workout_list]
print("Yoga & Running Minutes:", yoga_running)

# Extracting weightlifting minutes for the last two friends
weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Weightlifting Minutes for Last Two Friends:", weightlifting_last_two)

# Checking for friends with 120+ total workout minutes
for friend, total in workout_stats.items():
    if "_Total" in friend and total >= 120:
        print(f"Great job staying active, {friend.replace('_Total', '')}!")

# User input for friend's workout data
friend_name = input("Enter a friend's name to view their workout stats: ")
if friend_name in workout_stats:
    print(f"Workout stats for {friend_name}: Yoga = {workout_stats[friend_name][0]} mins, "
          f"Running = {workout_stats[friend_name][1]} mins, "
          f"Weightlifting = {workout_stats[friend_name][2]} mins")
    print(f"Total workout minutes: {workout_stats[friend_name + '_Total']}")
else:
    print(f"Friend {friend_name} not found in the records.")

# Finding friend with highest and lowest total workout minutes
total_workout_entries = {k: v for k, v in workout_stats.items() if "_Total" in k}
max_friend = max(total_workout_entries, key=total_workout_entries.get).replace('_Total', '')
min_friend = min(total_workout_entries, key=total_workout_entries.get).replace('_Total', '')

print(f"Friend with highest total workout minutes: {max_friend}")
print(f"Friend with lowest total workout minutes: {min_friend}")
