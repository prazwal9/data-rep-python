''' ASSIGNMENT 2
    1.Plot a line chart to show correlation between all the attributes in single panel.
    2.Draw scatter plot for any two columns(One Weather and One COVID-19) and also write their correlation in the caption of scatter plot.
    3.Find most causative weather parameter that affect the infection rate.'''

import pandas as pd
from matplotlib import pyplot as pl

data = pd.read_csv(r"C:\Users\Zwal's pc\Desktop\A1A2\Meghalaya(75008).csv")
print ("\nThe dataset:\n")
print (data)
data = data.fillna(data.median())

def one():
    #taking different attributes and plotting a line chart 
    new = data[['Date', 'Min_Temp', 'Max_Temp', 'Max_Humidity', 'Min_Humidity', 'Max_windspeed', 'Min_windspeed', 'Max_PM(2.5)','Min_PM(2.5)', 'Mortality']]
    pl.title("Relation between the attributes")
    pl.xlabel("Date")
    pl.xticks(rotation = 69)            #slightly tilts the xlabels
    pl.ylabel("Attributes")

    #loop to add all the attributes to the line chart
    for att in new:
        if(att != 'Date'):
            pl.plot(new['Date'], new[att], label = att)

    pl.legend(loc="best")
    pl.show()

def two():
    pl.scatter(data['Date'], data['Mortality'], color = 'r', label = 'Mortality rate of covid-19')          #scatterplot between mortality rate and air quality index
    pl.scatter(data['Date'], data['Max_PM(2.5)'], color = 'g', label = 'Air quality index')
    pl.title("Scatterplot between Mortality rate and AQI")
    pl.xlabel("Date")
    pl.xticks(rotation = 69)
    pl.ylabel("Mortality rate and AQI")
    pl.show()

def three():
    new = data[['Date', 'Min_Temp', 'Max_Temp', 'Max_Humidity', 'Min_Humidity', 'Max_windspeed', 'Min_windspeed', 'Max_PM(2.5)','Min_PM(2.5)', 'Infected']]
    fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8)) = pl.subplots(nrows=2, ncols=4, sharex=True, sharey=True, figsize=(10,5))

    #creating and plotting subplots for different attributes in order to find the most causative weather attribute
    new.plot(x='Min_Temp', y='Infected', ax=ax1)
    ax1.set_title("Minimum temp")
    new.plot(x='Max_Temp', y='Infected', ax=ax2)
    ax2.set_title("Maximum temp")
    new.plot(x='Min_Humidity', y='Infected', ax=ax3)
    ax3.set_title("Minimum humdity")
    new.plot(x='Max_Humidity', y='Infected', ax=ax4)
    ax4.set_title("Maximum humidity")
    new.plot(x='Min_windspeed', y='Infected', ax=ax5)
    ax5.set_title("Minimum windspeed")
    new.plot(x='Max_windspeed', y='Infected', ax=ax6)
    ax6.set_title("Maximum windspeed")
    new.plot(x='Min_PM(2.5)', y='Infected', ax=ax7)
    ax7.set_title("Minimum AQI ")
    new.plot(x='Max_PM(2.5)', y='Infected', ax=ax8)
    ax8.set_title("Maximum AQI")
    pl.tight_layout()
    pl.show()
    
one()   
two()
three()



