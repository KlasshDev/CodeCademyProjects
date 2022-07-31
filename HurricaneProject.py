# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 
        'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 
        'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 
        'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 
        'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 
        'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 
        'September', 'September', 'September', 'September', 'September', 
        'September', 'October', 'September', 'August', 'September', 'September', 
        'August', 'August', 'September', 'September', 'August', 'October', 
        'September', 'September', 'July', 'August', 'September', 'October', 
        'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 
        1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 
        2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 
        160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 
        175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], 
        ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], 
        ['The Bahamas', 'Northeastern United States'], 
        ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], 
        ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], 
        ['Jamaica', 'Yucatn Peninsula'], 
        ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], 
        ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], 
        ['Bermuda', 'New England', 'Atlantic Canada'], 
        ['Lesser Antilles', 'Central America'], 
        ['Texas', 'Louisiana', 'Midwestern United States'], 
        ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], 
        ['Cuba', 'United States Gulf Coast'], 
        ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], 
        ['Mexico'], ['The Caribbean', 'United States East coast'], 
        ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], 
        ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], 
        ['The Caribbean', 'United States East Coast'], 
        ['The Bahamas', 'Florida', 'United States Gulf Coast'], 
        ['Central America', 'Yucatn Peninsula', 'South Florida'], 
        ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], 
        ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], 
        ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], 
        ['Bahamas', 'United States Gulf Coast'], 
        ['Cuba', 'United States Gulf Coast'], 
        ['Greater Antilles', 'Central America', 'Florida'], 
        ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], 
        ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], 
        ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], 
        ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], 
        ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', 
        '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', 
        '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', 
        '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', 
        '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,
        18,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:


def convertToFloat(data):
    # Convert M to 000000 and B to 000000000 and convert string to float
    replacement = [] 
    finalReplacement = []

    for cost in data: # replace prefixes and decimals
        replacement.append(cost
                    .replace('.', '')
                    .replace('M', '000000')
                    .replace('B', '000000000'))
 
    for cost in replacement: # convert to float
        if cost == 'Damages not recorded':
           finalReplacement.append(cost) 
        else:
           finalReplacement.append(float(cost)) 
    return finalReplacement 


#print(convertToFloat())



# write your construct hurricane dictionary function here:

def aggrigateHurricane():

# Takes lists(names, months, years, max_sustained_winds, areas_affected, 
# convertToFloat(damages), deaths) and links them into a dictionary for each
# hurricane
# Example output: {{'Name': 'Cuba I', 'Month': 'October', 'Year': 1924, 
# 'Max Sustained Wind': 165, 'Areas Affected': ['Central America', 'Mexico', 
# 'Cuba', 'Florida', 'The Bahamas'], 'Damage': 'Damages not recorded', 
# 'Deaths': 90}

    # itterate over lists and create new dictionary
    # with template key as key, and list as value
    hurricanes = {}
    for index in range(len(names)):
        hurricanes[names[index]] = {
                    "Name": names[index],
                    "Month": months[index],
                    "Year": years[index],
                    "Max Sustained Wind": max_sustained_winds[index],
                    "Areas Affected": areas_affected[index],
                    "Damage": convertToFloat(damages)[index],
                    "Deaths": deaths[index]}
    return hurricanes

#print(aggrigateHurricane())
hurricanes = aggrigateHurricane()


# write your construct hurricane by year dictionary function here:

def yearOfHurricane():
# Make a list of hurricanes, key being the year.
# If there are multiple hurricanes per year, append them
    temp = aggrigateHurricane()
    hurricaneByYear = {}
    for key, value in temp.items():
        currentCane = [value]
        currentYear = value['Year']
        if currentYear not in hurricaneByYear:
            hurricaneByYear[currentYear] = currentCane
        else:
            hurricaneByYear[currentYear].append(currentCane)
    return hurricaneByYear


#print(yearOfHurricane())
HurricaneYears = yearOfHurricane()



# write your count affected areas function here:
'''
Create a function that counts how often each area is listed as an affected area
of a hurricane store and return the results in a dictionary where the keys are 
the affected areas and the vales are the counts.
'''

def areaFrequency():
    caneList = aggrigateHurricane()
    areaCount = {}
    for values in caneList.values():
        for area in values['Areas Affected']:
            if area not in areaCount:
                areaCount[area] = 1
            else:
                areaCount[area] += 1
    return areaCount

#print(areaFrequency())
HurricaneArea = areaFrequency()

# write your find most affected area function here:

'''
Find the area affected the most by hurricanes
'''
def displayMaxArea():
    areasAffected = areaFrequency()
    maxCount = 0
    maxArea = ''
    for key, value in areasAffected.items():
        if value > maxCount:
            maxArea = key
            maxCount = value
        else:
            pass
        return [maxArea, maxCount]

#print(displayMaxArea())




# write your greatest number of deaths function here:
'''
Write a function that finds the hurricane with the gratest amount of deaths
'''

def maxDeaths():
    # Create a dict with cane and death count
    caneDeaths = aggrigateHurricane()
    deathArea = {}
    for cane, values in caneDeaths.items():
        deathArea[cane] = values['Deaths']
#    print(deathArea) 

    # ittirate through the hurricanes and return the highest
    maxDeath = 0
    area = ''
    for cane, death in deathArea.items():
        if death > maxDeath:
            area = cane
            maxDeath = death
    return [area, maxDeath]
# print(maxDeaths())



# write your catgeorize by mortality function here:
'''
Rate hurricanes by mortality rate: 
    Mortality_scale = {0:0, 1:100, 2:500, 3:1000, 4:10000}
'''

def hurricaneRating():
    mortality_scale = {0:0, 1:100, 2:500, 3:1000, 4:10000}
    ratedHurricanes = {
                    0:[],
                    1:[],
                    2:[],
                    3:[],
                    4:[]    }
    canes = aggrigateHurricane()
    for cane, values in canes.items():
        if values['Deaths'] < 100:
            ratedHurricanes[0].append(cane)
        elif values['Deaths'] < 500:
            ratedHurricanes[1].append(cane)
        elif values['Deaths'] < 1000:
            ratedHurricanes[2].append(cane)
        elif values['Deaths'] < 10000:
            ratedHurricanes[3].append(cane)
        else:
            ratedHurricanes[4].append(cane)

    return ratedHurricanes

#print(hurricaneRating())
ratedHurricanes = hurricaneRating()


# write your greatest damage function here:
'''
Write a fucntion that finds the hurricane that cause the greatest amount of 
damages, and how costly it was
'''
def maxDamages():
    damagingHurricane = {}
    for cane, damages in hurricanes.items():
       damagingHurricane[cane] = damages['Damage']
   # print(damagingHurricane)
    maxDamage = 0
    damageCane = ''
    for cane, damage in damagingHurricane.items():
        if damage == 'Damages not recorded':
            pass
        elif damage > maxDamage:
           damageCane = cane
           maxDamage = damage
        else:
            pass
    return [damageCane, maxDamage]

print(maxDamages())



# write your catgeorize by damage function here:
'''
Rate your hurricanes by how costly they were
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
'''
def damagesRating():
    damageScale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
    ratedHurricanes = {
                    0:[],
                    1:[],
                    2:[],
                    3:[],
                    4:[]    }
    for cane, values in hurricanes.items():
        if values['Damage'] == 'Damages not recorded':
            ratedHurricanes[0].append(cane)
        elif values['Damage'] < 100000000:
            ratedHurricanes[0].append(cane)
        elif values['Damage'] < 1000000000:
            ratedHurricanes[1].append(cane)
        elif values['Damage'] < 10000000000:
            ratedHurricanes[2].append(cane)
        elif values['Damage'] < 50000000000:
            ratedHurricanes[3].append(cane)
        else:
            ratedHurricanes[4].append(cane)

    return ratedHurricanes

print(damagesRating())
damageRating = damagesRating()


