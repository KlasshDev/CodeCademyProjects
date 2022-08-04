# perameters of dataset [age,sex,bmi,children,smoker,region,charges]
# int: age, bmi, children, charges(float)
# str: smoker(yes, no), region

# Questions, what are major factors to cost
# [Done]Whats the average cost
# What's the average age of participents
# where are the majority from
# what is the average age of someone with atleast 1 child
# What what's the average cost per region, sex, age?
# Smoker make a significant difference?
# BMI make a significant difference?
# Can you use this data to accurately predict insurance costs

# PROCESSING IDEAS
# Use SQL
# Make Dictionary
# Look for NULL
# Looks for formatting issues
# Look for outliers
import csv

#------------------------------------------------------------------------------
#       Creating a Dictionary for Further study
#       And lists for key values
#------------------------------------------------------------------------------

# Creating a dict with all the records for futher processing
# Numbering all records via index
medical_insurance_csv = {}
with open('insurance.csv', newline='') as insurance_csv:
    read_csv = csv.DictReader(insurance_csv)
    InsuranceDict = {}
    index = 1
    for row in read_csv:
        InsuranceDict[index] = row
        index += 1


charges = [float(charge['charges']) for charge in InsuranceDict.values()]
ages = [float(charge['age']) for charge in InsuranceDict.values()]

#------------------------------------------------------------------------------
#       Understanding Data
#------------------------------------------------------------------------------

# Calculating Averages
sumCost = 0
sumAge = 0
for row in InsuranceDict.values():
    sumCost += float(row['charges'])
    sumAge += float(row['age'])
averageCost = round((sumCost / len(InsuranceDict)),2)
averageAge = round((sumAge / len(InsuranceDict)))
print('The Average age of participants is:', averageAge)
print('The average cost of heath insurance is:', averageCost)


# What is the MAX charge someone is paying (What about the least)
print('The larges charge is:',max(charges), 'The smallest is:',min(charges))
print('The oldes age is:',max(ages), 'The youngest is:',min(ages))

# What group is paying above average
# Make a function to test againsed different rows vs the average cost
        
# 22% of claims involving Smokers are paying above average    


