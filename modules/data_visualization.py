import matplotlib.pyplot as plt

# Data
y_values = y # y is expeted to be an array like [2,4,6,8]
x_values =range(len(y_values))
#y_values = [2,4,6,8]
# Enable "Dark Mode" for the graphs
plt.style.use('dark_background')

#Cyberpunk pink Catot style
plt.plot(x_values, y_values, color='#FF00FF', linewidth=1)
# Labels
plt.title('FCIs Growth')
plt.xlabel('años')
plt.ylabel('Future value of money over 5 years')



# there is a dimentional problem with this array cause y=8 and x=4 in the test code so maybe we can implement a len function to sum to x an num for every elem in

# and the future value functon apply the future value one time for all the fcis, this is inneficient we needs array to create unique time growth by year and win speed, this way we can overlap grapics using matplotlib


