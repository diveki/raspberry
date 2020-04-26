import sys
import numpy as np
import matplotlib.pyplot as plt


def press(event):
    global x
    global y
    print('press', event.key)
    sys.stdout.flush()
    if event.key == 'up':
        y = y +10
        ax.plot(x,y,'go',markersize=10)
        fig.canvas.draw()
    if event.key == 'down':
        y = y -10
        ax.plot(x,y,'go',markersize=10)
        fig.canvas.draw()
    if event.key == 'right':
        x = x +10
        ax.plot(x,y,'go',markersize=10)
        fig.canvas.draw()
    if event.key == 'left':
        x = x -10
        ax.plot(x,y,'go',markersize=10)
        fig.canvas.draw()

# Fixing random state for reproducibility
np.random.seed(19680801)

x = 0
y = 0

fig, ax = plt.subplots()

fig.canvas.mpl_connect('key_press_event', press)

ax.plot(x,y, 'go', markersize=10)
ax.set_xlim([-50,50])
ax.set_ylim([-50,50])
xl = ax.set_xlabel('easy come, easy go')
ax.set_title('Press a key')
plt.show()
