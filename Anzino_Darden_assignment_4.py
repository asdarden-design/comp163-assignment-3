# test 1 cases
student_name = "Aznino Darden"  # Replace with your actual name
current_gpa = 3.2  # Replace with float (1.0 to 4.0)
study_hours = 25   # Integer
social_points = 50 # Integer
stress_level = 30  # Integer (0-100)
print(f"Welcome, {student_name}!")
print(f"Starting stats:")
print(f" Current GPA: {current_gpa}")
print(f" Study Hours: {study_hours}")
print(f" Social Points: {social_points}")
print(f" Stress Level: {stress_level}")
#test 2 cases
print("Choose your course load:")
print("easy) Light (12 credits)")
print("mid) Standard (15 credits)")
print("cry) Heavy (18 credits)")
choice = input("Your choice: ")

if choice == "easy":
    if current_gpa >= 3.0:
        study_hours -= 5
        stress_level -= 10
    else:
        study_hours -= 2
        stress_level -= 5
elif choice == "mid":
    # Medium impact
    if current_gpa >= 3.0:
        study_hours += 0  # no change
        stress_level += 0
    else:
        study_hours += 5
        stress_level += 10
elif choice == "cry":
    if current_gpa >= 3.5:
        study_hours += 10
        stress_level += 20
    else:
        study_hours += 15
        stress_level += 30
else:
    print("Invalid choices.")

print(f" Study Hours: {study_hours}")
print(f" Stress Level: {stress_level}")
# test 3 cases
study_options = ["Programming", "Math", "English", "History"]
user_choice = input("Choose your study subject: ")
if user_choice in study_options:
    if user_choice == "Programming" or user_choice == "Math" and current_gpa < 3.0:
        current_gpa += 0.3
        social_points -= 5
        print("good luck, you'll need it.")
    elif user_choice == "English" and social_points >= 40:
        current_gpa += 0.2
        social_points += 5
        print("Your taking a class that you should pass easily.")
    elif user_choice == "History" or (social_points < 40 or stress_level > 50):
        current_gpa += 0.1
        social_points -= 10
        print("If you fail this i'm demoting you to foolish")
    else:
        if user_choice not in study_options:
            print("Invalid")
if user_choice != "5":
    print("Abnormal behavior")
# test 4 cases
# final statistics
print(f"Final GPA: {current_gpa}")
print(f"Final Study Hours: {study_hours}")
print(f"Final Social Points: {social_points}")
print(f"Final Stress Level: {stress_level}")

# Generate different endings based on stats
if current_gpa >= 3.5 and social_points >= 60:
    print("You're doing good, keep it up lest you fall behind.")
elif current_gpa < 3.0 and stress_level > 50:
    print("You are being foolish, mellow out before you crash out and then get back to work.")
elif current_gpa is 2.0 or current_gpa <= 2.0:
    print("Warning: Your GPA is below the acceptable level. You need to change your methods or everything or else you're not going to make it.")
elif current_gpa is not 2.0 and current_gpa > 2.0:
    print("You're still surviving at least, work a little harder and you can beat this course. I'm sure of it!")
else:
    print("Keep pushing forward, the moment you give up is the moment you lose. Every effort counts!")
