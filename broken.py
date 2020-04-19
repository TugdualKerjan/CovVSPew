import matplotlib.pyplot as plt
import matplotlib.animation as animation
from queue import Queue
import numpy as np
import random

font_title = {'name': 'roboto',
              'family': 'sans-serif',
              'color':  '0.137',
              'size': 16,
              }

font_num = {'name': 'roboto',
            'family': 'sans-serif',
            'color':  '0.137',
            'size': 10,
            }

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
plt.subplots_adjust(bottom=0.05, right=0.98, top=0.95,
                    left=0.02, wspace=0.01, hspace=0.01)

ax1.spines['bottom'].set_visible(False)
# ax1.spines['top'].set_visible(False)
# ax1.spines['right'].set_visible(False)
# ax1.spines['left'].set_visible(False)

# ax2.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
# ax2.spines['right'].set_visible(False)
# ax2.spines['left'].set_visible(False)
ax1.xaxis.set_visible(False)
ax2.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)
ax2.yaxis.set_visible(False)

# # ax.tick_params(labeltop='off')  # don't put tick labels at the top
ax2.xaxis.tick_bottom()

length = 100

pewsubs = 14000000 + random.randint(0, 1000000)
corsubs = 2000000 + random.randint(0, 100000)

pewqueue = Queue()
corqueue = Queue()
[pewqueue.put(pewsubs) for i in range(length)]
[corqueue.put(corsubs) for i in range(length)]

xar = [i for i in range(length)]

y_size = 160
image1 = plt.imread("data/pew.jpg")
image2 = plt.imread("data/virus.png")
ax1.autoscale(enable=False) 
ax3 = ax1.twiny()
ax3.spines['bottom'].set_visible(False)
ax3.xaxis.set_visible(False)
ax4 = ax2.twiny()
ax4.spines['top'].set_visible(False)
ax4.xaxis.set_visible(False)


def animate(i):
    global pewsubs, corsubs
    pewsubs += random.randint(0, 7) - 2
    corsubs += random.randint(0, 5) - 2
    if(pewqueue.qsize() == length):
        print(pewqueue.get())
    if(corqueue.qsize() == length):
        print(corqueue.get())
    pewqueue.put(pewsubs)
    corqueue.put(corsubs)
    ax1.clear()
    ax2.clear()
    ax1.plot(xar, list(pewqueue.queue), color="red")
    ax1.text(97, pewsubs, str(pewsubs),
             horizontalalignment='center',
             verticalalignment='bottom', fontdict=font_num)
    ax2.plot(xar, list(corqueue.queue), color="blue")
    ax2.text(97, corsubs, str(corsubs),
             horizontalalignment='center',
             verticalalignment='bottom', fontdict=font_num)
    ax1.text(5, pewsubs + y_size - 30, "PewDiePie", fontdict=font_title, horizontalalignment='left', verticalalignment='top')
    ax1.set_ylim(pewsubs - y_size, pewsubs + y_size)  # outliers only
    ax3.clear()
    ax4.clear()
    ax3.set_xlim(0, 1000)
    ax4.set_xlim(0, 1000)
    ax3.imshow(image1, extent=[3, 80, pewsubs + y_size - 2, pewsubs + y_size - 80])
    ax4.imshow(image2, extent=[3, 80, corsubs + y_size - 2, corsubs + y_size - 80])
    ax2.text(5, corsubs + y_size - 30, "Coronavirus", fontdict=font_title, horizontalalignment='left', verticalalignment='top')
    ax2.set_ylim(corsubs - y_size, corsubs + y_size)  # most of the data


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
