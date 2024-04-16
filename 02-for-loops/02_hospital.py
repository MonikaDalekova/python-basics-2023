time_period = int(input())

doctors = 7
every_day = 0
treated_patients = 0
nontreated_patients = 0

for every_day in range(0, time_period):
    patients = int(input())
    every_day += 1
    if every_day % 3 == 0 and nontreated_patients > treated_patients:
        doctors += 1

    if patients > doctors:
        treated_patients += doctors
        nontreated_patients += (patients - doctors)
    else:
        treated_patients += patients
print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {nontreated_patients}.")