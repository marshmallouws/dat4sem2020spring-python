"""-------------------------------- 03 Plotting -----------------------------------
with the following dataset:

student_attendance = {'day1':33, 'day2':34,'day3':29,'day4':31,'day5':28,'day6':26,'day7':30}

create a line graph showing attendance over time. hint: use keys() and values() method of the dictionary.
add title and labels for x and y axis.
"""

import matplotlib.pyplot as plt

student_attendance = {'day1':33, 'day2':34,'day3':29,'day4':31,'day5':28,'day6':26,'day7':30}

plt.figure()
for s in student_attendance:
    plt.scatter(s, student_attendance.get(s))

plt.show()

"""
1.1     Using this dict: `{'Holger':25,'Helga':54,'Hasse':76,'Halvor':12,'Hassan':43,
        'Hulda':31,'Hansi':102}` 
        display a bar plot of the people and there ages sorted by age.  
1.2     Add title and x and y axis labels to the bar plot
"""

persons = {'Holger':25,'Helga':54,'Hasse':76,'Halvor':12,'Hassan':43,'Hulda':31,'Hansi':102}

plt.figure()

ages = list(persons.values())
ages.sort()
names = list(persons.keys())

plt.bar(ages, names, width=2, align='center')

plt.xlabel('Age', fontsize=12)
plt.ylabel('Name', fontsize=12)

plt.show()


"""
2.1     Using the kkdata module with population data from Copenhagen display a line graph 
        showing the population development over time (year on x and population on y)
"""
"""
import kkdata

plt.figure()
citizens_year = {}

for year in kkdata.STATISTICS:
    neighbourhoods = kkdata.STATISTICS[year].keys()
    age_range = set([])

    for n in neighbourhoods:
        age_range.update(kkdata.STATISTICS[year][n].keys()) #update() on set adds any new elements
    
    no_of_citizens = 0

    for n in neighbourhoods:
        for age in age_range:
            if age in kkdata.STATISTICS[year][n].keys():
                c_codes = set(kkdata.STATISTICS[year][n][age].keys())
                for f_code in c_codes:
                    no_of_citizens += kkdata.STATISTICS[year][n][age][f_code]
    
    citizens_year[year] = no_of_citizens

no = list(citizens_year.values())
year = list(citizens_year.keys())

plt.bar(year, no, width=0.5, align='center')
"""

"""
1.  based on kkdata show the distribution of citizenships in all copenhagen areas and all ages in 2015
    hint if you need help to get the summarized population by citizenship from kkdata you can use:
    import cit
    print(cit.get_citizen_dist(2015))
2.  remove the danes (code 5100) and show only the top 10 nationalities.
"""
import kkdata
import cit
import operator

plt.figure()
citizen_dist = cit.get_citizen_dist(2015)
top_10_cit = {}

sorted_citizen_dist = dict(sorted(citizen_dist.items(), key=operator.itemgetter(1)))

out = dict(list(sorted_citizen_dist.items())[-11: -1])  

area_code = list(out.keys())
population = list(out.values())

plt.ylim(0, 5000)
plt.bar(area_code, population, width=0.5, align='center')
plt.show()