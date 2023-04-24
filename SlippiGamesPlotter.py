import os
import datetime
import matplotlib.pyplot as plt
import calendar

# Specify the directory you want to trawl
directory = "D:\Slippi"

# Create a dictionary to store the counts for each month
month_counts = {}

# Create variables to store start and end dates and total number of games
start_date = None
end_date = None
total_games = 0

# Loop through all the files in the directory
for filename in os.listdir(directory):
    # Only consider files with the extension ".slp"
    if filename.endswith(".slp"):
        # Get the modification time of the file
        modified_time = os.path.getmtime(os.path.join(directory, filename))
        # Convert the modification time to a datetime object
        modified_date = datetime.datetime.fromtimestamp(modified_time)
        # Extract the month and year from the datetime object
        month_year = modified_date.strftime("%Y-%m")
        # Add one to the count for that month
        month_counts[month_year] = month_counts.get(month_year, 0) + 1
        # Update start and end dates and total games played
        if start_date is None or modified_date < start_date:
            start_date = modified_date
        if end_date is None or modified_date > end_date:
            end_date = modified_date
        total_games += 1

# Create lists for the x and y axis data
x_values = []
y_values = []
for month_year, count in sorted(month_counts.items()):
    year, month = month_year.split('-')
    month_name = calendar.month_name[int(month)]
    x_values.append(f"{month_name[:3]}\n{year}")  # add line break
    y_values.append(count)

# Create the line chart
fig, ax = plt.subplots()
ax.plot(x_values, y_values, color="blue")

# Set the title and axes labels
ax.set_title("Number of Games Played per Month")
ax.set_xlabel("Month", labelpad=15)  # add padding to the x-axis label
ax.set_ylabel("Number of Games")






# Add gridlines and adjust margins
ax.grid(True, axis='y')
fig.tight_layout()

# Add a text box with total games played and date range
start_date_str = start_date.strftime("%Y-%m-%d")
end_date_str = end_date.strftime("%Y-%m-%d")
text_box_str = f"Total games played from {start_date_str} to {end_date_str}: {total_games}"
text_box = ax.text(0.5, -0.2, text_box_str, transform=ax.transAxes, fontsize=12,
                    verticalalignment='center', horizontalalignment='center',
                    bbox={'facecolor': 'white', 'alpha': 0.9, 'pad': 10})

# Show the chart
plt.show()
