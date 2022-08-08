#------------------------------------------------------------------------------
# perameters of dataset [age,sex,bmi,children,smoker,region,charges]
# int: age, bmi, children, charges(float)
# str: smoker(yes, no), region

# Questions, what are major factors to cost
# [Done]Whats the average cost
# [Done]What's the average age of participents
# [Done]where are the majority from
# what is the average age of someone with atleast 1 child
# What what's the average cost per region, sex, age?
# Smoker make a significant difference?
# BMI make a significant difference?
# Can you use this data to accurately predict insurance costs

# PROCESSING IDEAS
# Use SQL - Not option at this stage
# Make Dictionary - Done
# Look for NULL - Data is clean
# Looks for formatting issues
# Look for outliers
#------------------------------------------------------------------------------

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

# Insurance charges
charges = [float(charge['charges']) for charge in InsuranceDict.values()]

# Ages information
ages = [float(charge['age']) for charge in InsuranceDict.values()]

# Calculating Averages
sumCost = 0
sumAge = 0
for row in InsuranceDict.values():
    sumCost += float(row['charges'])
    sumAge += float(row['age'])
averageCost = round((sumCost / len(InsuranceDict)),2)
averageAge = round((sumAge / len(InsuranceDict)))

# BMI
BMI = [float(row['bmi']) for row in InsuranceDict.values()]

# Region information
regionList = [row['region'] for row in InsuranceDict.values()]
regionData = {}
for row in InsuranceDict.values():
    if row['region'] not in regionData:
        regionData[row['region']] = 1
    else:
        regionData[row['region']] += 1

# Sex distribution
sexList = [row['sex'] for row in InsuranceDict.values()]
sexData = {}
for row in InsuranceDict.values():
    if row['sex'] not in sexData:
        sexData[row['sex']] = 1
    else:
        sexData[row['sex']] += 1
# Children
childrenList = [row['children'] for row in InsuranceDict.values()]
children = {'Children':0, 'NoChildren':0} 
for row in InsuranceDict.values():
    if row['children'] != '0':
       children['Children'] += 1
    else:
       children['NoChildren'] += 1
# Smokers
smokerList = [row['smoker'] for row in InsuranceDict.values()]
smoker = {'Smoker':0, 'NonSmoker':0} 
for row in InsuranceDict.values():
    if row['smoker'] == 'yes':
       smoker['Smoker'] += 1
    else:
       smoker['NonSmoker'] += 1


#------------------------------------------------------------------------------
#       Understanding Data
#------------------------------------------------------------------------------

# What is the MAX charge someone is paying (What about the least)
print('The larges charge is:',max(charges), 'The smallest is:',min(charges))
print('The average cost of heath insurance is:', averageCost)

# Whats the age range we're looking at on this data set?
print('The oldes age is:',max(ages), 'The youngest is:',min(ages))
print('The Average age of participants is:', averageAge)

# Any regions polled higher then others worth mentioning?
print('The', max(regionData), 'region was polled significantly higher ' \
        'then the others')

# Sex information, are they polled equally?
print('The sexes were polled as', sexData, 'So not a significant bias')

# BMI information
print('The lowest BMI is:', round(min(BMI),2), "And the highest is",\
        round(max(BMI), 2))
print('The Average BMI is:', round(sum(BMI)/len(BMI),2))

# Children situation
print('The distribution of people with children is:', children)

# Smokers distribution
print('The distribution of smokers is:', smoker)


#------------------------------------------------------------------------------
#       Analytics
#------------------------------------------------------------------------------

# Make a function to see what effect 1 column has on insurance price
def costEffect(column):
    newDict = zip(column, charges) 
    index = 0
    sum1 = 0
    sum2 = 0
    for item in list(newDict):
        if item[index] == item[0]:
            sum1 += item[1]
    return sum1, sum2

print(costEffect(smokerList))
