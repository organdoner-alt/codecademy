# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# write your update damages function here:
def damage_update(damages):
    updated_damages = []
    for damage in damages:
        if damage[-1] == "M":
            updated_damages.append(float(damage[0:-1]) * 1000000)
        elif damage[-1] == "B":
            updated_damages.append(float(damage[0:-1]) * 1000000000)
        else:
            updated_damages.append("Damages not recorded")
    return updated_damages
updated_damages = damage_update(damages)


# write your construct hurricane dictionary function here:
def create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
    zipped_hurricane_records = zip(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
    hurricane_dict = dict()
    num_hurricanes = len(names)
    for i in range(num_hurricanes):
        hurricane_dict[names[i]] = {"Name":names[i], 
                      "Month": months[i], 
                      "Year": years[i], 
                      "Maximum Sustained Winds": max_sustained_winds[i], 
                      "Affected Areas": areas_affected[i], 
                      "Damages": updated_damages[i], 
                      "Deaths": deaths[i]}
    return hurricane_dict
hurricane_dict = create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)

# write your construct hurricane by year dictionary function here:
def create_year_dictionary(hurricane_dict):
    hurricanes_by_year = {}
    for record in hurricane_dict:
        current_year = hurricane_dict[record]['Year']
        current_record = hurricane_dict[record]
        if current_year not in hurricanes_by_year:
            hurricanes_by_year[current_year] = [current_record]
        else:
            hurricanes_by_year[current_year].append(current_record)
    return hurricanes_by_year
hurricanes_by_year = create_year_dictionary(hurricane_dict)


# write your count affected areas function here:
def count_affected_areas(areas_affected):
    area_count_dict = dict()
    for areas in areas_affected:
        for area in areas:
            if area not in area_count_dict:
                area_count_dict[area] = 1
            else:
                area_count_dict[area] += 1
    return area_count_dict
area_count_dict = count_affected_areas(areas_affected)


# write your find most affected area function here:
def most_affected_area(area_count_dict):
    area_most_affected = max(area_count_dict, key=area_count_dict.get)
    area_most_affected_and_number = area_most_affected, area_count_dict[area_most_affected]
    return area_most_affected_and_number
area_most_affected_and_number = most_affected_area(area_count_dict)


# write your greatest number of deaths function here:
def get_deadliest_hurricane(names, deaths):
    hurricane_deaths = {names:deaths for [names, deaths] in zip(names, deaths)}
    most_deaths_name = max(hurricane_deaths, key=hurricane_deaths.get)
    most_deaths_value = hurricane_deaths[most_deaths_name]
    return most_deaths_name, most_deaths_value
most_deaths = get_deadliest_hurricane(names, deaths)


# write your catgeorize by mortality function here:
def get_mortality_scale(hurricane_dict):
    zero = []
    one = []
    two = []
    three = []
    four = []
    five = []
    for hurricane in hurricane_dict:
        deaths = hurricane_dict[hurricane]['Deaths']
        if deaths == 0:
            zero.append(hurricane_dict[hurricane])
        elif deaths > 0 and deaths < 101:
            one.append(hurricane_dict[hurricane])
        elif deaths > 100 and deaths < 501:
            two.append(hurricane_dict[hurricane])
        elif deaths > 500 and deaths < 1001:
            three.append(hurricane_dict[hurricane])
        elif deaths > 1000 and deaths < 10001:
            four.append(hurricane_dict[hurricane])
        else:
            five.append(hurricane_dict[hurricane])
    mortality_dict = {0:zero, 1:one, 2:two, 3:three, 4:four, 5:five}
    return mortality_dict
mortality_dict = get_mortality_scale(hurricane_dict)


# write your greatest damage function here:
def get_greatest_damage(hurricane_dict):
    greatest_damage = 0
    for hurricane in hurricane_dict:
        current_hurricane = hurricane_dict[hurricane]
        current_damage = hurricane_dict[hurricane]['Damages']
        if current_damage == 'Damages not recorded':
            continue
        elif current_damage > greatest_damage:
            greatest_damage = current_damage
    return current_hurricane['Name'], greatest_damage
greatest_damage = get_greatest_damage(hurricane_dict)


# write your catgeorize by damage function here:
def get_damage_rating(hurricane_dict):
    zero = []
    one = []
    two = []
    three = []
    four = []
    five = []
    for hurricane in hurricane_dict:
        current_hurricane = hurricane_dict[hurricane]
        damage = hurricane_dict[hurricane]['Damages']
        if damage == 'Damages not recorded':
            continue
        elif damage == 0:
            zero.append(current_hurricane)
        elif damage > 0 and damage <= 100000000:
            one.append(current_hurricane)
        elif damage > 100000000 and damage <= 1000000000:
            two.append(current_hurricane)
        elif damage > 1000000000 and damage <= 10000000000:
            three.append(current_hurricane)
        elif damage > 10000000000 and damage <= 50000000000:
            four.append(current_hurricane)
        else:
            five.append(current_hurricane)
    damage_rating = {0:zero, 1:one, 2:two, 3:three, 4:four, 5:five}
    return damage_rating
damage_rating = get_damage_rating(hurricane_dict)
