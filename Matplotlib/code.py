# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(path)
loan_status = data['Loan_Status'].value_counts()

loan_status.plot(kind='bar')
#Code starts here


# --------------
#Code starts here

property_and_loan = data.groupby(['Property_Area', 'Loan_Status'])
property_and_loan = property_and_loan.size().unstack()

plt.plot(kind='bar', stacked=False)
plt.xticks(rotation=45)
plt.yticks(rotation=45)

plt.xlabel('Property_Area')
plt.ylabel('Loan_Status')

plt.show()




# --------------
#Code starts here

education_and_loan = data.groupby(['Education', 'Loan_Status'])
education_and_loan = education_and_loan.size().unstack()

plt.plot(kind='bar', stacked=True, figsize=(15, 10))

plt.xlabel('Education')
plt.ylabel('Loan_Status')

plt.xticks(rotation=45)
plt.yticks(rotation=45)

plt.show()


# --------------
#Code starts here

graduate = data[data['Education'] == 'Graduate']

not_graduate = data[data['Education'] == 'Not Graduate']

graduate['LoanAmount'].plot(kind='density', label='Graduate')

not_graduate['LoanAmount'].plot(kind='density', label='Not Graduate')

plt.show()
#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here

fig, (ax_1, ax_2, ax_3) = plt.subplots(nrows = 3, ncols = 1)
res_1 = data.groupby(['ApplicantIncome', 'LoanAmount'])
res_1.plot.scatter(x='ApplicantIncome', y='LoanAmount', ax=ax_1)
ax_1.set_title('Applicant Income')

res_2 = data.groupby(['CoapplicantIncome', 'ApplicantIncome'])
res_2.plot.scatter(x='CoapplicantIncome', y='ApplicantIncome', ax=ax_2)
ax_2.set_title('Coapplicant Income')


data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
res_3 = data.groupby(['TotalIncome', 'LoanAmount'])
res_3.plot.scatter(x='TotalIncome', y='LoanAmount', ax=ax_3)
ax_3.set_title('Total Income')

plt.show()


