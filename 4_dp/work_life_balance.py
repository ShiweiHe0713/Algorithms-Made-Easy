from numpy import random

def calculate_max_happiness(n, b, p):
    C = [0] * (n + 1)  # Maximum happiness up to hour i
    decision = [False] * (n + 1)  # Track study decisions

    # Base cases
    for i in range(1, min(b+1, n+1)):
        C[i] = 0  # Can't study within the first b hours
    
    # Compute C[i] for i from 1 to n
    for i in range(b+1, n+1):
        if i-b-1 >= 0:
            if C[i-1] < C[i-b-1] + p[i]:
                C[i] = C[i-b-1] + p[i]
                decision[i] = True
            else:
                C[i] = C[i-1]
        else:
            C[i] = C[i-1]  # Can't study at i if it violates the b-hour rule
    
    return C, decision

def find_study_hours(n, b, decision):
    study_hours = []
    i = n
    while i > 0:
        if decision[i]:
            study_hours.append(i)
            i -= b + 1  # Skip back b+1 hours as we must have not studied for b hours before a study hour
        else:
            i -= 1
    study_hours.reverse()  # To get the hours in chronological order
    return study_hours

# p = random.randint(10, size=(10))
n = 10  # Total hours
b = 1   # Hours of rest required before studying
p = [0, 3, 2, 6, 1, 5, 4, 8, 3, 7, 2]  # Happiness values, assuming p[0] is a placeholder

C, decision = calculate_max_happiness(n, b, p)
study_hours = find_study_hours(n, b, decision)

print("Maximum Happiness:", C[n])
print("Study Hours:", study_hours)

