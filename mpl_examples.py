import matplotlib.pyplot as plt
import matplotlib
import numpy as np

def update_colors(ax, cm = 'jet'):
    """ Update colour of existing lines to span colour table range
    Function from: http://stackoverflow.com/questions/20040597/matplotlib-change-colormap-after-the-fact """
    lines = ax.lines
    cm = plt.get_cmap(cm) # Get colour map: eg OrRd, jet
    colors = cm(np.linspace(0, 1, len(lines)))
    for line, c in zip(lines, colors):
        line.set_color(c)
    ax.legend() # Update legend so its colours match the lines

def mpl_examples():
    ## Using color maps - example from http://stackoverflow.com/questions/8931268/using-colormaps-to-set-color-of-line-in-matplotlib
    # define some random data that emulates your intended code:
    NCURVES = 10
    np.random.seed(101)
    curves = [np.random.random(20) for i in range(NCURVES)]
    values = range(NCURVES)

    fig = plt.figure('Colour table line colours')
    ax = fig.add_subplot(111)

    jet = cm = plt.get_cmap('jet')
    cNorm  = matplotlib.colors.Normalize(vmin=0, vmax=values[-1])
    scalarMap = matplotlib.cm.ScalarMappable(norm=cNorm, cmap=jet)
    print(scalarMap.get_clim())

    lines = []
    for idx in range(len(curves)):
        line = curves[idx]
        colorVal = scalarMap.to_rgba(values[idx])
        colorText = (
            'color: (%4.2f,%4.2f,%4.2f)'%(colorVal[0],colorVal[1],colorVal[2])
            )
        retLine, = ax.plot(line,
                           color=colorVal,
                           label=colorText)
        lines.append(retLine)
    ## Legend
    handles,labels = ax.get_legend_handles_labels()
    legend1 = ax.legend(handles, labels, title = 'A buch of lines', loc='best', ncol=2, framealpha =0.5, fontsize=10, fancybox=True)
    legend1.draggable()
    # legend1.get_frame().set_alpha(0.5)
    ax.grid()
    plt.show(block = False)


    ## Update colour of existing lines to span colour table range
    x = np.linspace(0, 1, 100)
    fig2, ax = plt.subplots()
    for i in range(10):
        y = x**(1+i*0.1)
        ax.plot(x, y, label='%d' % i)
        plt.annotate('%d' % i, xy = (x[50],y[50]),  xycoords='data',
                xytext=(-50, 30), textcoords='offset points',
                # bbox=dict(boxstyle="round4,pad=.5", fc="0.8"),
                arrowprops=dict(arrowstyle="->",                    # arrows pointing to each line
                    connectionstyle="angle3,angleA=0,angleB=-90"))
    ann = ax.annotate('', xy=(0.6, 0.6),  xycoords='data',
        xytext=(0.6, 0.4), textcoords='data',
        arrowprops=dict(arrowstyle="<->",           # Two ended arrow
                        connectionstyle="bar",
                        ec="k",
                        shrinkA=5, shrinkB=5,
                        )
        )
    plt.axis('tight') #changes x and y axis limits such that all data is shown. If all data is already shown, it will move it to the center of the figure
    plt.legend()
    update_colors(ax, cm)
    plt.show(block=False)

    ## Error bars
    fig3 = plt.figure()
    x = np.arange(0.1, 4, 0.5)
    y = np.exp(-x)
    plt.errorbar(x, y, xerr=0.2, yerr=0.4, marker='s', mfc='red', mec='green', ms=20, mew=4)
    plt.show(block=False)

    x = np.linspace(0, 1)
    y = np.sin(4 * np.pi * x) * np.exp(-5 * x)

    ## Get input from the user - click on plot to get x,y
    fig4 = plt.figure()
    plt.fill(x, y, 'r')
    plt.grid(True)
    x = plt.ginput(n=3, timeout=30, show_clicks=True,
       mouse_add=1, mouse_pop=3, mouse_stop=2)
    print("clicked",x)
    plt.show(block=False)

    plt.show

    # input('Press any key to close plots')
    # plt.close('all')

if __name__ == "__main__":
    mpl_examples()
