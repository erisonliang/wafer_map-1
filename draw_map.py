'''Taking a map composed of cells, we draw a colored map of a considered value
blue is the highest value while red is the lowest'''

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from decimal import Decimal

def draw(wafer):

    fig = plt.figure(1)
    fig.patch.set_facecolor('#F0FFF0')
    ax = fig.add_subplot(121)

    for cell in wafer.cell_list:
        x,y = cell.x, cell.y
        value = cell.value

        Amplitude, Middle, Maxi, Mini = wafer.amplitude()

        for k in range(len(value)):

            #takes values from the class 'wafer'
            value_k=value[k]
            x_k=x[k]
            y_k=y[k]

            # blue for values above the middle value, red for belows
            if (value_k-Middle)/Amplitude>=0:
                c = (1, 1-(value_k-Middle)/Amplitude , 1-(value_k-Middle)/Amplitude)
            else:
                c = (1+(value_k-Middle)/Amplitude, 1+(value_k-Middle)/Amplitude, 1)

            rect = patches.Rectangle((x_k,y_k), 0.90, 0.90, facecolor=c, edgecolor='k')
            ax.add_patch(rect)

    # diefinition of the legend
    maxPatch = patches.Rectangle((0, 0), 0, 0, facecolor='r', edgecolor='k')
    half_maxPatch = patches.Rectangle((0, 0), 0, 0, facecolor=(1, 0.5, 0.5) , edgecolor='k')
    midPatch = patches.Rectangle((0, 0), 0, 0, facecolor='w', edgecolor='k')
    half_minPatch = patches.Rectangle((0, 0), 0, 0, facecolor=(0.5,0.5,1), edgecolor='k')
    minPatch = patches.Rectangle((0, 0), 0, 0, facecolor='b', edgecolor='k')

    plt.legend([maxPatch,half_maxPatch, midPatch, half_minPatch, minPatch],
               [str(round(Decimal(Maxi),10)),
                str(round(Decimal((Maxi+ Middle)/2),10)),
                str(round(Decimal(Middle),10)),
                str(round(Decimal(Mini+ Middle)/2,10)),
                str(round(Decimal(Mini),10))],
                markerscale=100, frameon=False, fontsize=10)

    plt.title('Real values')
    plt.xlim([-1, 23])
    plt.ylim([-1, 12])
    plt.axis('off')