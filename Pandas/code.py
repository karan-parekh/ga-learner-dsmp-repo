# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 

# code starts here
bank = pd.read_csv(path)

categorical_var = bank.select_dtypes(include='object')
print(categorical_var)

numerical_var = bank.select_dtypes(include='number')
print(numerical_var)

# code ends here


# --------------
# code starts here
banks = bank.drop(['Loan_ID'], axis=1)
bank_mode = banks.mode
banks = banks.fillna(bank_mode)

print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here




avg_loan_amount = pd.pivot_table(banks, index=['Gender', 'Married', 'Self_Employed'], values='LoanAmount', aggfunc=np.mean)


# --------------

# code starts here
# self_employeed = banks['Self_Employed'] == 'Yes'
# loan_status_y = banks['Loan_Status'] == 'Y'
# loan_approved_se = banks[self_employeed & loan_status_y]

# not_self_employeed = banks['Self_Employed'] == 'No'
# loan_approved_nse = banks[not_self_employeed & loan_status_y]

loan_approved_se = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')]
loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')]

percentage_se = (len(loan_approved_se) / 614) * 100
percentage_nse = (len(loan_approved_nse) / 614) * 100

print(percentage_se)
print(percentage_nse)
# code ends here


# --------------
# code starts here






loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12 if isinstance(x, float) else None)
loan_term_without_na = loan_term.dropna() >= 25
# print(loan_term)
# big_loan_term = len(loan_term_without_na)
big_loan_term = loan_term_without_na.value_counts()[True]
print(big_loan_term)

# code ends here


# --------------
# code starts here

loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']
mean_values = loan_groupby.mean()
print(mean_values)

# code ends here


