# CPU Usage over Time Plot CLI
## Python Script

Monitor and graph CPU usage over time until the user exits. It uses # the psutil library to gather CPU usage statistics and matplotlib to # generate the graph.
##### Please note that you will need to have `psutil` and `matplotlib` libraries installed in your python environment.
When you run this script, it prints the current CPU usage every second. When you're ready to generate the graph, press Ctrl+C in the terminal. This will generate a graph of CPU usage over time.


```
import time
import psutil
import matplotlib.pyplot as plt

# Create an empty list to store CPU percentages
percentages = []

try:
    while True:
        # Get the current CPU usage as a percentage
        percentage = psutil.cpu_percent(interval=1)
        percentages.append(percentage)

        # Clear the console output
        print(chr(27) + '[2J')
        print('Current CPU usage: %s%%' % percentage)
        print('Press Ctrl+C to generate the graph.')

except KeyboardInterrupt:
    # The user pressed Ctrl+C, generate the graph
    plt.plot(percentages)
    plt.ylabel('CPU Usage (%)')
    plt.xlabel('Time (seconds)')
    plt.title('CPU Usage Over Time')
    plt.show()
```

#macos/dotfiles
