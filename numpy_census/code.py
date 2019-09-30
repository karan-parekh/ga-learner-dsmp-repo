# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data = np.genfromtxt(path, delimiter=",", skip_header=1)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census = np.concatenate((data, new_record))
print(census)   
#Code starts here



# --------------
#Code starts here
age = np.array([x[0] for x in census])
print(age)
max_age = np.max(age)
print(max_age)
min_age = np.min(age)
print(min_age)
age_mean = np.mean(age)
print(age_mean)
age_std = age.std()
print(age_std)



# --------------
#Code starts here
race_0 = np.array([x for x in census if x[2] == 0])
race_1 = np.array([x for x in census if x[2] == 1])
race_2 = np.array([x for x in census if x[2] == 2])
race_3 = np.array([x for x in census if x[2] == 3])
race_4 = np.array([x for x in census if x[2] == 4])

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

lens = [len_0, len_1, len_2, len_3, len_4]
min_len = min(lens)

for x in lens:
  if x == min_len:
    minority_race = lens.index(x)

print(minority_race)



# --------------
#Code starts here

senior_citizens = np.array([x for x in census if x[0] > 60])
working_hours = np.array([x[6] for x in senior_citizens])
working_hours_sum = np.sum(working_hours)
senior_citizens_len = len(senior_citizens)

avg_working_hours = working_hours_sum / senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here

high = np.array([x for x in census if x[1] > 10])  # high_education
low  = np.array([x for x in census if x[1] < 10])  # low_education 

high_income = np.array([x[7] for x in high])
low_income  = np.array([x[7] for x in low])

avg_pay_high = np.mean(high_income)
avg_pay_low  = np.mean(low_income) + 0.01

print(avg_pay_high)
print(avg_pay_low)



