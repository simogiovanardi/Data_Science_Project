import main
import matplotlib.pyplot as plt

# --------------Graph of Data for Report-------------------

plt.plot(main.data)
plt.title("Number of Passengers per Month in USA")
plt.ticklabel_format(style='plain', axis='y')  # To rescale the Y-axis

start_year = 2003
end_year = 2023
years = [str(year) for year in range(start_year, end_year + 1)]
positions = [i for i in range(0, len(main.data), 12)]
plt.xticks(positions, years)
plt.yticks(rotation=45)
plt.xticks(rotation=45)
plt.show()

# --------------Graph of Data for Report-------------------
