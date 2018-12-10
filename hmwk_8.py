# try it yourself 15.1
from matplotlib import pyplot as plt

# Define data
x_values = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]

# Make plot.
plt.scatter(x_values, cubes, edgecolor='none', s=40)

# Customize plot.
plt.title("Cubes", fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cube of Value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
# Show plot.
plt.show()

from matplotlib import pyplot as plt

# Define data.
x_values = list(range(5001))
cubes = [x**3 for x in x_values]

# Make plot.
plt.scatter(x_values, cubes, edgecolor='none', s=40)

# Customize plot.
plt.title("Cubes", fontsize=26)
plt.xlabel('Value', fontsize=16)
plt.ylabel('Cube of Value', fontsize=16)
plt.tick_params(axis='both', labelsize=16)
plt.axis([0, 5100, 0, 5100**3])

# Show plot.
plt.show()
# try it yourself 15.2
from matplotlib import pyplot as plt

# Define data.
x_values = list(range(5001))
cubes = [x**3 for x in x_values]

# Make plot.
plt.scatter(x_values, cubes, edgecolor='none', c=cubes, cmap=plt.cm., s=40)

# Customize plot.
plt.title("Cubes", fontsize=26)
plt.xlabel('Value', fontsize=16)
plt.ylabel('Cube of Value', fontsize=16)
plt.tick_params(axis='both', labelsize=16)
plt.axis([0, 5100, 0, 5100**3])
# try it yourself 15.3
from matplotlib import pyplot as  plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active
while True:
    # Make a random walk, then plot the points.
    rw = RandomWalk(6000)
    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(dpi=130, figsize=(10,6))

    point_numbers = list(range(rw.num_points))
    plt.plot (rw.x_values, rw.y_values, linewidth=1)

    # Emphasize the first and last points.
    plt.scatter (0, 0, c='blue', edgecolors='none', s=75)
    plt.scatter (rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
                 s=75)

    # Remove the axes.
    plt.axes ().get_xaxis ().set_visible (False)
    plt.axes ().get_yaxis ().set_visible (False)

    plt.show ()

    keep_running = input ("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
# try it yourself 15.4
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks,as long as the program is active.
while True:
      # Make a random walk, and plot the points.
     rw = RandomWalk(6000)
     rw.fill_walk()

     # Set the size of the plotting window.
     plt.figure(dpi=128, figsize=(10, 6))

     point_numbers = list(range(rw.num_points))
     plt.plot(rw.x_values, rw.y_values, linewidth=1)

    # Emphasize the first and last points.
    plt.scatter(0, 0, c='blue', edgecolor='none', s=75 )
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
        s=75)

    # Remove the axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
         break
# try it yourself 15.5
# try it yourself 15.6
# try it yourself 15.7
import pygal

from die_visual import Die

# Create two D8 dice.
die_1 = Die (8)
die_2 = Die (8)

# Make some rolls, and store results in a list.
results = []
for roll_num in range (1000000):
    result = die_1.roll () + die_2.roll ()
    results.append (result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range (2, max_result + 1):
    frequency = results.count (value)
    frequencies.append (frequency)

# Visualize the results.
hist = pygal.Bar ()

hist.title = "Results of rolling two D8 dice 1,000,000 times."
hist.x_labels = [str (x) for x in range (2, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add ('D8 + D8', frequencies)
hist.render_to_file ('dice_visual.svg')
# try it yourself 15.8
import pygal

from die_visual import Die

# Create three D6 dice.
die_1 = Die ()
die_2 = Die ()
die_3 = Die ()

# Make some rolls, and store results in a list.
results = []
for roll_num in range (1000010):
    result = die_1.roll () + die_2.roll () + die_3.roll ()
    results.append (result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range (4,max_result + 1):
    frequency = results.count (value)
    frequencies.append (frequency)

# Visualize the results.
hist = pygal.Bar ()

hist.title = "Results of rolling three D6 dice 1,000,000 times."
hist.x_labels = [str (x) for x in range (4,max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add ('D6 + D6 + D6', frequencies)
hist.render_to_file ('dice_visual.svg')
# try it yourself 15.9
import pygal

from die_visual import Die

# Create two D6 dice.
die_1 = Die ()
die_2 = Die ()

# Make some rolls, and store results in a list.
results = []
for roll_num in range (1000010):
    result = die_1.roll () * die_2.roll ()
    results.append (result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range (1, max_result + 1):
    frequency = results.count (value)
    frequencies.append (frequency)

# Visualize the results.
hist = pygal.Bar ()

hist.title = "Results of multiplying two D6 dice. (1,000,000 rolls)"
hist.x_labels = [str (x) for x in range (1, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add ('D6 * D6', frequencies)
hist.render_to_file ('dice_visual.svg')
# try it yourself 15.10
