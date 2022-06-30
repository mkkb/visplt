from vispy import scene, app
import sys
import numpy as np

figures = []
axes = []
current_fig = 0
current_ax = 0

def figure(*args, **kwargs):
    global figures, axes, current_fig, current_ax


    if len(args) > 0:
        title = args[0]

    canvas = scene.SceneCanvas(keys='interactive', size=(600, 600), show=True)
    grid = canvas.central_widget.add_grid(margin=10)
    grid.spacing = 0

    title = scene.Label("Plot Title", color='white')
    title.height_max = 40
    grid.add_widget(title, row=0, col=0, col_span=2)

    view = grid.add_view(row=1, col=1, border_color='white')
    view.camera = 'panzoom'

    figures.append(axes)
    axes.append(view)


def plot(*args, **kwargs):
    global figures, axes, current_fig, current_ax
    x = np.zeros(1)
    y = np.zeros(1)
    if len(axes) > 0:
        view = axes[current_ax]
        if len(args) > 2:
            x = args[0]
            y = args[1]
        elif len(args) == 1:
            y = args[0]
            x = np.arange(y.size)

        data = np.array([x, y])
        plot = scene.Line(data, parent=view.scene)

    if 'label' in kwargs.keys():
        print(" plot ->  adding legend: ", kwargs['label'])

def xlabel(lable):
    pass

def ylabel(lable):
    pass

def subplots():
    pass

def show():
    if sys.flags.interactive == 0:
        app.run()