#------------------------------------------------------------------------------
#
#   Medical Insurance Data Analysis Project
#   Source  : CodeCademy (Data Scientist)
#   Author  : Cameron Schweeder
# 
#------------------------------------------------------------------------------

import csv

#------------------------------------------------------------------------------
#       Creating a Dictionary for Further study
#       And lists for key values
#------------------------------------------------------------------------------

# Creating a dict with all the records for futher processing
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

minCharge = 9999999999999999 
maxCharge = 0
minMax = {'Smallest':0, 'Largest':0}


# Max and Min charge
for key, item in InsuranceDict.items():
    if float(item['charges']) > maxCharge:
        maxCharge = float(item['charges'])
        minMax['Largest'] = item
    elif float(item['charges']) < minCharge:
        minCharge = float(item['charges'])
        minMax['Smallest'] = item


#------------------------------------------------------------------------------
#       Understanding Data
#------------------------------------------------------------------------------

print(
"\n-------------------------------------------------------------------------------"
)
print('\n   General queries on the insurance costs data set\n') 
print(
"-------------------------------------------------------------------------------\n"
)


# What is the MAX charge someone is paying (What about the least)
print('The larges charge is: ${:,.2f}, The smallest is: ${:,.2f}'.format(
                                                max(charges),min(charges)))
print('The average cost of heath insurance is: ${:,.2f}'.format(averageCost))

# Whats the age range we're looking at on this data set?
print('The oldes age is:',max(ages), 'The youngest is:',min(ages))
print('The Average age of participant is:', averageAge)

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

# Displaying Min and Max charge information
print("\nThe person with the highest Insurance cost has these factors;")
print(minMax['Largest'])
print("\nThe person with the lowest Insurance cost has these factors;")
print(minMax['Smallest'])


#------------------------------------------------------------------------------
#       Analytics
#------------------------------------------------------------------------------

# A function to average the costs of different values from any category
def costEffect(columnList):
    # Create a dictionary of costs per value
    newDict = {}
    zipList = list(zip(columnList, charges))
    for item in zipList:
        if item[0] not in newDict:
            newDict[item[0]] = [item[1]]
        else:
            newDict[item[0]].append(item[1])
   
   # Average all the costs for each value
    for key in newDict:
        newDict[key] = sum(newDict[key]) / len(newDict[key])

    return newDict



# A function to calculate value average against overall average from costEffect
def vsAverage(columnList):
   
    valueAverage = costEffect(columnList)
   # calculate the difference between the value and the average
   # get use the difference to calculate the percentage over or under average
    for key, item in valueAverage.items():
        difference = item - averageCost
        percent = (difference / averageCost) * 100
        valueAverage[key] = round(percent, 1)
    return valueAverage
    


# Smoker specific
smokerPercent = vsAverage(smokerList)
smokerAvg = costEffect(smokerList)


# Region: East over West
regionAvg = costEffect(regionList)
eastVsWest = {'East':(regionAvg['southeast']+regionAvg['northeast'])/2,
                'West':(regionAvg['southwest']+regionAvg['northwest'])/2}
eastOverWest = (eastVsWest['East'] - eastVsWest['West']) / eastVsWest['West'] 


# Children
childrenAVG = costEffect(childrenList)
tempAvg = 0
for key, avg in childrenAVG.items():
    if key != '0':
        tempAvg += avg

withChild = {'0':childrenAVG['0'], '1 or more':tempAvg/(len(childrenAVG)-1)}
childDiff = (withChild['1 or more'] - withChild['0']) / withChild['0']


# BMI
roundedBMI = sorted([round(bmi) for bmi in BMI])
BMIAvg = costEffect(roundedBMI)
#print(BMIAvg)


# Age
ageAvg = costEffect(ages)


# Sex
sexAvg = costEffect(sexList)
sexDiff = (sexAvg['male'] - sexAvg['female']) / sexAvg['female']

#------------------------------------------------------------------------------
#       Final conclusions
#------------------------------------------------------------------------------

print(
"\n-------------------------------------------------------------------------------"
)
print('\n   There are many factors that go into insurance costs\n'\
        '   The below calculations are based on overall average, and doesn\'t \n'\
        '   consider all the different variables\n') 
print(
"-------------------------------------------------------------------------------\n"
)


# Smoker effect on costs
print('Smokers pay an average of {}% over average insurance costs'.format(
                                                    smokerPercent['yes']))

print("Their average insurance cost is ${:,.2f}!".format(smokerAvg['yes']))


# Children
print("People with children pay {:.2%} more than those with none(No significant"\
        " premium)".format(childDiff))


# BMI
# print("")


# Region
print("The eastern regions are paying {:.2%} more then the West".format(
                                            eastOverWest))


# Age
#print("")


# sex
print("Males pay {:.2%} more than Females".format(sexDiff))
